

class Gate2():
    def readFile(self):
        readPath = r'HW\Poarta1.txt'
        with open(readPath, 'r') as readFile:
            readContent = readFile.read()
            return readContent

    def saveFile(self):
        pass

    def postToDB(self):
        pass