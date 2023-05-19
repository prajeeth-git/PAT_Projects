from logic import logic
from view import output

name1=input("enter player 1 name(X):")
name2=input("enter player 2 name(O):")
visited=[0,1,2,3,4,5,6,7,8]
arr=[[False,False,False],[False,False,False],[False,False,False]]
points={0:[0,0],1:[0,1],2:[0,2],3:[1,0],4:[1,1],5:[1,2],6:[2,0],7:[2,1],8:[2,2]}
display=arr=[[False,False,False],[False,False,False],[False,False,False]]
for i in range(9):
    if i%3==0:
        print('\n',i,end="\t")
    else:
        print(i,end="\t")
print('\n')
while(len(visited)!=0):
    boxnumber1=int(input("Choose box number player1:"))
    while(boxnumber1 not in visited):
            print("box already choosen! please choose other box")
            boxnumber1=int(input("Choose box number player1:"))

    visited.remove(boxnumber1)
    a,b=points[boxnumber1][0],points[boxnumber1][1]
    arr[a][b]=True
    display[a][b]='X'
    output(display)
    obj1=logic(arr, boxnumber1,a,b,1)
    if obj1=="won":
        print(f"Player {name1} won")
        break
    boxnumber2=int(input("Choose box number player2:"))
    while(boxnumber2 not in visited):
            print("box already choosen! please choose other box")
            boxnumber2=int(input("Choose box number player2:"))
    visited.remove(boxnumber2)
    a,b=points[boxnumber2][0],points[boxnumber2][1]
    arr[a][b]=True
    display[a][b]='O'
    output(display)
    obj2=logic(arr, boxnumber2,a,b,2)
    if obj2=="won":
        print(f"Player {name2} won")
        break
else:
    pritn("draw")