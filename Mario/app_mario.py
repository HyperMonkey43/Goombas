from flask import Flask, render_template, request
import json
app = Flask(__name__)

smth = []

@app.route('/add_data', methods = ['POST'])
def add_data():
    global smth
    data = request.get_json()
<<<<<<< HEAD
    smth.append(data)
=======
    # ceva  = json.loads(data)
    print(data)
    # print(ceva[0]['name'])
>>>>>>> 675894ee78f8eb98843c82167f8decda3e12fed7
    return {}
    
@app.route('/')
def index():
   return render_template('index.html', items = smth)

app.run(host = '145.93.137.61')
