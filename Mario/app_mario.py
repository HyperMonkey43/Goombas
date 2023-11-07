from flask import Flask, render_template, request

app = Flask(__name__)

data=''

@app.route('/add_data', methods = ['POST'])
def add_data():
    data = request.get_json()
    return 200
    
@app.route('/')
def index():
   return render_template('mario.html')


app.run()
