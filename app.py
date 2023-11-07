from flask import Flask, render_template, request
import requests

app = Flask(__name__)
cart_items = []

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


central_server_url = "http://145.93.53.72:5000/add_data"
def create_sample():
    requests.post(central_server_url, json = cart_items)
    
if __name__ == '__main__':
    app.run(debug=True)
    
app.run()
