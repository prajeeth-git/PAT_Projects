def output(display):
    for i in range(3):
        for j in range(3):
            if display[i][j]:
                print(display[i][j],"|\t",end="")
            else:
                print('-',"|\t",end="")
        print("\n--------------------------")
