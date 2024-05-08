import MySQLdb

#define class User

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
class Storage():
    def __init__(self):
        self.connection = MySQLdb.connect(host='localhost', user='bunix', password='B@Unix', db='MajiApp_db')
        self.cursor = self.connection.cursor()
        self.Users = []
    def add_user(self, username, password):
        new_user = User(username, password)
        self.User.append(new_user)
        query = "INSERT INTO User_main (username, password) VALUES (%s, %s) "
        self.cursor.execute(query, (username, password))
        self.connection.commit()
