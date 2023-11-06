from flask import Flask, render_template

app = Flask(__name__)
cart_items = []  # Initialize an empty cart
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
        cart_items.append(item_name)  # Add the item to the cart

    return render_template('cart.html', cart_items=cart_items)


    
if __name__ == '__main__':
    app.run(debug=True)
    
app.run()
