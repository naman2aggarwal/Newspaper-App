## To run locally make sure to follow below steps:
Install pipenv using pip
pip install pipenv
Navigate to main folder using command line and run command

pipenv shell

Install dependencies

pipenv install

In settings.py file change the EMAIL_HOST, EMAIL_HOST_USER and EMAIL_HOST_PASSWORD according to your needs.
To run local server, run command

python manage.py runserver
Quit the server with CTRL-BREAK and run command "exit" to leave virtual env.


To run project in production make sure to change database to any other commercial database and use commercial web server like nginx, apache etc.

