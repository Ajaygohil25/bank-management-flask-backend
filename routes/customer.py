from models import Customer
from flask import  request,jsonify, Blueprint
from app import db
import json

customer_bp = Blueprint('customer',__name__)

@customer_bp.route('/create_customer', methods=[ 'POST'])
def create_customer():
    data= request.get_json()
    if 'name' not in data:
        return jsonify({"error": "Name is required field"}), 400
    name=data['name']
    new_data=Customer(name=name)
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"message":"customer is created "})

@customer_bp.route('/checkbalance/<int:id>',methods=['GET']) #here customer
def checkbalance(id):
    customer = Customer.query.get(id)
    if customer is None:
        return jsonify({"error":"No user found"})
    global bankdetails
    for account in customer.accounts:
       bankdetails=account.balance

    response ={
        "name" : customer.name,
        "balance" : bankdetails
    } 
    response= json.dumps(response)
    return response



    

