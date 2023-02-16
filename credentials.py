import sqlite3
from flask import Flask,render_template,request

# main 
app=Flask(__name__)
app.config['DEBUG']=True

# index route 
@app.route('/',methods=['GET','POST'])
def index():
  return render_template('index1.html')


# signup route 
@app.route('/signup',methods=["GET","POST"])
def signup():
  if request.method=="POST":
    username=request.form['username']
    email=(request.form['email'])
    password=request.form['password']
    c_password=request.form['c_password']

    #sql
    connection=sqlite3.connect('database1.db')
    cursor=connection.cursor()
    #logic

    is_email=cursor.execute("SELECT password FROM user_info WHERE email=:email",{'email':email}).fetchone()
    if not is_email:
      if c_password!=password:
          return render_template('signup.html')

      cursor.execute("INSERT INTO user_info(name,email,password) VALUES(?,?,?)",(username,email,password))
      connection.commit()
      return render_template('login1.html')
    else:
      return render_template('signup.html')  

  return render_template('signup.html')  


# login route
@app.route('/login',methods=['GET','POST'])
def login():
  if request.method=="POST":
    email=request.form['email']
    password=request.form['password']
    
    # sql
    connection=sqlite3.connect('database1.db')
    cursor=connection.cursor()
    mail_c=cursor.execute('SELECT email FROM user_info WHERE email=:email',{'email':email}).fetchone()
    
    if not mail_c:
      return render_template('login1.html')
    
    pass_=cursor.execute('SELECT password FROM user_info WHERE email=:email',{'email':email}).fetchone()
 
    if pass_[0]==password:
      print("lala")
      return "<h1>Sucessful !!!</h1>"
    
  return render_template('login1.html')  


if __name__=="__main__":
  app.run()
