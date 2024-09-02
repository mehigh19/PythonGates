from Gate1 import Gate1
from Gate2 import Gate2
from AddToDB import AddToDB
from MoveFile import MoveFile
from AddToAccess import AddToAccess
from ManipulateData import ManipulateData
from DataTreasurer import DataTreasurer
from flask import Flask,request, jsonify
import threading
import time
import json
import time

app=Flask(__name__)

def thread_function():
    addFileToDb = ManipulateData()
    moveFile = MoveFile()
    dataTr=DataTreasurer()
    processed_files = set()
    email_sent = False
    while True:
        txt_files = moveFile.get_txt_files()
        for txt_file in txt_files:
            if txt_file not in processed_files:
                addFileToDb.manipulateDataTxt(txt_file)
                moveFile.check_txt(txt_file)
                processed_files.add(txt_file)
        time.sleep(0.5)
        csv_files = moveFile.get_csv_files()
        for csv_file in csv_files:
            if csv_file not in processed_files:
                addFileToDb.manipulateDataCsv(csv_file)
                moveFile.check_csv(csv_file)
                processed_files.add(csv_file)
        time.sleep(0.5)
        if not email_sent:
                    target_hour = 15
                    target_minute = 54
                    dataTr.wait_until(target_hour, target_minute)
                    email_sent = True     
        time.sleep(10)
thread = threading.Thread(target=thread_function)
thread.start()

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
    print('Json data inserted succesfully')
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