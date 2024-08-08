from Gates import Gates

class Gate1(Gates):
    def readFile(self):
        readPath = r'HW\Poarta1.txt'
        with open(readPath, 'r') as readFile:
            readContent = readFile.read()
            return readContent

    def saveFile(self):
        savePath=r'HW\PythonGates\Poarta1.txt'
        with open(savePath,'w') as saveFile:
            saveFile.write(self.readFile())
            print('Fisier salvat')