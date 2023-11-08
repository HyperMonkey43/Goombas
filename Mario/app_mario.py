from flask import Flask, render_template, request
import json
app = Flask(__name__)

smth = []

@app.route('/add_data', methods = ['POST'])
def add_data():
    global smth
    data = request.get_json()
    smth.append(data)
    smth.pop()
    smth.pop()

@app.route('/')
def index():
   return render_template('index.html', items = smth)

app.run(host ='145.93.137.61')
