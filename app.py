from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)

@app.route('/')

def homepage():
    return render_template("home.html")

@app.route('/contact',methods = ["GET","POST"] )

def contactus():
    if request.method=='POST':
        name = request.form.get("name")
        Phone_no = request.form.get("phone")
        Email = request.form.get("email")
        State = request.form.get("state")
        Country = request.form.get("country")
        Message = request.form.get("message")
        print(name,Phone_no,Email,State,Country,Message)
        conn = sqlite3.connect('contactus.db')
        cur = conn.cursor()
        cur.execute(f'''
        INSERT INTO CONTACTS VALUES(
                    "{name}","{Phone_no}","{Email}",
                    "{Country}","{State}","{Message}"
        )
        ''')
        conn.commit()
        return render_template("message.html")
    else:
        return render_template('contactus.html')







if __name__=='__main__':
    app.run()

