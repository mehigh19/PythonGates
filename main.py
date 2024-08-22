from Gate1 import Gate1
from Gate2 import Gate2
from AddToDB import AddToDB
from MoveFile import MoveFile
from AddToAccess import AddToAccess
from flask import Flask,request, jsonify
import threading
import time
import json

app=Flask(__name__)

poarta1=Gate1()
poarta2=Gate1()
poarta1.saveFile()
poarta2.saveFileCsv()

def thread_function():
    while True:
        moveFile=MoveFile()
        MoveFile.check_txt()
        MoveFile.check_csv()
        time.sleep(20)

thread = threading.Thread(target=thread_function)
# thread.start()      

@app.route('/access',methods=['POST'])
def addFile():
    body = request.get_json()
    if body is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    data = body.get('data')
    sens = body.get('sens')
    idPersoana = body.get('idPersoana')
    idPoarta = body.get('idPoarta')

    addData=AddToAccess(data,sens,idPersoana,idPoarta)
    addData.addDataAccess()
    print('Data inserted succesfully')
    with open(r'HW\PythonGates\backup_intrari\Poarta3.json','w') as jsonFile:
        json.dump(body,jsonFile)
    return jsonify(body)


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