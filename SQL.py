from flask import Flask, request, jsonify

from flask_mysqldb import MySQL

app = Flask(__name__)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'M@maxeffort.5'
app.config['MYSQL_DB'] = 'cardataset'

mysql = MySQL(app)

@app.route('/sql', methods = ['GET','POST'])

def test2():

    if(request.method == ('POST')):

        cursor = mysql.connection.cursor()
        cursor.execute("use cardataset")
        query = request.json['query']
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify(str(result))

if __name__ == '__main__':
    app.run(port = 7000)
