import cmd
import MySQLdb
#define class User

class User():
    def __init__(self, username, password, complaints):
        self.username = username
        self.password = password
        # self.complaints = complaints[]
class Storage():
    def __init__(self):
        self.connection = MySQLdb.connect(host='localhost', user='MajiApp', password='B@Unix', db='MajiApp_db')
        self.cursor = self.connection.cursor()
        self.users = []
        self.users = self.fetch_users()
    def fetch_users(self):
        query = "SELECT * FROM User_maji"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        for user in users:
            self.users.append(User(user['username'], user['password']))
    def add_user(self, username, password):
        new_user = User(username, password)
        self.users.append(new_user)
        query = "INSERT INTO User_maji (username, password) VALUES (%s, %s)"
        self.cursor.execute(query, (username, password))
        self.connection.commit()
    def list_users(self):
        for user in self.users:
            print(f"User: {user.username} ({user.password})")
        
class  MajiAppCLI(cmd.Cmd):
    def __init__(self):
      super().__init__()
      self.prompt = ">>" 
      self.intro = "user register"
      
    def do_add_user(self, arg):
        args = arg.split()
        if len(args) != 2:
            print("Usage: add_user <username> <email>")
            return
        username, password = args
        storage.add_user(username, password)
        print(f"user {username} added")
    def do_list_users(self, arg):
        storage.list_users()
    def do_exit(self, arg):
        return True
    
if __name__ == "__main__":
    storage = Storage()
    cli = MajiAppCLI()
    cli.cmdloop() 