from flask import Flask, render_template
# IMPORTS

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home_page():
    return render_template('home.html')

@app.route('/market/')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '341351235', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '441351235', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '541351235', 'price': 150}
    ]
    return render_template('market.html', items=items)

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>Username: {username}</h1>'
