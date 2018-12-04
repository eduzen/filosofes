
def test_about(client):
    response = client.get('/about')

    assert response.status_code == 200
    assert response.context_data['view'].__class__.__name__ == 'AboutView'


def test_contact(client):
    response = client.get('/contact')

    assert response.status_code == 200
    assert response.context_data['view'].__class__.__name__ == 'ContactView'


def test_thanks(client):
    response = client.get('/thanks')

    assert response.status_code == 200
    assert response.context_data['view'].__class__.__name__ == 'ThanksView'
