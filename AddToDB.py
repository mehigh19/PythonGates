import mysql.connector

class AddToDB():
    def __init__(self,nume,prenume,companie,idmanager):
        self.nume=nume
        self.prenume=prenume
        self.companie=companie
        self.idmanager=idmanager

        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='pythongates',
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.con.cursor()
        
    def registerUser(self):
        query = 'INSERT INTO `pythongates` (`nume`, `prenume`, `companie`, `idmanager`) VALUES(%s,%s,%s,%s)'
        values = (self.nume,self.prenume,self.companie,self.idmanager)
        self.cursor.execute(query, values)
        self.con.commit()
        self.cursor.close()
        self.con.close()
        print(f'Utilizatorul {self.nume} {self.prenume} a fost inregistrat cu succes')