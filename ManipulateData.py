from Gate1 import *
from AddToAccess import *

readTxt=Gate1

class ManipulateData():

     def manipulateDataTxt(self):
        dateTxt=readTxt.readFile(self).split('\n')
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
        
        return 'Data from Poarta1.txt inserted succesfully'

        # list=[]
        # for element in range(len(dateTxt)-1):
        #        list.append(id_list[element])
        #        list.append(data_list[element])
        #        list.append(sens_list[element])

        # return(list)

verificaTxt=ManipulateData()
print(verificaTxt.manipulateDataTxt())