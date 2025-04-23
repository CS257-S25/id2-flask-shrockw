'''Tests for Flask application routes.'''
import unittest
import random
from app import app

class TestFlaskRoutes(unittest.TestCase):
    '''Test case for Flask application routes.'''
    def setUp(self):
        self.client = app.test_client()

    def test_homepage(self):
        '''Test the homepage route.'''
        response = self.client.get('/')
        self.assertIn(b"In the url after the /, \
        enter the word random, then a /, \
        then a number between 1 and 10. \
        This will return that many random recipes from the dataset. \
        For example: /random/3 will return 3 random recipes.", response.data)

    def test_random_route(self):
        '''Test the random route.'''
        random.seed(32719)
        response = self.client.get('/random/1')
        self.assertIn(
        b"10: Put the chipotle peppers and adobo sauce in a small food processor",
        response.data)
