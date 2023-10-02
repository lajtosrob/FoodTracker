# Food Tracker

This is a food tracking application built using **Django 3**, **HTML 5**, **CSS 3**, and **Bootstrap 5** that uses a **SQLite** database to store data. Charts are built using **Chart.js 2**.

## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the application](#run-the-application)
- [Adding data to the application](#add-data-to-the-application)
- [Copyright and License](#copyright-and-license)


## Prerequisites

Install the following prerequisites:

1. [Python](https://www.python.org/downloads/)
2. [Visual Studio Code](https://code.visualstudio.com/download)


## Installation

### 1. Create a virtual environment

From the **root** directory run:

```bash
python -m venv venv
```

### 2. Activate the virtual environment

From the **root** directory run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

### 3. Install required dependencies

From the **root** directory run:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

From the **root** directory run:

```bash
touch .env
```

The **touch** command will create the **.env** file in the **root** directory. This command works on Mac and Linux but not on Windows. If you are a Windows user, instead of using the command line, you can create the **.env** file manually by navigating in Visual Studio Code to the Explorer, and selecting the option **New File**.


Next, declare environment variables in the **.env** file. Make sure you don't use quotation marks around the strings.

```bash
SECRET_KEY=yoursecretkey
DEBUG=True
DATABASE_NAME=food
DATABASE_USER=yourusername
DATABASE_PASS=yourpassword
DATABASE_HOST=localhost
```

### 6. Run migrations

From the **root** directory run:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

### 7. Create an admin user to access the Django Admin interface

From the **root** directory run:

```bash
python manage.py createsuperuser
```

When prompted, enter a username, email, and password.


## Run the application

From the **root** directory run:

```bash
python manage.py runserver
```

## View the application

Go to http://127.0.0.1:8000/ to view the application.


## Add data to the application

Add data through Django Admin.

Go to http://127.0.0.1:8000/admin to access the Django Admin interface and sign in using the admin credentials.


## Copyright and License

Copyright © 2023 Fülöpné Kiss Anikó, Lajtos Róbert. Code released under the MIT license.
