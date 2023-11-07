from flask import Flask, render_template, request
app = Flask(__name__)

ceva = "hehe"

@app.route('/add_data', methods = ['POST'])
def add_data():
    
    data = request.get_json()
    print(data)
    return {}
    
@app.route('/')
def index():
   return render_template('index.html', items = ceva)

app.run(host = '192.168.0.119')
