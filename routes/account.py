from flask import Flask,Blueprint,request,jsonify
from models import Account,Customer
from app import db

account_bp = Blueprint('account',__name__)

@account_bp.route('/create_account', methods=['POST'])
def create_account():
    data=request.get_json()
    customer_id = data['id']
    if not customer_id:
        return jsonify({"error": "not found"})
    new_account = Account(customer_id=customer_id)
    db.session.add(new_account)
    db.session.commit()
    return jsonify({"success":"account created"})

@account_bp.route("/add_amount/<int:id>", methods=["POST"])
def add_amount(id):
    data=request.get_json()
    amount=data["amount"]
    account = Account.query.get(id)
    if not account:
        return jsonify({"error":"No account found"})
    account.balance= account.balance+amount
    db.session.add(account)
    db.session.commit()
    return jsonify({"success":"balance is updated "})
    

@account_bp.route("/widraw_amount/<int:id>", methods=["POST"])
def widraw_amount(id):
    data=request.get_json()
    amount=data["amount"]
    account = Account.query.get(id)
    if not account:
        return jsonify({"error":"No account found"})
    if account.balance<amount:
        return jsonify({"error":"Not enough balance"})
    else:
        account.balance= account.balance-amount
        db.session.add(account)
        db.session.commit()
        return jsonify({"success":"balance is updated ", "account": account.balance})
    
@account_bp.route("/delete/<int:id>")
def delete_account(id):
    data=request.get_json()
    id= int(data['id'])
    account =  Account.query.get(id)
    if not account: 
        return jsonify({"error": "Account not found"})
    else:
        db.session.delete(account)
        db.session.commit()
        return jsonify({"success":"account deleted successfully"})
    