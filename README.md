
README TO CLONE AND OPEN DJANGO PROJECT
* Ensure Python is installed: https://www.python.org/downloads/
* Ensure Pycharm is installed: https://www.jetbrains.com/pycharm/download/?section=windows
* Ensure Git is installed: https://git-scm.com/downloads

- Create a folder to clone the repository into.
- cd into that file in a terminal.
- clone the repository with this command: "git clone https://github.com/dacayed/Art_Store_Database"
- open PyCharm, Open the project folder where the repository was cloned
- Open PyCharm Terminal, run "pip install -r requirements.txt"
- install pillow: "pip install Pillow"
- create ".env" file in root directory
- run "python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'" in your terminal, copy the output for next step
- write "SECRET_KEY="your-secret-key-here"" paste what you copied in 
- on terminal run "python manage.py migrate"
- create a superuser: python manage.py createsuperuser
- create an account
- open web application: http://127.0.0.1:8000/
- type admin into url: http://127.0.0.1:8000/admin
- log into superuser account
- add desired art products through the admin view
- 
   WEBSITE FEATURES
- add users by registering
- log in and log out of website
- create reviews be filling in the form (must be signed in)
- add orders to order list by pressing order button on details page
- view and cancel orders on order list page
- supports media image formats
