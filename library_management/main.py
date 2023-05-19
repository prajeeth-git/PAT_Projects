from manager import manager
from bookstore import bookstore
from login import login
0
log1=login()
out1=log1.auth()
if out1=="Successfully logged in ":
    store1=bookstore()
    nbooks=store1.viewbooks()
    print("Choose book title to view full details")
    for i in range(len(nbooks)):
        pass
elif out1=="Inccorect password":
    pass
elif out1=="Username not found":
    pass