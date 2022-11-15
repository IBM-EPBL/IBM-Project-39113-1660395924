import os

import mysql.connector
from flask import Flask, redirect, render_template, request

app=Flask(__name__)
app.secret_key=os.urandom(24)

conn=mysql.connector.connect(host = "remotemysql.com" ,  user ="ZVJPoqsB7J", password="BfKWHI3fWw", database="ZVJPoqsB7J")
cursor=conn.cursor()

@app.route('/')
def login():
    return render_template("/login.html")



@app.route('/register')
def about():
    return render_template("/register.html")

@app.route('/home')
def home():
    return render_template("/home.html")


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('Password')

    cursor.execute("""SELECT * FROM 'user_login' WHERE 'email' LIKE '{}' AND 'password' LIKE '{}' """
                    .format(email,password))
    users=cursor.fetchall()

    if len(users)>0:
        return redirect('/home')
    else:
        return render_template("/login.html")


@app.route('/add_user', methods=["POST"])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    contact = request.form.get('ucnt')
    password = request.form.get('upwd')

    cursor.execute("""INSERT INTO 'user_id'( 'name', 'email', 'contact', 'password') VALUES (NULL, '{}', '{}', '{}', '{}')""".format(name,email,contact,password))
    conn.commit()

    cursor.execute("""SELECT * FROM 'users' WHERE 'email' LIKE '{}'""".format(email))
    myuser=cursor.fetchall()
    return redirect('/home')

@app.route('/logout')
def logout():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)