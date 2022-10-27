'''Main site admin actions'''
from django.contrib import admin
from django.contrib import messages
from django.contrib.admin import helpers
from django.contrib.admin.utils import model_ngettext, quote
from django.db.models import Q
from django.template.response import TemplateResponse
from django.utils.html import format_html
from django.utils.text import capfirst
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy
from django.urls import NoReverseMatch, reverse
from .models import BulletinGroup


@admin.action(permissions=['change'], description=gettext_lazy("Mark selected rows as Enabled"))
def make_enabled(modeladmin, request, queryset):
	queryset.update(enabled=True)

@admin.action(permissions=['change'], description=gettext_lazy("Mark selected rows as Disabled"))
def make_disabled(modeladmin, request, queryset):
	queryset.update(enabled=False)

@admin.action(permissions=['change'], description=gettext_lazy("Invert Enabled/Disabled state for selected rows"))
def make_inverted(modeladmin, request, queryset):
	queryset.update(enabled=Q(enabled=False))

@admin.action(permissions=['change'], description=gettext_lazy("Change Bulletin Group"))
def change_bulletin_group(modeladmin, request, queryset):

	opts = modeladmin.model._meta

	if request.POST.get("post"):

		queryset.update(bulletin_group=request.POST.get("group"))
		# logger.warning(queryset)
		messages.add_message(request, messages.INFO, f'Updated {queryset.count()} Bulletin Entry groups')

		# Return None to display the change list page again.
		return None

	objects_name = model_ngettext(queryset)

	title = _("Select new Bulletin Group")

	def format_callback(obj):
		model = obj.__class__
		has_admin = model in admin.site._registry
		opts = obj._meta

		no_edit_link = "%s: %s" % (capfirst(opts.verbose_name), obj)

		if has_admin:
			try:
				admin_url = reverse(
					f"{admin.site.name}:{opts.app_label}_{opts.model_name}_change",
					None,
					(quote(obj.pk),),
				)
			except NoReverseMatch:
				# Change url doesn't exist -- don't display link to edit
				return no_edit_link

			# Display a link to the admin page.
			return format_html(
				'{}: <a href="{}">{}</a>', capfirst(opts.verbose_name), admin_url, obj
			)
		else:
			# Don't display link to edit, because it either has no
			# admin or is edited inline.
			return no_edit_link

	to_update = [format_callback(obj) for obj in queryset]

	context = {
		**modeladmin.admin_site.each_context(request),
		"title": title,
		"subtitle": None,
		"objects_name": str(objects_name),
		"groups": BulletinGroup.objects.all(),
		"update_objects": to_update,
		"queryset": queryset,
		"opts": opts,
		"action_checkbox_name": helpers.ACTION_CHECKBOX_NAME,
		"media": modeladmin.media,
	}

	request.current_app = modeladmin.admin_site.name

	# Display the confirmation page
	return TemplateResponse(
		request,
		"admin/change_bulletin_group.html",
		context,
	)
