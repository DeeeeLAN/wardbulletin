# Ward Bulletin

A ward bulletin website with a Django backend and custom admin application for easy management.

---
## Users

Quick start:

1. 
2. 
3. 

For more detailed instructions, please see [USERS.md](USERS.md)

---
## Web Administrators

Requirements for hosting:

- MySQL Server
- Python application support

Here is an outline of the steps needed to get the website deployed. You will likely need to adjust the steps based on your exact environment.

1. Make sure you have your domain and hosting purchased and configured. This is outside the scope of this project, but if you have any questions about how I set my site up, feel free to ask on the discussions page
1. Download the latest release of the repository
1. Copy the code to your webserver
1. Install pipenv with `pip install -r requirements-deploy.txt`
1. Install the dependencies with `pipenv install`
1. Create a `.env` file based on the `.env.example` file provided, making sure to fill int he correct details for your database
1. If you are running the wsgi appliation yourself, it might look something like this:
    - `gunicorn --bind :8000 wardbulletin.wsgi.prod:application`
    - If you are using a webhost, they likely will handle this for you, just follow their guide on running a Python application
1. In the wardBulletin directory, run:
    - `python manage.py makemigrations` - Prepares any missing migrations
    - `python manage.py migrate` - Creates the database configuration
    - `python manage.py createsuperuser` - Creates an admin user account
1. Upload a logo to `wardbulletin/main/static/main/images/logos` if you want a logo in the top-left corner of the page
1. Modify or replace the folder of temple photos at `wardbulletin/main/static/main/images/temples` as you see fit.
1. Import the quote_data.json file into the quote table (unless you plan on using your own quotes)
    - `python manage.py loaddata ../quote_data.json`
1. In the root of the folder, run `./tailwindcss -i wardbulletin/main/static/main/source.css -o wardbulletin/main/static/main/dist.css --minify`
1. In the wardBulletin directory, run:
    - `python manage.py collectstatic` - Collects the static files for Django
    - `python manage.py check --deploy`, and take care of any issues reported
1. Log into the admin interface at your chosen admin URL in the `.env` file
1. The django migration will pre-load the quotes table - you can modify the contents if desired, or leave it as-is. 
1. You don't need to expose all the tables to your bulletin editors - I recommend creating a permissions group and settings permissions for just the tables they need to access.
1. Create user accounts for anybody who needs access to the admin interface, and assign permissions as needed.
1. Go through the tables and set up your initial data as desired.

Congratulations! You should now have a fully configured ward bulletin website for your ward.


---
## Developers

If you are interested in contributing or want to modify the project for your own purposes, here are some notes to get you started.

### Configuration

A docker-compose environment is included, so you can test the website easily. Clone the code, install the developer dependencies with `pip install -r requirements-developer.txt`, then run `docker-compose build` and `docker-compose up` to start the local instance.

Once the images are running, open the `wardbulletin-djangoapp` image shell and run:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

To add new dependencies, add them to `Pipfile`, then either rebuild the image, or open the image shell and run `pipenv lock` and `pipenv install --system` to install them.

If you are able to host a docker instance for production use, remove the `docker-compose.override.yml` file so docker uses the production Dockerfile instead of the developer version. 

### Tailwind

Use the following commands to manage the tailwind css files

```bash
./tailwindcss -i wardbulletin/main/static/main/source.css -o wardbulletin/main/static/main/dist.css --watch # Have this running while editing the code
./tailwindcss -i wardbulletin/main/static/main/source.css -o wardbulletin/main/static/main/dist.css --minify
