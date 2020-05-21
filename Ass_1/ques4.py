import random
answer= random.randint(0,99999)
boo=1
while boo:
    g=int(input("Enter your guess   :"))
    if g<answer:
        print("Guess Higher")
    elif g>answer:
        print("Guess lower")
    else :
        print("Correct!")
        boo=0
print("Game Over")
