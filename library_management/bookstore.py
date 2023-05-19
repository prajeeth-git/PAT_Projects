class bookstore:
    def __init__(self):
        self.books={
            'All-in On AI ':{
                'Price':'₹1,880',
                'Language':' English',
                'author':' Thomas H. Davenport',
                'No of Pages':'256',
                'Publisher':' Harvard Business Review Press',
                'Publisher Date':' 06 Dec 2022',
                'ISBN-13': '9781647824693'
            },

            'It Ends with Us':{
                'Price':'₹274',
                'Language':' English',
                'author':'  Colleen Hoover ',
                'No of Pages':'384',
                'Publisher':'  Atria Books',
                'Publisher Date':' 02 Aug 2016',
                'ISBN-13': '9781501110368'
            },

            'Your Time Will Come':{
                'Price':'₹119',
                'Language':' English',
                'author':' Fingerprint! Publishing',
                'No of Pages':'248',
                'Publisher':'  Atria Books',
                'Publisher Date':'08 Apr 2022',
                'ISBN-13': '9789354400704'
            },
            "Harry Potter and the Philosopher's Stone":{
                'Price':'₹374',
                'Language':' English',
                'author':'J. K. Rowling',
                'No of Pages': '352',
                'Publisher':' Bloomsbury Publishing PLC',
                'Publisher Date':'01 Sep 2014',
                'ISBN-13': '9781408855652'
            },
            "Harry Potter and the Chamber of Secrets":{
                'Price':'₹384',
                'Language':' English',
                'author':'J. K. Rowling',
                'No of Pages': '384',
                'Publisher':' Bloomsbury Publishing PLC',
                'Publisher Date':'01 Sep 2014',
                'ISBN-13': '9781408855669'
            }        
        }

    def viewbooks(self):
        return self.books

    def rent(self,bookname,obj):
        obj.count[bookname]-=1
        return 'Your book is successfully rented'

    def bookdetails(self,bookname):
        return self.books[bookname]