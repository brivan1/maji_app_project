import MySQLdb

#define class User

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
class Storage():
    def __init__(self):
        self.connection = MySQLdb.connect(host='localhost', usr='bunix', password='B@Unix', db='MajiApp_db')
        self.cursor = self.connection.cursor()
        self.Users = []
    def add_user(self, username, password):
        new_user = User(username, password)
        self.Users.append(new_user)
        query = "INSERT INTO Users (username, password) VALUES (%s, %s) "
        self.cursor.execute(query, (username, password))
        self.connection.commit()
