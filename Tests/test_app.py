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
        b"Hot Pimento Cheese Dip",
        response.data)

    def test_random_route_invalid_large(self):
        '''Test the random route with an invalid number.'''
        response = self.client.get('/random/11')
        self.assertIn(
        b"Please enter a number between 1 and 10.",
        response.data)

    def test_random_route_invalid_small(self):
        '''Test the random route with an invalid number.'''
        response = self.client.get('/random/0')
        self.assertIn(
        b"Please enter a number between 1 and 10.",
        response.data)

    def test_random_route_wrong_format(self):
        '''Test the random route with a wrong format.'''
        response = self.client.get('/random/abc')
        self.assertIn(
        b"Sorry, wrong format. Do this instead: the_url/random/number_of_recipes",
        response.data)

    def test_random_route_wrong_url(self):
        '''Test the random route with a wrong format.'''
        response = self.client.get('/rando')
        self.assertIn(
        b"Sorry, wrong format. Do this instead: the_url/random/number_of_recipes",
        response.data)
