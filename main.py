from Gate1 import Gate1
from Gate2 import Gate2
from AddToDB import AddToDB
from MoveFile import MoveFile
from flask import Flask,request, jsonify
import threading
import time

app=Flask(__name__)

poarta1=Gate1()
poarta1.saveFile()
poarta2=Gate1()
poarta2.saveFileCsv()

def thread_function():
    while True:
        moveFile=MoveFile()
        MoveFile.check_txt()
        time.sleep(4)
        MoveFile.check_csv()
        time.sleep(15)

thread = threading.Thread(target=thread_function)
# thread.start()      

@app.route('/test')
def addFile():
    pass

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