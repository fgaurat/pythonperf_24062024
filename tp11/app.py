from flask import Flask,render_template
from Customer import Customer
from CustomerDAO import CustomerDAO


app = Flask(__name__)

@app.route("/")
def index():
    with CustomerDAO(r"customers_db.db") as customerDAO:
        customers = list(customerDAO.findAll())

    return render_template('customers.html',customers=customers)

# flask run --debug
@app.route("/toto")
def toto():
    return "<h1>Bonjour, Toto!</h1>"