def checker(system):
    flag=0
    if system[5]==1 and system[6]==1:
        flag=1
    if system[6]==1 and system[7]==1:
        flag=1
    return flag

def generator(system):
    if system[1]==system[0]==system[2]==1:
        system[1]=0
        system[6]=1
        lm=1
    elif system[0]==1:
        system[0]=0
        system[5]=1
        lm=0
    elif system[2]==1:
        system[2]=0
        system[7]=1
        lm=2
    else:
        system[1]=0
        system[6]=1
        lm=1
    system[3]=0
    system[4]=1
    if system[0]==system[1]==system[2]==system[3]==0:
        return
    printer(system)
    if checker(system)==1:
        for i in range(5,8):
            if system[i]==1 and not i==lm+5:
                system[i]=0
                system[i-5]=1
                system[3]=1
                system[4]=0
                return
    else :
        system[3]=1
        system[4]=0
    return

def printer(system):
    print("\n\nAfter next move\n\n")
    print("Island 1 :")
    if system[0]:
        print("Tiger")
    if system[1]:
        print("Goat")
    if system[2]:
        print("Grass")
    if system[3]:
        print("Man")
    print("\nIsland 2 :")
    if system[5]:
        print("Tiger")
    if system[6]:
        print("Goat")
    if system[7]:
        print("Grass")
    if system[4]:
        print("Man")
    return
system={}
lm=10
k=1
for i in range(8):
    system[i]=0
system[0]=1  #tiger
system[1]=1  #goat
system[2]=1  #grass
system[3]=1  #man
while system[0]==1 or system[1]==1 or system[2]==1:
    generator(system)
    printer(system)
