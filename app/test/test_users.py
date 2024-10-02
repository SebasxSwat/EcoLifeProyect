def test_get_user(client, user):
    response = client.get(f'/user/{user.id}')
    assert response.status_code == 200
    assert b"test_user" in response.data  # Asegúrate de que el usuario de prueba esté en la respuesta


def test_update_user(client, user):
    response = client.put(f'/user/{user.id}', json={
        'name': 'Updated Name',
        'lastname': 'Updated Lastname',
        'email': 'updated@exeeeeample.com',
        'phone': '9876543210'
    })
    assert response.status_code == 200
    assert b"User updated successfully" in response.data


# def test_get_users(client):
#     response = client.get('/users')
#     assert response.status_code == 200
#     assert b"" in response.data  # Asumiendo que "Usuario" se muestra en la respuesta de los usuarios listados


# # def test_delete_user(client, user):
# #     response = client.delete(f'/users/{user.id}')
# #     assert response.status_code == 200
# #     assert b"Usuario eliminado correctamente" in response.data


# def test_get_user_count(client):
#     response = client.get('/user-count')
#     assert response.status_code == 200
#     json_data = response.get_json()
#     assert 'userCount' in json_data


# def test_get_average_carbon_footprint(client):
#     response = client.get('/average-carbon-footprint')
#     assert response.status_code == 200
#     json_data = response.get_json()
#     assert 'averageCarbonFootprint' in json_data
