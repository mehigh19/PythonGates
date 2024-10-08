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
import os

def thread_function():
    addFileToDb = ManipulateData()
    checkFolder=ManipulateData()
    checkFolder.checkFolders()
    time.sleep(1)
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
        target_hour='17'
        target_minute='48'
        time.sleep(10)
        if hour_now == target_hour and minute_now == target_minute:
            print(dataTr.send_email('mihaitg1919@gmail.com'))
            time.sleep(60)

app=Flask(__name__)

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
        json_path=r'HW\PythonGates\backup_intrari\Poarta3.json'
        if os.path.isfile(json_path):
            mode='a'
        else:
            mode='w'
        with open(r'HW\PythonGates\backup_intrari\Poarta3.json',mode) as jsonFile:
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

def run_flask_server():
    app.run(host="0.0.0.0", port=4000, debug=True, threaded=True, use_reloader=False)

if __name__ == '__main__':
    thread = threading.Thread(target=thread_function)
    thread.start()
    thread2 = threading.Thread(target=run_flask_server)
    thread2.start()
    thread.join()
    thread2.join()