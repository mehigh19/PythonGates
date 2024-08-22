from Gate1 import *
from AddToAccess import *

readTheFile=Gate1

class ManipulateData():

    def manipulateDataTxt(self):
        try:
            dateTxt=readTheFile.readFile(self).split('\n')
            data_list=[]
            id_list=[]
            sens_list=[]

            for time in range(len(dateTxt)-1):
                data=""
                for character in range(2,26): 
                    data+=dateTxt[time][character]
                data_list.append(data)
            
            for way in range(len(dateTxt)-1):      
                sens=''
                sens+=dateTxt[way][27]
                sens+=dateTxt[way][28]
                if (dateTxt[way][29]) ==';':
                    sens_list.append(sens)
                else:
                    sens+=dateTxt[way][29]
                    sens_list.append(sens)
            for id in range(len(dateTxt)-1): 
                id_list.append(dateTxt[id][0])

            for element in range(len(dateTxt)-1):
                object=AddToAccess(data_list[element],sens_list[element],id_list[element],1)
                object.addDataAccess()
            
            print('Data from Poarta1.txt inserted succesfully')
        except FileNotFoundError:
             print("That txt file doesn't exist")

    def manipulateDataCsv(self):
        try:
            dateCsv=readTheFile.readFileCsv(self).split('\n')
            data_list=[]
            id_list=[]
            sens_list=[]

            for time in range(len(dateCsv)-1):
                if not time ==0:
                    data=""
                    for character in range(2,26): 
                            data+=dateCsv[time][character]
                    data_list.append(data)
                
            for way in range(len(dateCsv)-1):
                if not way ==0:
                    sens=''
                    sens+=dateCsv[way][27]
                    sens+=dateCsv[way][28]
                    try:
                            if (dateCsv[way][29]) == 't':
                                sens+=dateCsv[way][29]
                    except IndexError as e:
                            pass
                    sens_list.append(sens)
            for id in range(len(dateCsv)-1):
                if not id == 0: 
                    id_list.append(dateCsv[id][0])

            for element in range(len(dateCsv)-2):
                object=AddToAccess(data_list[element],sens_list[element],id_list[element],2)
                object.addDataAccess()

            print('Data from Poarta2.csv inserted succesfully')
        except FileNotFoundError:
             print("That csv file doesn't exist")