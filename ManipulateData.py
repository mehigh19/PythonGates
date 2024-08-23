from Gate1 import Gate1
from AddToAccess import AddToAccess

class ManipulateData:
    def __init__(self):
        self.gate1 = Gate1()

    def manipulateDataTxt(self, txt_file):
        try:
            df = self.gate1.readFile()
            for element in range(len(df)):
                data = df.iloc[element, 1]
                sens = df.iloc[element, 2]
                idPersoana = int(df.iloc[element, 0])
                obj = AddToAccess(data, sens, idPersoana, 1)
                obj.addDataAccess()
            print(f'Data from {txt_file} inserted successfully')
        except FileNotFoundError:
            print(f"That file {txt_file} doesn't exist")

    def manipulateDataCsv(self, csv_file):
        try:
            df = self.gate1.readFileCsv()
            for element in range(len(df)):
                if element != 0:
                    data = df.iloc[element, 1]
                    sens = df.iloc[element, 2]
                    idPersoana = int(df.iloc[element, 0])
                    obj = AddToAccess(data, sens, idPersoana, 2)
                    obj.addDataAccess()
            print(f'Data from {csv_file} inserted successfully')
        except FileNotFoundError:
            print(f"That file {csv_file} doesn't exist")
