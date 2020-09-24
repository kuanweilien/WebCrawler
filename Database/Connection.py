import mysql.connector as sql
from mysql.connector  import Error
import configparser as cp
import configparser as cp
import os

class Con:
    def __init__(self):
        cnf=cp.ConfigParser()
        cnf.read(os.path.realpath( os.path.join(os.path.dirname(os.path.realpath(__file__)),os.path.pardir,"config.ini")),"UTF-8")
        self.conStr = dict(
            host=cnf.get("db","HOST"),
            port=cnf.get("db","PORT"),
            database=cnf.get("db","DBNAME"),
            user=cnf.get("db","USER"),
            password=cnf.get("db","PWD"))

        self.cmd = sql.connect(
            host=self.conStr['host'],
            port=self.conStr['port'],
            database=self.conStr['database'],
            user=self.conStr['user'],
            password=self.conStr['password']
        )
    def Close(self):
        self.cmd.close()

