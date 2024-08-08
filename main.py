from Gate1 import Gate1
from Gate2 import Gate2
from AddToDB import AddToDB
from flask import Flask,request, jsonify
import json

poarta1=Gate1()
poarta1.saveFile()

app=Flask(__name__)

@app.route('/test')
def addJson():
    poarta2 = Gate2()
    file_content = poarta2.readFile()
    lines = file_content.strip().splitlines()
    json_content = {"file_content": lines}
    save_path = r'HW\PythonGates\Poarta2.json'
    with open(save_path, 'w') as json_file:
        json.dump(json_content, json_file, indent=4)
    return jsonify(json_content)

@app.route('/test',methods=['POST'])
def postToDB():
    body = request.get_json()
    if body is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    nume = body.get('nume')
    prenume = body.get('prenume')
    companie = body.get('companie')
    idmanager = body.get('idmanager')
        
    ceoUser=AddToDB(nume,prenume,companie,idmanager)
    ceoUser.registerUser()
    return jsonify(body)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000,debug=True)