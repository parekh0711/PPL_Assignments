#The purpose of this program is to show  virtual functions,  abstract classes, base class, derive class, interfaces, polymorphism , modularity and hierarchy in Python

from class_animals import*
#   Animals is an abstract class
#   It cannot be instantiated

#   Animals is the base class for all other classes
#   Wolf, Tiger, Lion, etc are derived classes.

# Modularity can be achieved by splitting the code into different modules.
# in this case, all derived classes are in class_animals.py and base class is in abstract_animals.py

#polymorphism refers to the function overriding, in this case, implemented by redefinging the functions in children class through virtual methods.
if __name__ == '__main__':
    print("Welcome to your Jungle")
    while True:
        animals=['Default',Wolf,Tiger,Lion,Rhino,Hippo,Fox,Cheetah,Giraffe,Hyena]
        print("Enter choice of animal. Options are:")
        print("1. Wolf\n2. Tiger\n3. Lion\n4. Rhino\n5. Hippo\n6. Fox\n7. Cheetah\n8. Giraffe\n9. Hyena\n")
        cl=int(input())
        cl=animals[cl]
        name=input("Enter Name\n")
        age=float(input("Enter Age\n"))
        a=cl(name,age)
        a.print_features()
        print("")
