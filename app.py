from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['TITLE'] = "Padoza-TOP"
Bootstrap(app)

@app.route('/')
def index():
    products = ['Ciabatta', 'Baguete', 'Pretzel']
    return render_template('index.html', products=products)

