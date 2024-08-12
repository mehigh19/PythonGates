from Gate1 import Gate1
from Gate2 import Gate2
from AddToDB import AddToDB
from flask import Flask,request, jsonify
import os

poarta1=Gate1()
poarta1.saveFile()

app=Flask(__name__)

@app.route('/test')
def addFile():
    poarta2=Gate2()
    return poarta2.saveFile()

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