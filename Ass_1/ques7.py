low=input("Enter the lower limit    :")
high=input("Enter the upper limit   :")
high=int(high)
low=int(low)
for num in range(low,high+1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num,"is an Armstrong number")
