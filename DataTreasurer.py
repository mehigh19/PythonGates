import mysql.connector
from datetime import datetime, timedelta
from collections import defaultdict
import smtplib, ssl
from passwords import password,passwordDb
import csv
import time

class DataTreasurer():
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password=passwordDb,
            database='pythongates',
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.con.cursor()

    def __fetch_data(self):
        query = "SELECT * FROM pythongates.access;"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        self.con.commit()
        return results

    def __clearData(self):
        inNout=[]
        checkedInNout=[]
        yesterday=''
        data=self.__fetch_data()
        for row in range(len(data)):
            if yesterday=='':
                yesterday=(list(data[row])[0].split('-')[2].split('T')[0])
            elif (int(yesterday)-(int(list(data[row])[0].split('-')[2].split('T')[0]))) > 15:
                inNout.append(list(self.fetch_data()[row]))
            else:
                if yesterday<=(list(data[row])[0].split('-')[2].split('T')[0]):
                    yesterday=(list(data[row])[0].split('-')[2].split('T')[0])
                    inNout.append(list(data[row]))
                    if (inNout[0][0].split('-')[2].split('T')[0]) < (data[row][0].split('-')[2].split('T')[0]):
                        inNout.pop(0)
        yesterday=''
        for check in inNout:
            for row in range(len(inNout)):
                if yesterday == '':
                        yesterday = check[0].split('-')[0][2].split('T')[0]
                elif (check[0].split('-')[2].split('T')[0]) < yesterday:
                    checkedInNout.append(check)
        if len(checkedInNout) == 0:
            return inNout
        else:
            inNout=list(set(checkedInNout))
            return inNout
        
    def __createDict(self):
        db_dict=[]
        data=self.__clearData()
        for row in range(len(data)):
            entry = {
                "data":data[row][0],
                "sens":data[row][1],
                "idPersoana":data[row][2],
                "idPoarta":data[row][3]
            }
            db_dict.append(entry)
        return db_dict

    def __clockingDict(self):
        content=self.__createDict()
        grouped_data={}
        dict_clocking=[]
        for entry in content:
            person_id=entry['idPersoana']
            if person_id not in grouped_data:
                grouped_data[person_id] = []
            grouped_data[person_id].append(entry)
        for idPersoana in (grouped_data):
            for element in range(len(grouped_data[idPersoana])):
                oraOut=(grouped_data[idPersoana][element]["data"]).split('T')[1].split('.')[0]
                oraIn=(grouped_data[idPersoana][element-1]["data"]).split('T')[1].split('.')[0]
                sens=(grouped_data[idPersoana][element]["sens"])
                if sens == "out" or sens == "out;" or sens == "out; ":
                    oreLucrate=int(oraOut.split(":")[0])-int(oraIn.split(":")[0])
                    minuteLucrate=int(oraOut.split(":")[1])-int(oraIn.split(":")[1])
                    secundeLucrate=int(oraOut.split(":")[2])-int(oraIn.split(":")[2])
                    entry = {
                            "id":idPersoana,
                            "ore":oreLucrate,
                            "minute":minuteLucrate,
                            "secunde":secundeLucrate
                            }
                    dict_clocking.append(entry)
        return dict_clocking
    
    def __getById(self,given_id):
        cursor = self.con.cursor()
        cursor.execute("SELECT nume, prenume FROM pythongates.pythongates WHERE id = %s", (given_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            name=result[0]+" "+result[1]
            return name
        else:
            return None
        
    def __getIdAndTime(self):
        oreLucrate=[]
        total_time = defaultdict(lambda: {'ore': 0, 'minute': 0, 'secunde': 0})
        for entry in self.__clockingDict():
            id = entry['id']
            ore = entry['ore']
            minute = entry['minute']
            secunde = entry['secunde']
            if secunde < 0:
                secunde += 60
                minute -= 1
            if minute < 0:
                minute += 60
                ore -= 1
            total_time[id]['ore'] += ore
            total_time[id]['minute'] += minute
            total_time[id]['secunde'] += secunde
            if total_time[id]['secunde'] >= 60:
                total_time[id]['minute'] += total_time[id]['secunde'] // 60
                total_time[id]['secunde'] = total_time[id]['secunde'] % 60
            if total_time[id]['minute'] >= 60:
                total_time[id]['ore'] += total_time[id]['minute'] // 60
                total_time[id]['minute'] = total_time[id]['minute'] % 60
        result = dict(total_time)
        final_dict=[]
        for id,time in result.items():
            oreLucrate.append(f'{time['ore']}h{time['minute']}min')
            oreLucratee=str(time['ore']) + "h" + str(time['minute']) + "min"
            entry={
                "nume":self.__getById(id),
                "oreLucrate": oreLucratee
            }
            final_dict.append(entry)
        return final_dict

    def createFile(self):
        data=self.__getIdAndTime()
        with open(r'HW\PythonGates\backup_intrari\chiulangii.txt','w') as file:
            for element in range(len(data)):
                entry=((data[element]["nume"]) + " " + (data[element]["oreLucrate"])+"\n")
                file.write(entry)
        with open(r'HW\PythonGates\backup_intrari\chiulangii.csv','w',newline='') as file:
            writer = csv.writer(file)
            header=['nume','oreLucrate']
            writer.writerow(header)
            for element in data:
                row = [element["nume"], element["oreLucrate"]]
                writer.writerow(row)
        return 'chiulangii.txt and chiulangii.csv files created succesfully into backup_intrari'

    def send_email(self,receiver_email):
        warning=''
        data=self.__clockingDict()
        for element in range(len(data)):
            if data[element]['ore'] < 8:
                message=(f'Id {data[element]['id']} worked less then 8 hours')
                warning=warning+message+"\n"
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "mihaitg19@gmail.com"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, warning)
        return 'Email sent !'

    def wait_until(self, target_hour, target_minute):
        now = datetime.now()
        target_time = datetime(now.year, now.month, now.day, target_hour, target_minute)
        if now > target_time:
            target_time += timedelta(days=1)
        while datetime.now() < target_time:
            time.sleep(10)
        print(self.createFile())
        print(self.send_email('mihaitg1919@gmail.com'))