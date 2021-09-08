# Proyecto-Guardias-Asistenciales-Backend
commands:
pip install virtual env
virtualenv venv

Packeges:
flask
flask-sqlalchemy
flask-marshmallow
marshmallow-sqlalchemy


download mariadb desde mariabd.org and install
add C:\Program Files\MariaDB 10.6\bin to PATH in system environment variable 
create database sggbd character set utf8mb4 collate utf8mb4_spanish_ci;
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'app0987user';
 grant all on sggdb.* to app_user@localhost;

pinenv
pip install pipenv
Excecute
pipenv shell
pipenv install
pipenv install -dev
