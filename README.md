
# Setup Django for Virtual Enviroment

## Pre Requirement

### install VENV and Django
```
apt install python3.10-venv
```


### Create New Virual Enviroment
```
python3 -m venv ali
```

### active venv
```
source ali/bin/activate
```
### list pakcage for pip
```
pip list
```

### Install LTS Django on Env
```
pip install Django==4.2.4
```
 
*** 


## Create New Project and Start It

### create project
```
django-admin startproject adminPanel
```
### run project
```
cd ../adminPanel/
python manage.py runserver
```

### Migrate All Data to sqlite
```
python manage.py migrate
```

path setting database sqlite3:

` adminPanel/adminPanel/settings.py `


### Create New Admin User
```
python manage.py createsuperuser --username admin
```

***
## Create New App
```
python manage.py startapp newApp
```
after create app you can add `urls.py` into app
after create app must be add into `settings.py` and into block `INSTALLED_APPS`

***
***
***


# Creating a New Django App

This guide will walk you through the process of creating a new Django app using the `python manage.py startapp` command.

## Prerequisites

- Django installed in your project environment
- Basic understanding of Django's project structure and apps

## Steps

1. **Open Terminal:**

    Open your terminal or command prompt.

2. **Navigate to Project Directory:**

    Navigate to the root directory of your Django project using the `cd` command.

    ```bash
    cd path/to/your/django/project
    ```

3. **Create a New App:**

    Run the following command to create a new Django app named `newApp`.

    ```bash
    python manage.py startapp newApp
    ```

4. **App Created:**

    After running the command, you'll see a new directory named `newApp` created within your project's directory. This directory contains the initial files and folders for your new app.

    ```
    project_directory/
    ├── manage.py
    ├── your_project/
    ├── newApp/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── ...
    ```

5. **Customize Your App:**

    Open the files in the `newApp` directory and start customizing your app. Here's a brief overview of the files:

    - `migrations/`: Directory containing database migration files.
    - `__init__.py`: An empty file indicating that the directory is a Python package.
    - `admin.py`: Define admin site configurations for your app's models.
    - `apps.py`: App configuration settings.
    - `models.py`: Define data models for your app.
    - `tests.py`: Write tests for your app.
    - `views.py`: Create views to handle HTTP requests.

6. **Integration with Project:**

    To use your new app within the project, add its name to the `INSTALLED_APPS` list in your project's `settings.py` file.

    ```python
    # settings.py
    INSTALLED_APPS = [
        # ...
        'newApp',
        # ...
    ]
    ```

7. **Run Migrations:**

    After creating your app's models, run migrations to create the necessary database tables.

    ```bash
    python manage.py makemigrations newApp
    python manage.py migrate
    ```


# Adding URLs to Your Django App

This guide will show you how to add URL patterns to your Django app.

## Prerequisites

- Django app created using the `python manage.py startapp` command
- Familiarity with Django views and URL routing

## Steps

1. **Open Your App's Directory:**

    Navigate to your app's directory in your terminal or command prompt.

    ```bash
    cd path/to/your/django/project/newApp
    ```

2. **Create `urls.py` File:**

    Create a new file named `urls.py` within your app's directory.

3. **Define URL Patterns:**

    In the `urls.py` file, you'll define URL patterns that map to your app's views. Here's an example of how to do this:

    ```python
    from django.urls import path
    from . import views

    app_name = 'newApp'

    urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
        # Add more URL patterns as needed
    ]
    ```

    In this example, we're importing views from your app and defining URL patterns using the `path()` function. Replace `views.index` and `views.about` with the actual views you've defined in your app.

4. **Include App URLs in Project URLs:**

    Open your project's main `urls.py` file (usually located in your project's root directory). Include your app's URL patterns using the `include()` function.

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('newApp/', include('newApp.urls')),  # Include your app's URLs
        # Add more URL patterns as needed
    ]
    ```

    Make sure to replace `'newApp'` with the actual



