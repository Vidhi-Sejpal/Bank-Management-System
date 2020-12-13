from flask import Flask, render_template, request, url_for, redirect,flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__,template_folder='templates',static_folder = 'static')
app.secret_key = 'vidhis'

# save the .sqlite3 file
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHMEY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User_Transfer_List(db.Model):

    __tablename__ = 'User_Transfer_List'

    id = db.Column(db.Integer, primary_key=True) # for numbers use Integer
    username = db.Column(db.Text)    # for text use Text
    bank_id = db.Column(db.Integer)
    balance = db.Column(db.Float)

    def __init__(self, username, bank_id, balance):
        self.username = username
        self.bank_id = bank_id
        self.balance = balance

    def __repr__(self):  
        return(f"{self.id} | {self.username} | {self.bank_id} | {self.balance}")

def create_one_time_entry():
    user_1 = User_Transfer_List('Rhea Shah',3654327790,50000)
    user_2 = User_Transfer_List('Sanya Shah',3654327791,50000)
    user_3 = User_Transfer_List('Akshit Tayade',3654327792,50000)
    user_4 = User_Transfer_List('Tisha Sejpal',3654327793,50000)
    user_5 = User_Transfer_List('Manvi Nathwani',3654327794,50000)
    user_6 = User_Transfer_List('Jay Jain',3654327795,50000)
    user_7 = User_Transfer_List('Darshan Shah',3654327796,50000)
    user_8 = User_Transfer_List('Saroj Sejpal',3654327797,50000)
    user_9 = User_Transfer_List('Pratibha Tayade',3654327798,50000)
    user_10 = User_Transfer_List('Prachi Sejpal',3654327799,50000)

    db.session.add_all([user_1,user_2,user_3,user_4,user_5,user_6,user_7,user_8,user_9,user_10])

    db.session.commit()

def update_entry(sender_name, receiver_name, bank_id, amount):

    sender_name = User_Transfer_List.query.filter_by(username= sender_name).first()
    receiver_name = User_Transfer_List.query.filter_by(username= receiver_name).first()

    if sender_name.bank_id == bank_id:

        sender_name.balance = sender_name.balance - amount
        receiver_name.balance = receiver_name.balance + amount

        db.session.add_all([sender_name, receiver_name])
        db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transferlist' , methods = ['GET', 'POST'])
def transferlist():
    all_users = User_Transfer_List.query.all()
    
    return render_template('transferlist.html', all_users=all_users)

@app.route('/transfer', methods = ['GET', 'POST'])
def transfer():

    if request.method == 'POST':

        sender_name = request.form['sender_name']
        receiver_name = request.form['receiver_name']
        account_no = int(request.form['account_no'])
        amount = float(request.form['amount'])


        sender = User_Transfer_List.query.filter_by(username= sender_name).first()
        receiver = User_Transfer_List.query.filter_by(username= receiver_name).first()

        if receiver.bank_id == account_no:

            sender.balance = float(sender.balance - amount)
            receiver.balance = float(receiver.balance + amount)

            db.session.add_all([sender, receiver])
            db.session.commit()

            all_users = User_Transfer_List.query.all()
            db.session.commit()

            flash(f"Transaction Sucessfull !!  Your Account Number {sender.bank_id} has been credited by Rs {amount} to {receiver_name }")
            return redirect(request.url)

        else :
            flash('Account Number entered is incorrect.Please try again!')
            return redirect(request.url)
        

    return render_template('transfer.html')


if __name__ == "__main__" :
    # db.create_all()
    # create_one_time_entry()
    app.run(debug = True)