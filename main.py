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
from datetime import datetime

app=Flask(__name__)

def thread_function():
    addFileToDb = ManipulateData()
    moveFile = MoveFile()
    dataTr=DataTreasurer()
    processed_files = set()
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
        hour_now = datetime.now().strftime('%H')
        minute_now = datetime.now().strftime('%M')
        target_hour='04'
        target_minute='51'
        time.sleep(10)
        if hour_now == target_hour and minute_now == target_minute:
            print(dataTr.createFile())
            time.sleep(2)
            print(dataTr.send_email('mihaitg1919@gmail.com'))
            time.sleep(60)

# thread = threading.Thread(target=thread_function)
# thread.start()

@app.route('/test',methods=['POST'])
def chiulangii():
    dataTr=DataTreasurer()
    print(dataTr.createFile())
    time.sleep(2)
    print(dataTr.send_email('mihaitg1919@gmail.com'))
    return 'done'

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


@app.route('/adduser',methods=['POST'])
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