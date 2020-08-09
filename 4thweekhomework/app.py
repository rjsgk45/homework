from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
# 여길 채워나가세요!
    name = request.form['name']
    size = request.form['size']
    address = request.form['address']
    phone = request.form['phone']

    my_order = {
        'name': name,
        'size': size,
        'address': address,
        'phone': phone
    }
    db.homework.insert_one(my_order)

    return jsonify({'result': 'success', 'msg':'주문이 완료되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
# 여길 채워나가세요!
    orders = list(db.homework.find({},{'_id':False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)