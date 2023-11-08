from flask import Flask, render_template, request
import json
app = Flask(__name__)

smth = []
n = 0
@app.route('/add_data', methods=['POST'])
def add_data():
    global smth
    global n
    
    data = request.get_json()
    item_names = [item['name'] for item in data] if data else []
    n+=1
    smth.append({'order': n, 'items': item_names })
    return {}, 200

@app.route('/')
def index():
   return render_template('index.html', items = smth)

app.run(host ='145.93.49.97')