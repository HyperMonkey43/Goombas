from flask import Flask, render_template, request
import json
app = Flask(__name__)

ceva = []

@app.route('/add_data', methods = ['POST'])
def add_data():
    data = request.get_json()
    # ceva  = json.loads(data)
    print(data)
    # print(ceva[0]['name'])
    return {}
    
@app.route('/')
def index():
   return render_template('index.html', items = ceva)

app.run(host = '145.93.137.61')
