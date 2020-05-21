i=0
k=0
while k in range(10):
    sum2=1
    sum=1
    j=2
    m=2
    while j*j<i and j<i:
        if i%j==0:
            sum+=j
            sum+=int(i/j)
        j+=1
    if sum%2==i%2 and sum>i:
        while m*m<sum:
            if sum%m==0:
                sum2+=m
                sum2+=int(sum/m)
            m+=1
    if i==sum2 and not sum==sum2:
        print(sum,"and",sum2)
        k+=1
    i+=1
