from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///bank_management.db'
db =SQLAlchemy(app)

from models import Account,Customer,Employee
with app.app_context():
    db.create_all()


from routes.customer import customer_bp
from routes.account import account_bp
from routes.employee import employee_bp

app.register_blueprint(customer_bp, url_prefix='/customer')
# /customer/create_customer --> for create customer  data: name
# /customer/checkbalance/<int:id> --> for check balance of customer 
app.register_blueprint(account_bp, url_prefix='/account')
# /account/create_account  --> data, customer id
# /account/add_amount/<int:id>  -- account id,data: amount
# /widraw_amount/<int:id>  -- account id,data: amount
# /delete/<int:id>  -- account id

app.register_blueprint(employee_bp,url_prefix="/employee")
# /employee/showAllCustomer


'''if __name__=='__main__':
    app.run(debug=True)'''