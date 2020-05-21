i=1
k=0
while k in range(10):
    numerator=0
    denominator=0
    for j in range(1,i+1):
        if i%j==0:
            rec=i/j
            denominator+=rec
            numerator+=1
    # if i==672 or i==1638 or i==2970:
    #     print("these two",i)
    #     print(numerator)
    #     print(denominator)
    mean=numerator/denominator
    mean*=i
    if mean.is_integer()==1:
        print(i)
        k+=1
    i+=1
