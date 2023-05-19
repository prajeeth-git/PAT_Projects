class manager:
    def __init__(self):
        self.count={
            'All-in On AI ':5,
            'It Ends with Us':2,
            'Your Time Will Come':3,
            "Harry Potter and the Philosopher's Stone":1,
            "Harry Potter and the Chamber of Secrets":3,

        }

    def addbook(self,obj):
        title=input("enter book title: ")
        price=input("enter book price: ")
        Language=input("enter book Language: ")
        author=input("enter book author: ")
        No_of_Pages=input("enter book No of Pages: ")
        Publisher=input("enter book Publisher: ")
        Publisher_Date=input("enter book Publisher Date: ")
        ISBN_13=input("enter book ISBN-13: ")
        obj.books[title]={
                'Price':price,
                'Language':Language,
                'author':author,
                'No of Pages':No_of_Pages,
                'Publisher':Publisher,
                'Publisher Date':Publisher_Date,
                'ISBN-13': ISBN_13
        }

    def removebook(self,obj,bookname):
        if bookname in obj.books:
            del obj.books[bookname]
            print("Removed successfully")
        else:
            print("No book with given name found")


    def acceptpayment(self):
        pass

    def updatedetails(self,bookname,obj):
        arr=list(map(str,input("Details you want to update(separate by space):")))
        for i in arr:
            x=input("enter book "+i)
            obj.book[bookname][i]=x
        
        
    
    def generateinvoice(self):
        pass
