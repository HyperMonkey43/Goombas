from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
    
app.run()
