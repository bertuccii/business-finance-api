import pytest

@pytest.fixture
def auth_token(client):
    # Register and login user
    client.post('/auth/register', json={
        'username': 'salesuser',
        'email': 'salesuser@example.com',
        'password': 'testpassword'
    })
    response = client.post('/auth/login', json={
        'username': 'salesuser',
        'password': 'testpassword'
    })
    token = response.get_json()['access_token']
    return token

def test_create_sale(client, auth_token):
    response = client.post('/sales/', json={
        'amount': 100.0,
        'description': 'Test sale'
    }, headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 201
    assert b'Sale created successfully' in response.data

def test_list_sales(client, auth_token):
    # First create a sale
    client.post('/sales/', json={
        'amount': 150.0,
        'description': 'Sale to list'
    }, headers={'Authorization': f'Bearer {auth_token}'})
    
    response = client.get('/sales/', headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'sales' in data
    assert len(data['sales']) >= 1

def test_update_sale(client, auth_token):
    # Create a sale
    post_resp = client.post('/sales/', json={
        'amount': 200.0,
        'description': 'Sale to update'
    }, headers={'Authorization': f'Bearer {auth_token}'})
    
    sale_id = post_resp.get_json().get('sale_id')

    # Update the sale
    response = client.put(f'/sales/{sale_id}', json={
        'amount': 250.0,
        'description': 'Updated sale'
    }, headers={'Authorization': f'Bearer {auth_token}'})

    assert response.status_code == 200
    assert b'Sale updated successfully' in response.data

def test_delete_sale(client, auth_token):
    # Create a sale
    post_resp = client.post('/sales/', json={
        'amount': 300.0,
        'description': 'Sale to delete'
    }, headers={'Authorization': f'Bearer {auth_token}'})
    
    sale_id = post_resp.get_json().get('sale_id')

    # Delete the sale
    response = client.delete(f'/sales/{sale_id}', headers={'Authorization': f'Bearer {auth_token}'})

    assert response.status_code == 200
    assert b'Sale deleted successfully' in response.data
