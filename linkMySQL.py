#works for the android studio app
from flask import Flask, request, jsonify,make_response
import pymysql
import pymysql.cursors

app=Flask(__name__)

connection = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="Yeliep224!",
                             db="userdb",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


@app.route('/product',methods=['GET'])
def showDatabase():
    cur = connection.cursor()
    cur.execute("SELECT * FROM userdb.products")
    productDetails = cur.fetchall()
    #print("Prouct Details",productDetails)
    return jsonify(productDetails)

@app.route('/product',methods=['POST'])
def uploadProduct():
    data = request.get_json()
    id = data['id']
    name = data['name']
    description = data['description']
    #price = data['price']
    #print("id: ", id, " name: ", name, " description: ",description," price: ", price)
    cur = connection.cursor()
    cur.execute("INSERT INTO userdb.products(id,name,description,price) VALUES (%s,%s,%s,%s)", (id,name,description,price))
    connection.commit()

    return jsonify({'id': id,'name': name,'description': description, 'price': price})

@app.route('/product/<id>',methods=['GET'])
def get_product(id):
    cur=connection.cursor()
    cur.execute("SELECT * FROM userdb.products WHERE id=%s",(id))
    product = cur.fetchone()
    #print("Product",product)
    return jsonify(product)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
