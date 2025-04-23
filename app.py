'''Replace me with your flask app'''

from flask import Flask
from Tests.cl import random_cl

app = Flask(__name__)

@app.route('/')
def homepage():
    '''This function returns the homepage.'''
    return "In the url after the /, \
        enter the word random, then a /, \
        then a number between 1 and 10. \
        This will return that many random recipes from the dataset. \
        For example: /random/3 will return 3 random recipes."

@app.route('/random/<int:num_recipes>')
def random_recipes(num_recipes):
    '''This function returns a random recipe from the dataset.'''
    if num_recipes < 1 or num_recipes > 10:
        return "Please enter a number between 1 and 10."
    # Call the function to get random recipes here
    recipes = random_cl(num_recipes)
    # return str(recipes)
    return f"Returning {num_recipes} random recipes.\n {recipes}"

@app.errorhandler(404)
def page_not_found(e):
    '''This function handles 404 errors, which are page not found errors.'''
    return f"Sorry, wrong format. Do this instead: the_url/random/number_of_recipes {str(e)}"

@app.errorhandler(500)
def python_bug(e):
    '''This function handles 500 errors, which are internal server errors.'''
    return f"Eek, a bug! {str(e)}"

if __name__ == '__main__':
    app.run()
