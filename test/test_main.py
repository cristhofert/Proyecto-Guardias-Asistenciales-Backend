import pytest
import requests
import json

ids = {}

@pytest.fixture(scope="module")
def token():
    url_api = 'http://localhost:5000'
    data = {
        "id": 98765431,
        "password": "jp123"
    }
    response = requests.post(f'{url_api}/login', json=data)
    return response.json()['access_token']

def gets(url_api, token):
    global ids
    response = requests.get(f'{url_api}', headers={
        'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    if response.status_code == 200:
        if url_api in ids:
            ids[url_api].append(response.json()['id'])
        else:
            ids[url_api] = [response.json()['id']]
    print(ids)
    return response.status_code

@pytest.mark.parametrize("route", [
    ('administrators'),
    ('medical_doctors'),
    'guards',
    'services',
    'zones',
    'subscriptions',
    'groups',
    'notifications'
])
def test_gets(token, route):
    assert gets(f'http://localhost:5000/{route}', token) == 201

def posts(url_api, token, data):
    response = requests.post(f'{url_api}', json=data, headers={
        'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    return response.status_code

@pytest.mark.parametrize("route, data", [
    ('administrator', {'id': 55555561, 'name': 'Carlos Casa', 'password':'nñcris12345'}),
    ('administrator', {'id': 55555555, 'name': 'Daniel De León', 'password':'cr232is123456'}),
    ('administrator', {'id': 99999999, 'name': 'Pablo Rodriguez', 'password':'cris12#@!;34'}),
    ('medical_doctor', {'id': 55555549, 'name': 'ljih jhg', 'password': 'nñcris12345', 'speciality':'pedriatria', 'phone': '099237277', 'email': 'ew3@gmail.com', 'zone_id':1}),
    ('medical_doctor', {'id': 99999983, 'name': 'asld jhfl', 'password': 'cr232is123456', 'speciality':'pedriatria', 'phone': '091283232', 'email': 'caseeas@gmail.com', 'zone_id':2}),
    ('medical_doctor', {'id': 78945612, 'name': 'laj dshfn', 'password': 'cris12#@!;34', 'speciality':'anestesista', 'phone': '09216321', 'email': 'qwe@hotmail.com', 'zone_id':1}),
    ('medical_doctor', {'id': 12940624, 'name': 'Javier Espino', 'password': 'nñcris12345', 'speciality':'mediciana general', 'phone': '094133424', 'email': 'cre@hotmail.com', 'zone_id':2}),
    ('guard', {'subscription_id': 1, 'zone_id': 1, 'date': '2021-12-20', 'start_time': '10:00:00', 'end_time':'11:00:00', 'quantity': 1}),
    ('guard', {'subscription_id': 1, 'zone_id': 1, 'date': '2021-12-25', 'start_time': '10:00:00', 'end_time':'12:00:00', 'quantity': 5}),
    ('service', {'name': 'Policlinica I','code': 'PI'}),
    ('zone', {'name': 'San Jose de Mayo', 'geotag': 'geotag', 'longitude': '-34.90328', 'latitude':  '-56.18816'}),
    ('superadmin', {'id': '00000038', 'name': 'Federico Rodriguez'})
])
def test_posts_valid(token, route, data):
    assert posts(f'http://localhost:5000/{route}/1', token, data) == 201

@pytest.mark.parametrize("route, data", [
    ('administrator', {'id': '00000016', 'name': 'Jhon Smith', 'password':'cris12#@!;34'}),
    ('medical_doctor', {'id': '00000022', 'name': 'weq hlassa', 'password': 'cris12#@!;34', 'speciality':'medicina general', 'phone': '093234234', 'email': 'lasjdh@gmsil.com', 'zone_id':3}),
    ('administrator', {'id': '00000011', 'name': 'Jhon Smith', 'password':'cris12#@!;34'}),
    ('administrator', {'id': '0000001', 'name': 'Carlos Casa', 'password':'nñcris12345'}),
    ('administrator', {'id': 99999999, 'name': 'Pablo Rodriguez', 'password':''}),
    ('administrator', {'id': 88888888, 'name': '', 'password':'12ssas#@s;34'}),
    ('medical_doctor', {'id': 32456724, 'name': '', 'password': 'cris12#@!;34', 'speciality':'medicina general', 'phone': '093234234', 'email': 'lasjdh@gmsil.com', 'zone_id':3}),
    ('medical_doctor', {'id': 55555549, 'name': 'ljih jhg', 'password': '', 'speciality':'pedriatria', 'phone': '099237277', 'email': 'ew3@gmail.com', 'zone_id':1}),
    ('medical_doctor', {'id': 25557684, 'name': 'asld jhfl', 'password': 'cr232is123456', 'speciality':'', 'phone': '091283232', 'email': 'caseeas@gmail.com', 'zone_id':2}),
    ('medical_doctor', {'id': 78945612, 'name': 'laj dshfn', 'password': 'cris12#@!;34', 'speciality':'anestesista', 'phone': '092163214', 'email': 'qwe@hotmail.com', 'zone_id':1}),
    ('medical_doctor', {'id': 12940624, 'name': 'Javier Espino', 'password': 'nñcris12345', 'speciality':'mediciana general', 'phone': '994133424', 'email': 'cre@hotmail.com', 'zone_id':2}),
    ('medical_doctor', {'id': 43566784, 'name': 'Javier Espino', 'password': 'nñcsds22345', 'speciality':'mediciana general', 'phone': '994133424', 'email': 'cre@dsfds', 'zone_id':2}),
    ('medical_doctor', {'id': 85698793, 'name': 'Javier Espino', 'password': 'nñcri32345', 'speciality':'mediciana general', 'phone': '994133424', 'email': 'crehotmail.com', 'zone_id':2}),
    ('medical_doctor', {'id': 52020393, 'name': 'Javier Espino', 'password': 'nñris42345', 'speciality':'mediciana general', 'phone': '994133424', 'email': 'cre@hotmail.com', 'zone_id':0}),
    ('medical_doctor', {'id': 43912139, 'name': 'Javier Espino', 'password': 'nñcrs52345', 'speciality':'mediciana general', 'phone': '994133434', 'email': 'cre@hotmail.com', 'zone_id':5}),
    ('guard', {'subscription_id': 0, 'zone_id': 1, 'date': '2021-12-20', 'start_time': '10:00:00', 'end_time':'11:00:00', 'quantity': 1}),
    ('guard', {'subscription_id': 1, 'zone_id': 0, 'date': '2021-12-20', 'start_time': '10:00:00', 'end_time':'11:00:00', 'quantity': 1}),
    ('guard', {'subscription_id': 1, 'zone_id': 1, 'date': '2019-12-20', 'start_time': '10:00:00', 'end_time':'11:00:00', 'quantity': 1}),
    ('guard', {'subscription_id': 1, 'zone_id': 1, 'date': '2021-12-20', 'start_time': '001:00:00', 'end_time':'11:00:00', 'quantity': 1}),
    ('guard', {'subscription_id': 1, 'zone_id': 1, 'date': '2021-12-20', 'start_time': '10:00:00', 'end_time':'111:00:00', 'quantity': 1}),
    ('guard', {'subscription_id': 1, 'zone_id': 1, 'date': '2021-12-20', 'start_time': '10:00:00', 'end_time':'11:00:00', 'quantity': 0}),
    ('guard', {'subscription_id': 1, 'zone_id': 1, 'date': '2021-12-20', 'start_time': '10:00:00', 'end_time':'11:00:00', 'quantity': -1}),
    ('guard', {'subscription_id': 1, 'zone_id': 9, 'date': '2021-12-20', 'start_time': '10:00:00', 'end_time':'111:00:00', 'quantity': 1}),
    ('guard', {'subscription_id': 100, 'zone_id': 1, 'date': '2021-12-20', 'start_time': '10:00:00', 'end_time':'11:00:00', 'quantity': 1}),
    ('service', {'name': '','code': 'PI'}),
    ('service', {'name': 'Policlinica I','code': ''}),
    ('zone', {'name': '', 'geotag': 'geotag', 'longitude': '-34.90328', 'latitude':  '-56.18816'}),
    ('zone', {'name': 'San Jose de Mayo', 'geotag': '', 'longitude': '-34.90328', 'latitude':  '-56.18816'}),
    ('zone', {'name': 'San Jose de Mayo', 'geotag': 'geotag', 'longitude': '', 'latitude':  '-56.18816'}),
    ('zone', {'name': 'San Jose de Mayo', 'geotag': 'geotag', 'longitude': '-34.90328', 'latitude':  ''}),
    ('subscription', {'type': 'este tipo no exite', 'service_id': 2}),
    ('subscription', {'type': '', 'service_id': 2}),
    ('subscription', {'type': 'dispersión', 'service_id': 0}),
    ('subscription', {'type': 'lista', 'service_id': 5})
])
def test_posts_invalid(token, route, data):

    assert posts(f'http://localhost:5000/{route}/1', token, data) >= 400
 
@pytest.mark.parametrize('medical_doctor_id, subscription_id',
                        [
                            ('55555561', '-1'),
                            ('122999562', '1000'),
                            ('1294062', '5'),
                            ('99', '-6')
                        ])
def test_post_subcribe_invalid(medical_doctor_id, subscription_id, token):
    response = requests.post(f'http://localhost:5000/subscribe/{medical_doctor_id}/{subscription_id}', headers={
                            'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code >= 400

@pytest.mark.parametrize('medical_doctor_id, subscription_id',
                        [
                            ('55555549', '1'),
                            ('38974126', '2'),
                            ('99999983', '14'),
                            ('62836582', '15')
                        ])
def test_post_subcribe_valid(medical_doctor_id, subscription_id, token):
    response = requests.post(f'http://localhost:5000/subscribe/{medical_doctor_id}/{subscription_id}', headers={
                            'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201

#superadmin
@pytest.mark.parametrize('medical_doctor_id, guard_id',
                            [
                                (99999983, 2),
                                (55555549, 3),
                            ])
def test_post_assignment_valid(medical_doctor_id, guard_id, token):
    url_api = 'http://localhost:5000'
    response = requests.post(f'{url_api}/assignment/{medical_doctor_id}/{guard_id}', headers={
                                'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201

@pytest.mark.parametrize('medical_doctor_id, guard_id',
                            [
                                (25557684, 1),
                                (43566784, 0),
                                (12942562, 9)
                            ])
def test_post_assignment_invalid(medical_doctor_id, guard_id, token):
    response = requests.post(f'http://localhost:5000/assignment/{medical_doctor_id}/{guard_id}', headers={
                                'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 500

def get(url_api, token):
    response = requests.get(f'{url_api}', headers={
        'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    return response.status_code

@pytest.mark.parametrize("route, id", [
    ('administrator', 55555555),
    ('medical_doctor', 78945612),
    ('guard', 1),
    ('service', 1),
    ('zone', 1),
    ('subscription', 1),
    ('group', 1)
])
def test_get(token, route, id):
    url_api = 'http://localhost:5000'

    assert get(f'{url_api}/{route}/{id}', token) == 201

@pytest.mark.parametrize("month, year", [
    (11, 2021)
])
def test_post_reports(token, month, year):
    url_api = 'http://localhost:5000/reports'

    response = requests.post(url_api, json={'month': month, 'year': year}, headers={
    'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201

def puts(url_api, token, data):
    response = requests.put(f'{url_api}', json=data, headers={
        'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    return response.status_code

@pytest.mark.parametrize("route, data", [
    ('administrator', {'id': 55555561, 'name': 'Carlos Casa Ernandez', 'password':'nñcris12345'}),
    ('administrator', {'id': 55555555, 'name': 'Daniel De León', 'password':'cr232is123456'}),
    ('administrator', {'id': 99999999, 'name': 'Pablo Rodriguez', 'password':'cris12#@!;34E'}),
    ('medical_doctor', {'id': 55555549, 'name': 'ljih jhg', 'password': 'nñcris12345', 'speciality':'pedriatria', 'phone': '099237277', 'email': 'ew3@gmail.com', 'zone_id':1}),
    ('medical_doctor', {'id': 99999983, 'name': 'asld jhfl', 'password': 'cr232is123456', 'speciality':'pedriatria', 'phone': '091283232', 'email': 'caseeas@gmail.com', 'zone_id':2}),
    ('medical_doctor', {'id': 78945612, 'name': 'laj dshfn', 'password': 'cris12#@!;34', 'speciality':'anestesista', 'phone': '09216321', 'email': 'qwe@hotmail.com', 'zone_id':1}),
    ('medical_doctor', {'id': 12940624, 'name': 'Javier Espino', 'password': 'nñcris12345', 'speciality':'mediciana general', 'phone': '094133424', 'email': 'cre@hotmail.com', 'zone_id':2}),
    ('guard', {'id': 1,'subscription_id': 1, 'zone_id': 1, 'date': '2021-12-20', 'start_time': '10:00:00', 'end_time':'11:00:00', 'quantity': 1}),
    ('guard', {'id': 1,'subscription_id': 1, 'zone_id': 1, 'date': '2021-12-25', 'start_time': '10:00:00', 'end_time':'12:00:00', 'quantity': 5}),
    ('service', {'id': 1,'name': 'Policlinica I','code': 'PI'}),
    ('zone', {'id': 1,'name': 'San Jose de Mayo', 'geotag': 'geotag', 'longitude': '-34.90328', 'latitude':  '-56.18816'})
])
def test_puts_valid(token, route, data):
    url_api = 'http://localhost:5000'
    id = data['id']
    assert puts(f'{url_api}/{route}/{id}', token, data) == 201

@pytest.mark.parametrize("route, data", [
    ('administrator', {'id': 555555, 'name': 'Carlos Casa', 'password':'nñcris12345'}),
    ('administrator', {'id': 0, 'name': 'Daniel De León', 'password':'cr232is123456'}),
    ('medical_doctor', {'id': 7894561, 'name': 'laj dshfn', 'password': 'cris12#@!;34', 'speciality':'anestesista', 'phone': '09216321', 'email': 'qwe@hotmail.com', 'zone_id':1}),
    ('medical_doctor', {'id': 1294062454, 'name': 'Javier Espino', 'password': 'nñcris12345', 'speciality':'mediciana general', 'phone': '094133424', 'email': 'cre@hotmail.com', 'zone_id':2}),
    ('guard', {'id': -1,'subscription_id': 1, 'zone_id': 1, 'date': '2021-12-20', 'start_time': '10:00:00', 'end_time':'11:00:00', 'quantity': 1}),
    ('guard', {'id': 1000,'subscription_id': 1, 'zone_id': 1, 'date': '2021-12-25', 'start_time': '10:00:00', 'end_time':'12:00:00', 'quantity': 5}),
    ('service', {'id': 1,'name': 'Policlinica I'}),
    ('zone', {'id': 1000,'name': 'San Jose de Mayo', 'geotag': 'geotag', 'longitude': '-34.90328', 'latitude':  '-56.18816'}),
    ('superadmin', {'id': '00000038', 'name': 'Federico Rodriguez'})
])
def test_puts_invalid(token, route, data):
    url_api = 'http://localhost:5000'
    id = data['id']
    assert puts(f'{url_api}/{route}/{id}', token, data) >= 400

def delete(url_api, token):
    response = requests.get(f'{url_api}', headers={
        'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    return response.status_code

@pytest.mark.parametrize("route, id", [
    ('administrator', 99999999),
    ('medical_doctor', 78945612),
    ('guard', 1),
    ('service', 1),
    ('zone', 1),
    ('subscription', 1),
    ('group', 1)
])
def test_delete_valid(token, route, id):
    url_api = 'http://localhost:5000'
    assert delete(f'{url_api}/{route}/{id}', token) == 201 

@pytest.mark.parametrize("route, id", [
    ('administrator', 9999999),
    ('administrator', 999999999),
    ('medical_doctor', 255573484),
    ('medical_doctor', 1294064),
    ('guard', -1),
    ('guard', 0),
    ('service', -1),
    ('service', 0),
    ('zone', -1),
    ('zone', 0),
    ('subscription', -1),
    ('subscription', 0),
    ('group', -1),
    ('group', 0)
])
def test_delete_invalid(token, route, id):
    url_api = 'http://localhost:5000'
    assert delete(f'{url_api}/{route}/{id}', token) >= 400 

@pytest.mark.parametrize("subscription_id, zone_id, date, start_time, end_time, quantity, repeat", [
    ( 4, 1, '2021-12-20', '10:00:00', '11:00:00', 1, ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']),
    ( 3, 2, '2021-12-20', '10:00:00', '11:00:00', 1, ['Monday',]),
    ( 2, 3, '2021-12-20', '10:00:00', '11:00:00', 1, ['Monday', 'Tuesday']),
    ( 1, 4, '2021-12-27', '10:00:00', '12:00:00', 5, ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
])
def test_post_guards_valid(token, subscription_id, zone_id, date, start_time, end_time, quantity, repeat):
    response = requests.post('http://localhost:5000/guards', json={'subscription_id': subscription_id, 'zone_id': zone_id,
        'date': date, 'start_time': start_time, 'end_time': end_time, 'quantity': quantity, 'repeat': repeat},
    headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201

@pytest.mark.parametrize("subscription_id, zone_id, date, start_time, end_time, quantity, repeat", [
    ( 1, 9, '2021-12-20', '10:00:00', '11:00:00', 1, []),
    ( 1, 9, '2021-12-20', '10:00:00', '11:00:00', 1, ['thing']),
    ( 1, 1, '2021-12-27', '', '12:00:00', 5, ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
])
def test_post_guards_invalid(token, subscription_id, zone_id, date, start_time, end_time, quantity, repeat):
    response = requests.post('http://localhost:5000/guards', json={'subscription_id': subscription_id, 'zone_id': zone_id,
        'date': date, 'start_time': start_time, 'end_time': end_time, 'quantity': quantity, 'repeat': repeat},
    headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code >= 400