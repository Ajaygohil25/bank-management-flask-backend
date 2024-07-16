from app import db

class Account(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    balance= db.Column(db.Float, nullable=False, default=0.0)
    customer_id= db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
                                 
class Customer(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    accounts= db.relationship('Account', backref='customer', lazy = True)

class Employee(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)