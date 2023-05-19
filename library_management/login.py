class login :
    def __init__(self):
        self.details={}
        self.username=input("Enter user name:")
        self.password=input("Enter password:")

    def auth(self):
        if self.username in self.details:
            if self.password == self.details[self.username]:
                return "Successfully logged in "
            else:
                return "Inccorect password"
        else:
            return "Username not found"
    
    def createuser(self):
        newusername=input("Enter user name:")
        newpassword=input("Enter password:")
        self.details[newusername]=newpassword