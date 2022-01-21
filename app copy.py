from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': u'raju',
        'no.': u'1234567890', 
        'done': False
    },
    {
        'id': 2,
        'name': u'Aashman',
        'no.': u'0987654321', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'no.': request.json.get('no.', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)