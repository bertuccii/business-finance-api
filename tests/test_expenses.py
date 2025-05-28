import pytest

@pytest.fixture
def auth_token(client):
    # Register and login user
    client.post('/auth/register', json={
        'username': 'expenseuser',
        'email': 'expenseuser@example.com',
        'password': 'testpassword'
    })
    response = client.post('/auth/login', json={
        'username': 'expenseuser',
        'password': 'testpassword'
    })
    token = response.get_json()['access_token']
    return token

def test_create_expense(client, auth_token):
    response = client.post('/expenses/', json={
        'amount': 50.0,
        'category': 'Test expense'
    }, headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 201
    assert b'Expense created successfully' in response.data

def test_list_expenses(client, auth_token):
    client.post('/expenses/', json={
        'amount': 75.0,
        'category': 'Expense to list'
    }, headers={'Authorization': f'Bearer {auth_token}'})
    
    response = client.get('/expenses/', headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'expenses' in data
    assert len(data['expenses']) >= 1

def test_update_expense(client, auth_token):
    post_resp = client.post('/expenses/', json={
        'amount': 120.0,
        'category': 'Expense to update'
    }, headers={'Authorization': f'Bearer {auth_token}'})
    
    expense_id = post_resp.get_json().get('expense_id')

    response = client.put(f'/expenses/{expense_id}', json={
        'amount': 130.0,
        'category': 'Updated expense'
    }, headers={'Authorization': f'Bearer {auth_token}'})

    assert response.status_code == 200
    assert b'Expense updated successfully' in response.data

def test_delete_expense(client, auth_token):
    post_resp = client.post('/expenses/', json={
        'amount': 90.0,
        'category': 'Expense to delete'
    }, headers={'Authorization': f'Bearer {auth_token}'})
    
    expense_id = post_resp.get_json().get('expense_id')

    response = client.delete(f'/expenses/{expense_id}', headers={'Authorization': f'Bearer {auth_token}'})

    assert response.status_code == 200
    assert b'Expense deleted successfully' in response.data
