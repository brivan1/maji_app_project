import cmd
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship

#Define a User class
class User:
    
    __tablename__ = 'Orm_maji'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(100))
    
    
    
    '''def __init__(self, username, email, location):
        self.username = username
        self.email = email
        self.location = location
        self.complaints = []
    ''' 
    def add_complaint(self, complaint):
        self.complaints.append(complaint)

class Complaints:
    
    __tablename__ = 'Complaints'
    
    id = Column(Integer, primary_key=True)
    
    """
    def __init__(self, username, message):
        self.username = username
        self.message = message
    """
    
class Storage:
    def __init__(self):
        self.users = []
        
    def add_user(self, username, email, location):
        new_user = User(username, email, location)
        self.users.append(new_user)
        
    def add_complaints(self, username, message):
        for user in self.users:
            if user.username == username:
                complaint = Complaints(message)
                user.add_complaints(complaint)
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