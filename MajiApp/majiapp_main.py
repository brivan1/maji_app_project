import cmd
import MySQLdb
#define class User

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
class Storage():
    def __init__(self):
        self.connection = MySQLdb.connect(host='localhost', user='MajiApp', password='B@Unix', db='MajiApp_db')
        self.cursor = self.connection.cursor()
        self.users = []
    def add_user(self, username, password):
        new_user = User(username, password)
        self.users.append(new_user)
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
        if len(args) == 2:
            username = args[0]
            password = args[1]
            storage = Storage()
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