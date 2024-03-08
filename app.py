from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# quotations = {100: {'customer_details': {'customerName': 'subham', 'customerNumber': '3434', 'customerEmail': '4234', 'customerAdd': 'fsdf'}, 'product_details': {'0': 'Happ,3,4,4', '1': 'sds,324,34,33'}}}
quotations = {}

id = len(quotations) + 100

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/printable')
def printable():
    productd = {}
    customer_details = quotations[100]['customer_details']
    for key, value in quotations.items():
        product_details = value.get('product_details', {})
        for product_id, product_info in product_details.items():
            product_info_list = product_info.split(',')
            productd[product_id]=product_info_list
            # product_name, quantity, price, total = product_info_list
            # print(f"Product ID: {product_id}, Name: {product_name}, Quantity: {quantity}, Price: {price}, Total: {total}")
    total_price = sum(int(detail[3]) for detail in productd.values())
    print(total_price)
    return render_template('printable.html', id=id,customer_details = customer_details ,product_details=productd,total_price=total_price)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.form.to_dict(flat=True)
    quotations[id]={'customer_details':data}
    print(quotations)
    return jsonify(quotations), 201

@app.route('/add_products', methods=['POST'])
def add_products():
    data = request.form.to_dict(flat=True)
    quotations[id].update({'product_details': data})
    print(quotations)
    return jsonify(quotations), 201

@app.route('/quotations')
def get_quotations():
    return jsonify(quotations)

if __name__ == "__main__":
    app.run(debug=True ,port=5001)#,port=5000, host= '192.168.81.55',192.168.202.64)