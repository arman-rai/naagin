
# 1. make a new project folder
mkdir jyango_manxe && cd jyango_manxe

# 2. create fresh venv inside it
python3 -m venv venv

# 3. activate it
source venv/bin/activate

# 4. upgrade pip (keeps installs smooth)
pip install --upgrade pip

# 5. install django
pip install django

# 6. start the project (root config)
django-admin startproject core .

# 7. create your first app (like checkout)
python manage.py startapp checkout

# 8. test server
python manage.py runserver

# 9. django migration and etc
python manage.py makemigrations → generate migration files after changing models

python manage.py migrate → apply them

python manage.py shell → test Python/Django stuff interactively

python manage.py runserver → start dev server

# file uses
init.py makes the whole directory look like a package
asgi and wsgi, config files that communicate with the web server
urls.py routes to different django apps
settings has db engines, apps list etc
manage.py is a special file that acts as a CLI 

inside an app like `blog`
create a file urls.py which includes different URL routes which will be connected to views

# templating
inside the app folder or blog/templates which will be rendered in the blog/views 

# Features:
Models → define your tables

Views → define your app logic

URLs → map routes

Templates → HTML front-end

Static files → CSS, JS, images


# Web framework 
only framework nothing else, example react is a library not a framweork
