# Proyecto-Guardias-Asistenciales-Backend

download mariadb desde mariabd.org and install
add C:\Program Files\MariaDB 10.6\bin to PATH in system environment variable 
create database sggbd character set utf8mb4 collate utf8mb4_spanish_ci;
CREATE USER  app_user @ localhost  IDENTIFIED BY  app0987user ;
 grant all on sggdb.* to app_user@localhost;

comands:
pip install pipenv
pipenv shell
pipenv install
pipenv install -dev

Routes:
[GET/PUT/DELETE/POST]  /administrator/<int:id>  
[GET]  /administrators 
[GET/PUT/DELETE/POST] /audit/<int:id>  
[GET]  /audits     
[GET/PUT/DELETE/POST]   /guard/<int:id>  
[GET]   /guards  
[GET/PUT/DELETE/POST]   /medical_doctor/<int:id>  
[GET]   /medical_doctors  
[GET/PUT/DELETE/POST]   /notification/<int:id>  
[GET]  /notifications  
[GET/PUT/DELETE/POST]   /service/<int:id>  
[GET]   /services  
[GET/PUT/DELETE/POST]   /subscription/<int:id>  
[GET]  /subscriptions  
[GET/PUT/DELETE/POST]   /zone/<string:name>  
[GET]   /zones  