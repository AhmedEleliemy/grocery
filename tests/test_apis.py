from app import create_app

#this function is to test the main page.
def test_index():
    """
    GIVEN a flask application configured for testing
    WHEN the '/' main page is requested (Get)
    THEN check if the response is valid
    """
    flask_app= create_app()
    with flask_app.test_client() as test_client:
        response=test_client.get('/')
        assert(response.status_code==200)

#this function is to test the get /items End Point
def test_get_items():
    """
    GIVEN a flask application configured for testing
    WHEN the '/items' request all available grocery items (Get)
    THEN check if the response is valid
    """
    flask_app= create_app()
    with flask_app.test_client() as test_client:
        response=test_client.get('/items')
        assert(response.status_code==200)