from flask import Flask,request, render_template,redirect,url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_DB']= "flask"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "1234"
app.config['MYSQL_CURSORCLASS']="DictCursor"
app.secret_key="myapp"

conn = MySQL(app)

@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method  == 'POST':
        username = request.form['username']
        password = request.form['password']
        con=conn.connection.cursor()
        sql = "insert into login(username,password) values(%s,%s)"
        result=con.execute(sql,(username,password))
        con.connection.commit()
        con.close()


        if result:
            return redirect(url_for('login'))
        else:
            return render_template('login.html')
    
    return render_template('login.html')

@app.route('/stu_details/', methods = ['POST', 'GET'])
def signup():
    if request.method  == 'POST':
        username = request.form['username']
        Roll_Number= request.form['Roll_Number']
        Department = request.form['Department']
        section= request.form['section']
        year_of_studying = request.form[' year_of_studying']
        feedback= request.form['  feedback']
    
        con=conn.connection.cursor()
        sql = "insert into signup(username,Roll_Number,Department,section,year_of_studying) values(%s,%s,%s,%s,%s)"
        result=con.execute(sql,(username,Roll_Number,Department,section,year_of_studying))
        con.connection.commit()
        con.close()
        return  redirect(url_for('login'))
        
    return render_template('stu_details.html')

@app.route('/index/',methods=['GET', 'POST'])
def index(): 
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)