from flask import Flask, render_template, request
import json
app = Flask(__name__)

smth = []
list=[]
n = 0
name = []
address = []

@app.route('/add_data', methods=['POST'])
def add_data():
    global smth
    global n
    global list
    global name
    global address
    list = request.get_json()
    data = list[0]
    name.append(list[1])
    address.append(list[2])
    print(data)
    print(name)
    print(address)
    item_names = [item['name'] for item in data] if data else []
    n+=1
    smth.append({'order': n, 'items': item_names })
    return {}, 200

@app.route('/')
def index():
   return render_template('index.html', items = smth)

@app.route('/Mario')
def Luigi():
   return render_template('Luigi.html', names = name, addresses = address, items = smth)

app.run(host ='192.168.0.119')