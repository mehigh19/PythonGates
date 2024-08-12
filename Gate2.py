from flask import jsonify
import json

class Gate2():
    def readFile(self):
        readPath = r'HW\intrari\Poarta2.csv'
        with open(readPath, 'r') as readFile:
            readContent = readFile.read()
            return readContent

    def saveFile(self):
        file_content = self.readFile()
        lines = file_content.strip().splitlines()
        json_content = {"file_content": lines}
        save_path = r'HW\PythonGates\Poarta2.json'
        with open(save_path, 'w') as json_file:
            json.dump(json_content, json_file, indent=4)
        return jsonify(json_content)
