import pandas as pd

class Gate2():
    def readFile(self):
        readPath = r'HW\PythonGates\intrari\Poarta2.csv'
        df = pd.read_csv(readPath, delimiter=',', header=None)
        return df