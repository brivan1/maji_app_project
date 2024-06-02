import cmd


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
        
    