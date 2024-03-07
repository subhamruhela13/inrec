from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

invoices = []
receipts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/printable')
def printable():
    return render_template('printable.html')

@app.route('/create_invoice', methods=['POST'])
def create_invoice():
    data = request.json
    invoice = {
        'id': len(invoices) + 1,
        'customer_name': data['customer_name'],
        'amount': data['amount']
    }
    invoices.append(invoice)
    return jsonify(invoice), 201

@app.route('/create_receipt', methods=['POST'])
def create_receipt():
    data = request.json
    receipt = {
        'id': len(receipts) + 1,
        'customer_name': data['customer_name'],
        'amount_paid': data['amount_paid']
    }
    receipts.append(receipt)
    return jsonify(receipt), 201

@app.route('/invoices')
def get_invoices():
    return jsonify(invoices)

@app.route('/receipts')
def get_receipts():
    return jsonify(receipts)


if __name__ == "__main__":
    app.run(debug=True , port=5000,host='192.168.81.52')#, host= '192.168.81.55',192.168.202.64)