import mysql.connector as sql
from mysql.connector  import Error
from Database.Type import SqlType as st

class DML:
    def __init__(self,con,sqlType,sqlStr,para):
        self.sqlType = sqlType
        self.sqlStr = sqlStr
        self.para = para
        self.c = con

    def execute(self):        
        self.cursor = self.c.cmd.cursor()

        if self.para == "" :
            self.cursor.execute(self.sqlStr )
        else:
            self.cursor.execute(self.sqlStr ,self.para )

        if self.sqlType == st.INSERT or self.sqlType == st.UPDATE or self.sqlType == st.DELETE :
            self.c.cmd.commit()

        return (self.sqlType.value,' Success')

    def dispose(self):
        self.cursor.close()
        self.c.Close()