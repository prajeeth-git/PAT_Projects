from user import user

class Manager:
    def __init__(self):
        self.count={
            'R15M ':6,
            'R15 V4 ':5,
            'R15S ':8,
            'MT-15 Ver 2.0':3,
            'FZ 25':7,
        }
    def avaliablestock(self):
        for i in self.count:
            print("model:",self.count[i])
    def selling(self,name):
        if self.count[name]==0:
            print("Out oF Stock")
        else:
            print("Thanks For Purchasing")
            self.count[name]-=1
        