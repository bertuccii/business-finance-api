import pytest

@pytest.fixture
def auth_token(client):
    # Register and login user
    client.post('/auth/register', json={
        'username': 'reportuser',
        'email': 'reportuser@example.com',
        'password': 'testpassword'
    })
    response = client.post('/auth/login', json={
        'username': 'reportuser',
        'password': 'testpassword'
    })
    token = response.get_json()['access_token']
    return token

def test_summary_report(client, auth_token):
    # Create a sale
    client.post('/sales/', json={
        'amount': 500.0,
        'description': 'Report sale'
    }, headers={'Authorization': f'Bearer {auth_token}'})

    # Create an expense
    client.post('/expenses/', json={
        'amount': 200.0,
        'category': 'Report expense'
    }, headers={'Authorization': f'Bearer {auth_token}'})

    # Get report
    response = client.get('/reports/summary', headers={'Authorization': f'Bearer {auth_token}'})

    assert response.status_code == 200
    data = response.get_json()
    assert 'report' in data
    assert 'total_sales' in data['report']
    assert 'total_expenses' in data['report']
    assert 'profit' in data['report']
    assert data['report']['total_sales'] >= 500.0
    assert data['report']['total_expenses'] >= 200.0
