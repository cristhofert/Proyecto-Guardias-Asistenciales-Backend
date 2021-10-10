# Proyecto-Guardias-Asistenciales-Backend

download mariadb desde mariabd.org and install
add C:\Program Files\MariaDB 10.6\bin to PATH in system environment variable 
create database sggbd character set utf8mb4 collate utf8mb4_spanish_ci;
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'app0987user';
GRANT ALL on sggdb.* to app_user@localhost;

Comands:

Build:
pip install pipenv;
Restart (Reiniciar);
pipenv install;
pipenv install -dev;

Run:
 pipenv run python .\api\app.py

Routes:
[GET/PUT/DELETE/POST]  /administrator/<int:id>  
 return {
    'id': 12349875,
    'name': 'Juan Perez',
    'password': '12password23'
    }
[GET]  /administrators 
[GET/PUT/DELETE/POST] /audit/<int:id>
return {
    'id': 1,
    'user_id': 1,
    'action': 'create guard 32',
    'timestamp': '2021-10-08 15:55:35'
}
[GET]  /audits
[GET/PUT/DELETE/POST]   /guard/<int:id>

[GET/POST] /guards 
return {
    'id': 1,
    'created_at': '2021-10-08 15:55:35',
    'updated_at': '2021-10-08 15:55:35',
    'date': '2021-11-25',
    'start_time': '19:45',
    'end_time': '19:45',
    'zone':  {
        'id': 1,
        'name': 'pocito',
        'geotag': 'geotag',
        'longitude': 155.2049,
        'latitude':  63.4378
        },
    'start': '2021-10-08 15:55:35',
    'end': '2021-10-08 15:55:35',
    'subscription': {
        'id': 1,
        'type': 'lista',
        'service_id': 1,
        'service': {
            'name': 'Puerta de Emergencia I',
            'code': 'E1',
            'color': '#55555',
            'id': 1
            },
        'name': 'Puerta de Emergencia I - lista'
        }
}
[GET/PUT/DELETE/POST]   /medical_doctor/<int:id>  
return {
    'id': 41239875,
    'name': 'Pedro Gonzalez',
    'speciality': 'Sirujano',
    'phone': '09166655',
    'email': 'pedrogonzalez@gmail.com'
    }
[GET]   /medical_doctors  
[GET/PUT/DELETE/POST]   /notification/<int:id>
return {
    'id': 1,
    'medical_doctor':  {
        'id': 41239875,
        'name': 'Pedro Gonzalez',
        'speciality': 'Sirujano',
        'phone': '09166655',
        'email': 'pedrogonzalez@gmail.com'
        },
    'message': 'Guardia disponible',
    'read': True,
    'timestamp': '2021-10-08 15:55:35'
}
[GET]  /notifications  
[GET/PUT/DELETE/POST]   /service/<int:id>  
[GET]   /services  
return {
    'name': 'Puerta de Emergencia I',
    'code': 'E1',
    'color': '#55555',
    'id': 1
    }
[GET/PUT/DELETE/POST]   /subscription/<int:id>
return {
    'id': 1,
    'type': 'lista',
    'service_id': 1,
    'service': {
        'name': 'Puerta de Emergencia I',
        'code': 'E1',
        'color': '#55555',
        'id': 1
        },
    'name': 'Puerta de Emergencia I - lista'
}
[GET]  /subscriptions  
[GET/PUT/DELETE/POST] /zone/<string:name>
return {
    'id': 1,
    'name': 'pocito',
    'geotag': 'geotag',
    'longitude': 155.2049,
    'latitude':  63.4378
    }
[GET] /zones
