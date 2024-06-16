import cmd
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine 
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

#Define a User class
class User(Base):
    
    __tablename__ = 'Orm_user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    email = Column(String(20))
    commplaints = relationship('Complaints', back_populates='user')
    
    '''def __init__(self, username, email, location):
        self.username = username
        self.email = email
        self.location = location
        self.complaints = []
    ''' 
    def add_complaint(self, complaint):
        self.complaints.append(complaint)

class Complaints(Base):
    
    __tablename__ = 'Orm_complaints'
    
    id = Column(Integer, primary_key=True)
    message = Column(String(200))
    user_id = Column(Integer, ForeignKey('Orm_user.id'))
    user = relationship('User', back_populates='complaints')
    
    """
    def __init__(self, username, message):
        self.username = username
        self.message = message
    """
    
class Storage:
    def __init__(self):
        
        path = 'mysql+pymysql://MajiApp:B@Unix:@localhost:orm_maji'
        self.engine = create_engine(path)
        
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        
        # self.users = []
        
    def add_user(self, username, email, location):
        new_user = User(username=username, email=email, location=location)
        self.session.add(new_user)
        self.session.commit()
        # self.users.append(new_user)
        
    def add_complaints(self, username, message):
        user = self.session.query(User).filter_by(username=username).first()
        if user:
            complaint = Complaints(message=message, user=user)
            self.session.add(complaint)
            self.session.commit()       
       
        '''
        for user in self.users:
            if user.username == username:
                complaint = Complaints(message)
                user.add_complaints(complaint)
        '''
                
                
    def list_users(self):
        for user in self.session.query(User).all():
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