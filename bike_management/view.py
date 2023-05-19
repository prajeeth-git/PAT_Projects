from user import user
from manager import Manager
print("Choose BIke Model:")
bike=user()
bikemodels=list(bike.displaymodels())
for i in range(len(bikemodels)):
    print(i+1,bikemodels[i])
choice=int(input("Enter Your Choice:"))
details=bike.bikedetails(bikemodels[choice-1])
buyoption=input("Want To Buy Y/N:  ")
m=Manager()

if buyoption=="Y":
    m.selling(bikemodels[choice-1])
else:
    print("Thanks for Viewing")
x=input("See other bikes Y/N:")
while(x=="Y"):
    print("Choose BIke Model:")
    bike=user()
    bikemodels=list(bike.displaymodels())
    for i in range(len(bikemodels)):
        print(i+1,bikemodels[i])
    choice=int(input("Enter Your Choice:"))
    details=bike.bikedetails(bikemodels[choice-1])
    buyoption=input("Want To Buy Y/N:  ")
    m=Manager()

    if buyoption=="Y":
        m.selling(bikemodels[choice-1])
    else:
        print("Thanks for Viewing")
    x=input("See other bikes Y/N:")

