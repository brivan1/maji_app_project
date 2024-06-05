import cmd
import MySQLdb

#Define a User class
class User:
    def __init__(self, username, email, location):
        self.username = username
        self.email = email
        self.location = location
        self.complaints = []
        
    def add_complaint(self, complaint):
        self.complaints.append(complaint)

class Complaints:
    def __init__(self, username, message):
        self.username = username
        self.message = message

class Storage:
    def __init__(self):
        self.connection = MySQLdb.connect(host='localhost', user= 'MajiApp', password='B@Unix', db='MajiApp_db')
        self.cursor = self.connection.cursor()
        self.users = []
        
    def add_user(self, username, email, location):
        new_user = User(username, email, location)
        self.users.append(new_user)
        query = "INSERT INTO User_maji(username, email, location) VALUES (%s, %s, %s)"
        self.cursor.execute(query(username, email, location))
        self.connection.commit()
        
    def add_complaints(self, username, message):
        for user in self.users:
            if user.username == username:
                complaint = Complaints(message)
                user.add_complaints(complaint)
                
                query = "SELECT Field FROM User_maji WHERE username = %s"
                self.cursor.execute(query, (username))
                username = self.cursor.fetchone()[0]
                
                query = "INSERT INTO Complaints(message, username) VALUES (%s, %s)"
                self.cursor.execute(query, (message, username))
                self.connection.commit()
    
    def fetch_user(self):
        users = []
        
        query = """
        SELECT User_maji.username, Complaints.message
        FROM User_maji
        LEFT JOIN Complaints ON User_maji.username = Complaints.username
        """
        self.cursor.execute(query)
        curr_user = None
        for row in self.cursor.fetchall():
            username, message = row
            if not curr_user or curr_user.username != username:
                curr_user = User(username)
                users.append(curr_user)
            if message:
                curr_user.add_complaints(Complaints(message))
            print(row)
        return users
           
    
    def list_users(self):
        for user in self.users:
            print(f"User:{user.username}")
            for complaint in user.complaints:
                print(f"Complaints: {complaint.message}")
              
class UserMajiAppCLI(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "water rationing >>"
        self.intro = "MajiApp Tool"
        
    def do_add_user(self,arg):
        args = arg.split()
        if len(args) != 2:
            print("Use: add_user <username> <email> <location>")
            return 
        username, email, location = args
        storage.add_user(username, email, location)
        
    def do_add_complaints(self, arg):
        args = arg.split()
        if len(args) !=2:
            print("use: add_complaints <username> <message>")
            return
        username, message = args
        storage.add_complaints(username, message)
        
    def do_list_users(self, arg):
        storage.list_users()
        
    def do_quit(self, arg):
        print("exiting")
        return True
    
if __name__ == "__main__":
    storage = Storage()
    cli = UserMajiAppCLI()
    cli.cmdloop