from flask import Flask, render_template, request
import requests

app = Flask(__name__)
cart_items = []

global central_server_url
central_server_url = "http://192.168.0.119:5000/add_data"

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    global cart_items

    if request.method == 'POST':
        item_name = request.form.get('item_name')
        item_price = float(request.form.get('item_price'))  
        cart_items.append({"name": item_name, "price": item_price})
    
    total_price = round(sum(item["price"] for item in cart_items), 2)

    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/checkout', methods=['POST'])
def checkout():
    global name
    global address
    name = request.form.get('name')
    address = request.form.get('address')
    if request.method == 'POST':
        create_sample()
    cart_items.clear()    
    return render_template('checkout.html', name=name, address=address)

def create_sample():
    requests.post(central_server_url, json = [cart_items,name,address])

if __name__ == '__main__':
    app.run(port=5000,debug=True)
    
app.run()
