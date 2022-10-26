# Ward Bulletin

A ward bulletin website with a Django backend and custom admin application for easy management.

## Users


## Developers

### Configuration

A docker-compose environment is included, so you can test the website easily. Clone the code, then run `docker-compose build` and `docker-compse up` to start the local instance.

Once the images are running, open the `wardbulletin-djangoapp` image shell and run:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

When deploying:
- make sure the webserver supports Python and Django, and has access to a MySQL database.
- update the django secret key

### Tailwind

Use the following commands to manage the tailwind css files

```bash
./tailwindcss -i wardbulletin/main/static/main/source.css -o wardbulletin/main/static/main/dist.css --watch
./tailwindcss -i wardbulletin/main/static/main/source.css -o wardbulletin/main/static/main/dist.css --minify
