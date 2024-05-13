import cmd
import MySQLdb
#define class User

class User():
    def __init__(self, username, email):
        self.username = username
        self.email = email
class Storage():
    def __init__(self):
        self.connection = MySQLdb.connect(host='localhost', user='MajiApp', password='B@Unix', db='MajiApp_db')
        self.cursor = self.connection.cursor()
        self.users = []
    def add_user(self, username, email):
        new_user = User(username, email)
        self.users.append(new_user)
        query = "INSERT INTO User_maji (username, email) VALUES (%s, %s)"
        self.cursor.execute(query, (username, email))
        self.connection.commit()
    def list_users(self):
        for user in self.users:
            print(f"User: {user.username} ({user.email})")
        
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
        username, email = args
        storage.add_user(username, email)
        print(f"user {username} added")
    def do_list_users(self, arg):
        storage.list_users()
    def do_exit(self, arg):
        return True
    
if __name__ == "__main__":
    storage = Storage()
    cli = MajiAppCLI()
    cli.cmdloop() 