import math
pages=input("Enter pages    :")
sp=pages.split(",")
pages=[]
for i in range(len(sp)):
    if not '-' in sp[i]:
        pages.append(int(sp[i]))
        if int(sp[i])%2==0:
            pages.append(int(sp[i])-1)
        else:
            pages.append(int(sp[i])+1)
    else:
        g=sp[i].split("-")
        for j in range(int(g[0]),int(g[1])+1):
            pages.append(j)
            if j%2==0:
                pages.append(j-1)
            else:
                pages.append(j+1)
for i in range(1,26):
     if not i in pages:
         print(i)
