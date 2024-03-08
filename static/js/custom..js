let products = [];

function addProduct() {
    let productDiv = document.createElement('div');
    productDiv.className = 'product';
    productDiv.innerHTML = `
        <label for="ProdDesc" class="form-label">Description</label>
        <input type="text" class="form-control" name="ProdDesc" placeholder="Enter Product Description">
        <label for="Qty" class="form-label">Qty</label>
        <input type="number" class="form-control" name="Qty" placeholder="Enter Qty">
        <label for="Rate" class="form-label">Rate</label>
        <input type="number" class="form-control" name="Rate" placeholder="Enter Rate/-">
        <label for="amount" class="form-label">Amount</label>
        <input type="number" class="form-control" name="amount" placeholder="Enter amount">
        <button type="button" class="btn btn-danger" onclick="deleteProduct(this)">Delete</button>
    `;
    let form = document.getElementById('productForm');
    let buttonsDiv = document.getElementById('buttons');
    form.insertBefore(productDiv, buttonsDiv);
};

function deleteProduct(button) {
    var productDiv = button.parentNode;
    productDiv.remove();
}

function submitCustomer() {
    const url = '/add_customer';
    let form = document.getElementById('customerForm');
    let formData = new FormData(form);
    sendFormData(formData,url);
};

function submitProducts() {
    const url = '/add_products'
    var productForms = document.querySelectorAll('.product');
    var formData = new FormData();

    productForms.forEach(function(form, index) {
        var desc = form.querySelector('input[name="ProdDesc"]').value;
        var qty = form.querySelector('input[name="Qty"]').value;
        var rate = form.querySelector('input[name="Rate"]').value;
        var amount = form.querySelector('input[name="amount"]').value;

        let plist = []
        plist.push(desc,qty,rate,amount)
        formData.append(index,plist);
        // formData.append(''+ index +'[description]', desc);
        // formData.append(''+ index +'[quantity]', qty);
        // formData.append(''+ index +'[rate]', rate);
        // formData.append(''+ index +'[amount]', amount);
    });
    sendFormData(formData,url);
}

function printPage() {
    window.print();
};

function sendFormData(formData,url) {
    fetch(url, {
        method: 'POST',
        body: formData
    }).then(response => {
        if (response.ok) {
            alert('submitted successfully');
        } else {
            alert('Failed to submit form');
        }
    });
}