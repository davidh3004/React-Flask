from flask import Flask 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/users')
def get_users():
    return {
        "users": ['Alice', 'Bob', 'Charlie'],
    }

@app.route('/api/fruits')
def get_fruits():
    return ['Apple', 'Banana', 'Cherry']

if __name__ == '__main__':
    app.run(debug=True)
# This code creates a simple Flask web application that returns "Hello, World!" when accessed at the root URL. 
# The app runs in debug mode, which is useful for development as it provides detailed error messages and automatically reloads 
# the server when code changes are made.
# To run this code, save it in a file named `main.py` and execute it using Python. Make sure you have Flask installed in your
# Python environment. You can install Flask using pip if you haven't done so already: pip install Flask