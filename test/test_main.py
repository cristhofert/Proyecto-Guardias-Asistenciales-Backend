""" 



  


#### GET ####
    @pytest.mark.parametrize('_id', admins)
    def test_get_admin(_id):
        response = requests.get(f'{self.url_api}/administrator/{_id}',    headers={
                                'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'})
        print(response.text)
        assert response.status_code == 201


    @pytest.mark.parametrize(
        "id",
        mds)
    def test_get_md(_id):

        response = requests.get(f'{self.url_api}/medical_doctor/{_id}',    headers={
                                'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'})
        print(response.text)
        assert response.status_code == 201


    @pytest.mark.parametrize('_id',
                            guards
                            )
    def test_get_guard(_id):

        response = requests.get(f'{self.url_api}/guard/{_id}',    headers={
                                'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'})
        print(response.text)
        assert response.status_code == 201


    @pytest.mark.parametrize('_id',
                            subscriptions
                            )
    def test_get_assignment(_id):

        response = requests.get(f'{self.url_api}/assignment/{_id}',    headers={
                                'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'})
        print(response.text)
        assert response.status_code == 201


    @pytest.mark.parametrize('_id',
                            services)
    def test_get_service(_id):

        response = requests.get(f'{self.url_api}/service/{_id}',    headers={
                                'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'})
        print(response.text)
        assert response.status_code == 201


    @pytest.mark.parametrize('_id',
                            assignments)
    def test_get_assignment(_id):
        response = requests.get(f'{self.url_api}/subcribe/{medical_doctor__id}/{subscription__id}', headers={
                                'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'})
        print(response.text)
        assert response.status_code == 201

    @pytest.mark.parametrize('_id',
                                zones)
    def test_get_zone(_id):

        response = requests.get(f'{self.url_api}/zone/{_id}',    headers={
                                'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'})
        print(response.text)
        assert response.status_code == 201
    #subscription
    @pytest.mark.parametrize('_id',
                                subscriptions)
    def test_get_subscription(_id):

        response = requests.get(f'{self.url_api}/subscription/{_id}',    headers={
                                'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'})
        print(response.text)
        assert response.status_code == 201

    #superadmin
    @pytest.mark.parametrize('_id',
                                superadmins)
    def test_get_superadmin(_id):

        response = requests.get(f'{self.url_api}/superadmin/{_id}',    headers={
                                    'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'})
        print(response.text)
        assert response.status_code == 201
   """