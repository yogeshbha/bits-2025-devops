import flask
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Welcome to my Flask application!'

# Add another route with a different endpoint
@app.route('/about')
def about():
    return 'This is the about page'

# Add a route with a dynamic parameter
@app.route('/user/<username>')
def user_profile(username):
    return f'Hello, {username}!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
