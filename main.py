# BASE
import os
import sys

#LOCAL IMPORTS
from file_handle import File_man
from conns import Sock_Conn

import flask
# FLASK IMPORT
from flask import Flask, render_template, redirect, url_for, request, flash, Response, session, abort
from datetime import datetime

# DATA_BASE
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




# FLASK_LOGIN
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)


# SECRETE KEY
app.secret_key = "daBoss"
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

# DATA_BASE_ENVs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
# INIT-> DATA_BASE
db = SQLAlchemy(app)


# DATA_BASE_MODEL
class Create_Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)



@app.route('/', methods=["GET","POST"])
def main():
    print("HELLO")
    return "HELLO"


@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        print("ORDER_UP")
        # BOOKINGS FORMS
        try:
            # STANDARD BOOKING
            if request.form['submit_button'] == 'ORDER UP':
                name = str(request.form['client-name'])
                numb = str(request.form['client-num'])
                addr = str(request.form['client-addr'])
                smal = str(request.form['spq'])
                medi = str(request.form['mpq'])
                larg = str(request.form['lpq'])
                



                details_ = [name, numb, addr, smal, medi, larg]
                
                print("NAME:: ", name)
                print()
        except Exception as e:
            print(f"[E]::[>{str(e)}<]")




    return render_template('index.html')













###       ADMIN PAGE        ###
@app.route('/myAdmin', methods=["GET", "POST"])
def admin():
    if "daBoss" in session["state"]:
        print("SESSION:: ", str(session))
        try:
            # # # 
            # ToDo::
            # # #
            #   # DISPLAY ALL ORDER:
                #   # CHECK/UNCHECKED

            return  "<h1>MyAdmin<h1> "#render_template("admin_.html") #,news_up=news_,bookings=bookings,  users=our_users, about=about_)
        except Exception as e:
            print("E:admin:LOGIN:", str(e))
            return render_template("/login")
    else:
        return redirect(url_for("index"))

@app.route('/login', methods=["GET","POST"])
def login():
    pswd = ""
    if request.method == 'POST':
        try:
            if request.form['submit_pswd'] == 'login':
                pswd = str(request.form['PSWD'])
                print("PSWD:: ", str(pswd))
                if "daBoss" in pswd:
                    try:
                        session["state"] = pswd

                    except Exception as se:
                        print("[ERROR]:[SEESION]:",str(se))
                    return redirect(url_for("admin"))
                else:
                    return redirect(url_for("index"))

        except Exception as e:
            print("[ERROR]:[LOGIN]:",str(e))

    return render_template("login_admin.html")

@app.route('/callback', methods=["GET","POST"])
def callback():
    #flow.fetch_token(authorization_response=request.url)
    if not session["state"] == request.args["state"]:
        abort(500) # State doe not match
        return redirect(url_for("index"))

@app.route('/logout', methods=["GET","POST"])
def logout():
    session.clear()
    return redirect(url_for('index'))











if __name__=="__main__":
    #app.config['SERVER_NAME'] = 'bossref.com:5000'
    app.run(host='0.0.0.0', debug=True)