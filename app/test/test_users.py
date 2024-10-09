import uuid

def test_get_user(client, user):
    
    response = client.get(f'/user/{user.id}')

    assert response.status_code == 200

    assert b"test_user" in response.data  


def test_add_user(client):

    usuario = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "password123",
        "name": "Juan",
        "lastname": "Daza",
        "phone": "1234567890",
    }

    response = client.post('/auth/register', json=usuario)


    assert response.status_code == 201
    assert response.get_json()["message"] == "Registro exitoso"

    data = response.get_json()
    user_data = data['user']

    assert user_data['name'] == 'Juan'
    assert user_data['lastname'] == 'Daza'


def test_update_user(client, user):
    data = {
        'name': 'Updated Name',
        'lastname': 'Updated Lastname',
        'email': f"fabian{uuid.uuid4()}@example.com",  
        'phone': '3144073535'
    }
    
    response = client.put(f'/user/{user.id}', json=data)
    
    assert response.status_code == 200
    assert b"User updated successfully" in response.data
    


def test_get_users(client):

    response = client.get('/users')

    assert response.status_code == 200
    assert b"" in response.data  


def test_delete_user(client, user):

    response = client.delete(f'/users/{user.id}')

    assert response.status_code == 200
    assert b"Usuario eliminado correctamente" in response.data


def test_get_user_count(client):

    response = client.get('/user-count')

    json_data = response.get_json()

    assert response.status_code == 200

    assert 'userCount' in json_data


def test_get_average_carbon_footprint(client):

    response = client.get('/average-carbon-footprint')
    assert response.status_code == 200

    json_data = response.get_json()

    assert 'averageCarbonFootprint' in json_data
