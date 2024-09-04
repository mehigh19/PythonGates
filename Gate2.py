from flask import jsonify
import json

class Gate2():
    def readFile(self):
        readPath = r'HW\intrari\Poarta2.csv'
        with open(readPath, 'r') as readFile:
            readContent = readFile.read()
            return readContent