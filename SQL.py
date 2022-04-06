#import libraries
from flask import Flask, request, jsonify
import pymongo
from flask_mysqldb import MySQL

app = Flask(__name__)

# SQL connection configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'dataset'

mysql = MySQL(app)

#mongodb connection
client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.aa8cm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

#SQL request
@app.route('/sql', methods = ['GET','POST'])
def test2():
    if(request.method == ('POST')):

        cursor = mysql.connection.cursor()
        cursor.execute("use cardataset")
        query = request.json['query']
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify(str(result))

#mongodb request
@app.route('/mongo', methods = ['GET'])
def test3():
    db = client['New']
    coll = db['inneuron_collection']
    return jsonify(str(list(coll.find().limit(5))))
   
#run flask app
if __name__ == '__main__':
    app.run(port = 7000)
