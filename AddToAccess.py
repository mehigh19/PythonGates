import mysql.connector

class AddToAccess():
    def __init__(self,data,sens,idPersoana,idPoarta):
        self.data=data
        self.sens=sens
        self.idPersoana=idPersoana
        self.idPoarta=idPoarta

        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='pythongates',
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.con.cursor()
        
    def addDataAccess(self):
        query = 'INSERT INTO `access` (`data`, `sens`, `idPersoana`, `idPoarta`) VALUES(%s,%s,%s,%s)'
        values = (self.data,self.sens,self.idPersoana,self.idPoarta)
        self.cursor.execute(query, values)
        self.con.commit()
        self.cursor.close()
        self.con.close()