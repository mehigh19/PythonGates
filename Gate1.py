from Gates import Gates
import pandas as pd

class Gate1(Gates):
    def readFile(self):
        readPath = r'HW\PythonGates\intrari\Poarta1.txt'
        df = pd.read_csv(readPath, delimiter=',', header=None)
        return df