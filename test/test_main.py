import pytest
import requests
import json

url_api = 'http://127.0.0.1:5000'
token = ''


def test_client():
    global token
    data = {
        "id": 1234562,
        "password": "cris1234"
    }
    response = requests.post(f'{url_api}/login', json=data)
    assert response.status_code == 201
    token = response.json()['access_token']


def test_get_user():
    response = requests.get(f'{url_api}/login', headers={
                            'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    assert response.status_code == 201


@pytest.mark.parametrize(
    "id, name, password",
    [
        (12342562, 'weqhlg43.!', 'cris12#@!;34'),
        (123400000000000000000000000000000062, 'ljih73jhg', 'nñcris12345'),
        (0, 'asldjhfl', 'cr232is123456'),
        (1222562, 'l;ajdshfn', 'cris12#@!;34'),
        (1234062, 'khdsafgldsa', 'nñcris12345'),
        (9, 'dsa5fdsahds12', 'cr232is123456')
    ])
def test_create_admin(id, name, password):
    data = {
        "id": id,
        "name": name,
        "password": password
    }
    response = requests.post(f'{url_api}/administrator/1', json=data,  headers={
                             'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201


@pytest.mark.parametrize(
    "id, name, password, speciality, phone, email, zone_id",
    [
        (12942562, 'weqhlg43.!', 'cris12#@!;34',
         'sd;jah438@#%^%&()', '0932342', 'lasjdh@asd.cas', 1),
        (1234000090090000000000000000062, 'ljih73jhg',
         'nñcris12345', '][\[d22sa', '0932372732', 'ew3][=', 1),
        (997, 'asldjhfl', 'cr232is123456', 'dsafsd343f',
         '091283232', 'caseeas@asdasd.com', 1),
        (122999562, 'l;ajdshfn', 'cris12#@!;34',
         'sdff3fcsdsd', '09216321', 'qwe@dscsva.com', 1),
        (1294062, 'khdsafgldsa', 'nñcris12345',
         'sdfdsf3ds', '092133424', 'cre@asd.com', 1),
        (99, 'dsa5fdsahds12', 'cr232is123456',
         'efwfal23sa', '324asddas12', 'dksf@sfkfsd', 1)
    ])
def test_create_md(id, name, password, speciality, phone, email, zone_id):
    data = {
        "id": id,
        "name": name,
        "password": password,
        "speciality": speciality,
        "phone": phone,
        "email": email,
        "zone_id": zone_id
    }
    response = requests.post(f'{url_api}/medical_doctor/1', json=data,  headers={
                             'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201


@pytest.mark.parametrize('subscription_id, zone_id, date, start_time, end_time, quantity',
                         [
                             (1, 1, '2020-01-01', '10:00:00', '11:00:00', 4),
                             (1, 1, '2020-01-01', '10:00:00', '11:00:00', 5),
                             (1, 1, '2020-01-01', '10:00:00', '11:00:00', 4),
                             (1, 1, '2020-01-01', '10:00:00', '11:00:00', 1),
                             (1, 1, '2020-01-01', '10:00:00', '11:00:00', 2),
                             (1, 1, '2020-01-01', '10:00:00', '11:00:00', 1),
                             (1, 1, '2020-01-01', '10:00:00', '11:00:00', 5),
                             (1, 1, '2020-01-01', '10:00:00', '11:00:00', 2),
                             (1, 1, '2020-01-01', '10:00:00', '11:00:00', 5),
                             (1, 1, '2020-01-01', '10:00:00', '11:00:00', 2)
                         ])
def test_create_guard(subscription_id, zone_id, date, start_time, end_time, quantity):
    data = {
        "subscription_id": subscription_id,
        "zone_id": zone_id,
        "date": date,
        "start_time": start_time,
        "end_time": end_time,
        "quantity": quantity
    }
    response = requests.post(f'{url_api}/guard/1', json=data,  headers={
                             'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201


@pytest.mark.parametrize('subscription_id, zone_id, date, start_time, end_time, quantity',
                         [
                             (12942562, 1),
                             (1234000090090000000000000000062, 2),
                             (997, 3),
                             (122999562, 4),
                             (1294062, 5),
                             (99, 6)
                         ])
def test_create_assignment(medical_doctor_id, guard_id):
    data = {
        'medical_doctor_id': medical_doctor_id,
        'guard_id': guard_id
    }
    response = requests.post(f'{url_api}/assignment/1', json=data,  headers={
                             'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201


@pytest.mark.parametrize('subscription_id, zone_id, date, start_time, end_time, quantity',
                         [
                             ('Policlinica I', 'PI'),
                             ('Policlinica II', 'P2'),
                             ('Policlinica III', 'PI3'),
                             ('Puerta de Emergencia IV', 'PE4'),
                             ('Piso 1', 'P1'),
                             ('Piso 2', 'P2'),
                             ('Piso 3', 'P3'),
                             ('Piso 4', 'P4'),
                             ('Piso 5', 'P5'),
                             ('Piso 6', 'P6')
                         ])
def test_create_service(name, code):
    data = {
        'name': name,
        'code': code
    }
    response = requests.post(f'{url_api}/service/1', json=data,  headers={
                             'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201


@pytest.mark.parametrize('subscription_id, medical_doctor_id',
                         [
                             (12942562, 1),
                             (1234000090090000000000000000062, 2),
                             (997, 3),
                             (122999562, 4),
                             (1294062, 5),
                             (99, 6)
                         ])
def test_create_assignment(medical_doctor_id, subscription_id):
    response = requests.post(f'{url_api}/subcribe/{medical_doctor_id}/{subscription_id}', headers={
                             'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201
