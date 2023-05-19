

def logic(arr,x,a,b,player):
    if player==1:
        mark="X"
    else:
        mark="O"
    if arr[a][0]== arr[a][1] == arr[a][2]==mark:
        return "won"
    elif arr[0][b]== arr[1][b] == arr[2][b]== mark:
        return "won"
    else:
        if x==0 or x==4  or x==8:
            if arr[0][0]== arr[1][1] == arr[2][2] == mark:
                return "won"
        elif x==2 or x==4 or x==6:
            if arr[0][2] == arr[1][1] == arr[2][0] == mark:
                return "won"
            