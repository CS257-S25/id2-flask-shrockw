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
        self.assertIn(b"Returning 1 random recipes.\n 10: Put the chipotle peppers and adobo sauce in a small food processor or blender and blend until the mixture turns into a smooth pur\xc3\xa9e. Set aside. The chipotle pur\xc3\xa9e can be made in advance, stored in an airtight container, and refrigerated for up to 2 months.\nOn a cutting board, sprinkle the garlic with a large pinch of salt and gather it into a small mound. Holding the blunt side of the knife with both hands, press and scrape the knife\xe2\x80\x99s sharp end, holding it at a slight angle, across the garlic mound to flatten it. Repeat, dragging it across the garlic, until you have a smooth paste. Set aside.\nIn a small bowl, mix the cornstarch and 1\xc2\xbd tsp. of the evaporated milk into a slurry. Pour the rest of the evaporated milk into a medium saucepan and stir in the slurry. Bring to a boil over medium-high heat, whisking constantly. Turn the heat to low and add the Cheddar gradually by the handful, stirring until the Cheddar is melted and the mixture is smooth. Add the cream cheese and whisk until it melts. Stir in the mayonnaise, pimento peppers, 1\xc2\xbd tsp. of the chipotle pur\xc3\xa9e, and the garlic paste. Season with salt. Transfer to a serving bowl or keep it warm in a slow cooker and serve immediately.\nTo reheat the sauce, microwave it, stirring every 30 seconds, until fully melted.\n", response.data)
