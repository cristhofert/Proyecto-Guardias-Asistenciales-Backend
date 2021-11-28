import pytest
import requests
import json

ids = {}

@pytest.fixture(scope="module")
def token():
    url_api = 'http://localhost:5000'
    data = {
        "id": 1234562,
        "password": "cris1234"
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
    'users',
    'notifications'
])
def test_gets(token, route):
    url_api = 'http://localhost:5000'

    assert gets(f'{url_api}/{route}', token) == 201

def posts(url_api, token, data):
    response = requests.post(f'{url_api}', json=data, headers={
        'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    return response.status_code

@pytest.mark.parametrize("route, data", [
    ('administrator', {'id': 12342562, 'name': 'weqhlg43.!', 'password':'cris12#@!;34'}),
    ('administrator', {'id': 123400000000000000000000000000000062, 'name': 'ljih73jhg', 'password':'nñcris12345'}),
    ('administrator', {'id': 0, 'name': 'asldjhfl', 'password':'cr232is123456'}),
    ('administrator', {'id': 1222562, 'name': 'l;ajdshfn', 'password':'cris12#@!;34'}),
    ('administrator', {'id': 1234062, 'name': 'khdsafgldsa', 'password':'nñcris12345'}),
    ('administrator', {'id': 9, 'name': 'dsa5fdsahds12', 'password':'cr232is123456'}),
    ('medical_doctor', {'id': 12942562, 'name': 'weqhlg43.!', 'password': 'cris12#@!;34', 'speciality':'sd;jah438@#%^%&()', 'phone': '0932342', 'email': 'lasjdh@asd.cas', 'zone_id':1}),
    ('medical_doctor', {'id': 4984164, 'name': 'ljih73jhg', 'password': 'nñcris12345', 'speciality':'d22sa', 'phone': '093237277', 'email': 'ew3', 'zone_id':1}),
    ('medical_doctor', {'id': 997, 'name': 'asldjhfl', 'password': 'cr232is123456', 'speciality':'dsafsd343f', 'phone': '091283232', 'email': 'caseeas@asdasd.com', 'zone_id':1}),
    ('medical_doctor', {'id': 78945612, 'name': 'l;ajdshfn', 'password': 'cris12#@!;34', 'speciality':'sdff3fcsdsd', 'phone': '09216321', 'email': 'qwe@dscsva.com', 'zone_id':1}),
    ('medical_doctor', {'id': 1294062, 'name': 'khdsafgldsa', 'password': 'nñcris12345', 'speciality':'sdfdsf3ds', 'phone': '092133424', 'email': 'cre@asd.com', 'zone_id':1}),
    ('medical_doctor', {'id': 99, 'name': 'dsa5fdsahds12', 'password': 'cr232is123456', 'speciality':'efwfal23sa', 'phone': '095547', 'email': 'dksf@sfkfsd', 'zone_id':1}),
    ('guard', {'subscription_id': 1, 'zone_id': 1, 'date': '2020-01-01', 'start_time': '10:00:00', 'end_time':'11:00:00', 'quantity':4}),
    ('service', {'name': 'Policlinica I','code': 'PI'}),
    ('zone', {'name': 'San Jose de Mayo', 'geotag': 'geotag', 'longitude': '5461665.55747', 'latitude':  '-4515421.454'}),
    ('subscription', {'type': 'dispersión', 'service_id': 2}),
    ('superadmin', {'id': 2364354, 'name': 'asdasd'})
])
def test_posts(token, route, data):
    url_api = 'http://localhost:5000'

    assert posts(f'{url_api}/{route}/1', token, data) == 201

@pytest.mark.parametrize('medical_doctor_id, subscription_id',
                        [
                            (12942562, 1),
                            (1234000090090000000000000000062, 2),
                            (997, 3),
                            (122999562, 4),
                            (1294062, 5),
                            (99, 6)
                        ])
def test_create_subcribe(medical_doctor_id, subscription_id, token):
    url_api = 'http://localhost:5000'
    response = requests.post(f'{url_api}/subscribe/{medical_doctor_id}/{subscription_id}', headers={
                            'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201

#superadmin
@pytest.mark.parametrize('medical_doctor_id, guard_id',
                            [
                                (12942562, 1)
                            ])
def test_create_assignment(medical_doctor_id, guard_id, token):
    url_api = 'http://localhost:5000'
    response = requests.post(f'{url_api}/assignment/{medical_doctor_id}/{guard_id}', headers={
                                'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201


def get(url_api, token):
    response = requests.get(f'{url_api}', headers={
        'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    return response.status_code

@pytest.mark.parametrize("route, id", [
    ('administrator', 9),
    ('medical_doctor', 99),
    ('guard', 1),
    ('service', 1),
    ('zone', 1),
    ('subscription', 1),
    ('group', 1),
    ('user', 997)
])
def test_get(token, route, id):
    url_api = 'http://localhost:5000'

    assert get(f'{url_api}/{route}/{id}', token) == 201

@pytest.mark.parametrize("month, year", [
    (11, 2021)
])
def test_get_reports(token, month, year):
    url_api = 'http://localhost:5000/reports'

    response = requests.get(f'{url_api}', json={'month': month, 'year': year}, headers={
    'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    assert response.status_code == 201
 
def puts(url_api, token, data):
    response = requests.put(f'{url_api}', json=data, headers={
        'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    return response.status_code

@pytest.mark.parametrize("route, data", [
    ('administrator', {'id': 12342562, 'name': 'eweqhlg43.!', 'password':'cris12#@!;34'}),
    ('administrator', {'id': 123400000000000000000000000000000062, 'name': 'eljih73jhg', 'password':'nñcris12345'}),
    ('administrator', {'id': 0, 'name': 'easldjhfl', 'password':'cr232is123456'}),
    ('administrator', {'id': 1222562, 'name': 'el;ajdshfn', 'password':'cris12#@!;34'}),
    ('administrator', {'id': 1234062, 'name': 'ekhdsafgldsa', 'password':'nñcris12345'}),
    ('administrator', {'id': 9, 'name': 'edsa5fdsahds12', 'password':'cr232is123456'}),
    ('medical_doctor', {'id': 12942562, 'name': 'eweqhlg43.!', 'password': 'cris12#@!;34', 'speciality':'sd;jah438@#%^%&()', 'phone': '0932342', 'email': 'lasjdh@asd.cas', 'zone_id':1}),
    ('medical_doctor', {'id': 4984164, 'name': 'eljih73jhg', 'password': 'nñcris12345', 'speciality':'d22sa', 'phone': '093237277', 'email': 'ew3', 'zone_id':1}),
    ('medical_doctor', {'id': 997, 'name': 'easldjhfl', 'password': 'cr232is123456', 'speciality':'dsafsd343f', 'phone': '091283232', 'email': 'caseeas@asdasd.com', 'zone_id':1}),
    ('medical_doctor', {'id': 78945612, 'name': 'el;ajdshfn', 'password': 'cris12#@!;34', 'speciality':'sdff3fcsdsd', 'phone': '09216321', 'email': 'qwe@dscsva.com', 'zone_id':1}),
    ('medical_doctor', {'id': 1294062, 'name': 'ekhdsafgldsa', 'password': 'nñcris12345', 'speciality':'sdfdsf3ds', 'phone': '092133424', 'email': 'cre@asd.com', 'zone_id':1}),
    ('medical_doctor', {'id': 99, 'name': 'edsa5fdsahds12', 'password': 'cr232is123456', 'speciality':'efwfal23sa', 'phone': '095547', 'email': 'dksf@sfkfsd', 'zone_id':1}),
    ('guard', {'id': 1, 'subscription_id': 1, 'zone_id': 1, 'date': '2020-01-01', 'start_time': '20:00:00', 'end_time':'11:00:00', 'quantity':4}),
    ('service', {'id': 3, 'name': 'ePoliclinica I','code': 'PI'}),
    ('zone', {'id': 2, 'name': 'eSan Jose de Mayo', 'geotag': 'geotag', 'longitude': '5461665.55747', 'latitude':  '-4515421.454'}),
    ('subscription', {'id': 5, 'type': 'dispersión', 'service_id': 2})
])
def test_puts(token, route, data):
    url_api = 'http://localhost:5000'
    id = data['id']
    assert puts(f'{url_api}/{route}/{id}', token, data) == 201 
    

def delete(url_api, token):
    response = requests.get(f'{url_api}', headers={
        'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    print(response.text)
    return response.status_code

@pytest.mark.parametrize("route, id", [
    ('administrator', 9),
    ('medical_doctor', 99),
    ('guard', 1),
    ('service', 1),
    ('zone', 1),
    ('subscription', 1),
    ('group', 1),
    ('user', 997)
])
def test_delete(token, route, id):
    url_api = 'http://localhost:5000'

    assert delete(f'{url_api}/{route}/{id}', token) == 201