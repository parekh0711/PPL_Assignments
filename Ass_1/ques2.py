import random

li=[1,2,3,4,5,6]

g=input("Press r to roll dice or q to quit	:")

while not g=='q' :
	if g=='r' :
		random.shuffle(li)
		print(li[0])
	g=input("Press r to roll dice or q to quit	:")
	
	

