from flask import Blueprint, jsonify
from models import Account, Customer
from app import db
import json

employee_bp=Blueprint('employee',__name__)

@employee_bp.route("/showAllCustomer", methods=['GET','POST'])
def showAllCustomer():
    results= db.session.query(Customer, Account).join(Account).all()
    allConsumer=[]
    for cust, ac in results:
        x={
            "name": cust.name,
            "balance": ac.balance
        }
        allConsumer.append(x)
    y = json.dumps(allConsumer)
    return y

