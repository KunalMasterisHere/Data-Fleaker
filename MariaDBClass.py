# import pymysql
from DatabaseClass import DatabaseClass
from MySQLClass import MySQLClass, MySQLEngineTypes

# Inherit from MySQLClass
class MariaDBClass(MySQLClass):
    mariaDBInstanceCount = 0

    def __init__(self,
                 host: str,
                 userName: str,
                 passWord: str,
                 auth_plugin: str = 'mysql_native_password'):
        DatabaseClass.__init__(self, "Maria Database")
        MariaDBClass.mariaDBInstanceCount += 1
        self.mariaInstanceID = DatabaseClass.instanceSeedID
        self.host = host
        self.userName = userName
        self.passWord = passWord
        self.auth_plugin = auth_plugin

    def getMariaDBClassInstanceCount(self):
        return MariaDBClass.mariaDBInstanceCount

    def getMariaDBClassInstanceID(self):
        return self.mariaInstanceID

    def __del__(self):
        MariaDBClass.mariaDBInstanceCount -= 1
        DatabaseClass.__del__(self, self.description, self.mariaInstanceID)
