from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'info'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def userInfo():

    if request.method == 'POST':
        names = request.form['fname']
        years = request.form['ynumber']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO infos(name, year) VALUES(%s, %s)", (names, years))
        mysql.connection.commit()
        cur.close()
        return redirect('/info')
    return render_template('user.html')


@app.route('/info')
def printInfo():
    cur = mysql.connection.cursor()
    resVal = cur.execute("SELECT * FROM infos")
    if resVal > 0:
        infos = cur.fetchall()
        return render_template('infos.html', infos=infos)

if __name__ == '__main__':
    app.run()
