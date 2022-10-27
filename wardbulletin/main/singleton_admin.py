from django.urls import re_path
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.db.utils import OperationalError
import logging 

logger = logging.getLogger(__name__) 

class DjangoSingletonModelAdmin(admin.ModelAdmin):
	change_form_template = "django_singleton_admin/change_form.html"

	def has_add_permission(self, request):
		if self.model.objects.all().count() == 0:
			return True
		return False

	def has_change_permission(self, request, obj=None):
		if self.model.objects.all().count() == 1:
			return True
		return False

	def has_view_permission(self, request, obj=None):
		return True

	def has_delete_permission(self, request, obj=None):
		return False

	def get_urls(self):
		urls = super(DjangoSingletonModelAdmin, self).get_urls()
		try:
			model_name = self.model._meta.model_name
			self.model._meta.verbose_name_plural = self.model._meta.verbose_name
			url_name_prefix = '%(app_name)s_%(model_name)s' % {
				'app_name': self.model._meta.app_label,
				'model_name': model_name,
			}
			custom_urls = [
				re_path(r'^$',
					self.admin_site.admin_view(self.change_view),
					{'object_id': str(self.singleton_instance_id)},
					name='%s_change' % url_name_prefix),
			]
			# By inserting the custom URLs first, we overwrite the standard URLs.
		except Exception as e:
			logger.warning("Django Singleton failed to build URLs, likely because a database migration is required.")
			custom_urls = []
		return custom_urls + urls

	def _changeform_view(self, request, object_id, form_url, extra_context):
		# self.model.objects.get_or_create(pk=self.singleton_instance_id)
		if extra_context is None:
			extra_context = {}
		extra_context.update({'show_save_and_add_another': False})

		return super()._changeform_view(
			request,
			object_id,
			form_url=form_url,
			extra_context=extra_context,
		)

	@property 
	def singleton_instance_id(self):
		if self.model.objects.all():
			return self.model.objects.all()[0].pk
		else:
			return 1
