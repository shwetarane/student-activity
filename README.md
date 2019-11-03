# Students Activity

## Getting Started

* Install [python](https://www.python.org/downloads/) and pip

* (optional, but recommended) Install virtual environment, [https://virtualenvwrapper.readthedocs.io/en/latest/install.html](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) -> For this step, make sure you create the following directory before update the bash file. For MAC Users, its bash_profile in your home directory.
```bash
  mkdir $HOME/.virtualenvs
 ```
* Create virtual environment for your project, say dev1

  ```bash
  mkvirtualenv dev1
  ```

* Install [django](https://docs.djangoproject.com/en/2.2/topics/install/)

  ```bash
  pip install django
  ```

## Setting up the project
Needs [git](https://git-scm.com/download/win) installed and set-up on your machine.  
In Terminal, ensure virtual environment is activated, where you want the project,

To activate virtual environment, ```workon dev1```

```git clone git@github.com:shwetarane/student-activity.git```

```python manage.py makemigrations```

```python manage.py migrate```

### To run the project:

```python manage.py createsuperuser```

To access django-admin, use creds for superuser we just created : ```localhost:8000/admin/```

```python manage.py runserver```

If encoutered with error on running, install the following binaries as well :-

```pip3 install pillow```

```pip3 install django-crispy-forms```

Also make sure, to import Django in the corresponding python & virtual environment. 

```python3```

```import django```

## Functions

* **Student** **Login**
* **Register**
* **Update** **Information** 
* Username/Password Retrieval
* Student/Faculty search
* Textbook Search
* Purchase Books
* Find a Roommate
* Meal Plan
* Purchase Bus Tickets
* Sport Activities and Parties
* Election polls



