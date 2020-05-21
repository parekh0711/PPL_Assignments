from abstract_animals import Animals

class Wolf(Animals):
    def __init__(self,name,age):
        super().basic_features()
        self.name=name
        self.color="Gray"
        self.age=age
    def print_features(self):
        print("Created Wolf with name",self.name+".")
        print("It is",self.color,"in color.")
        print("It is",self.age,"years old.")
        super().print_features()

class Tiger(Animals):
    def __init__(self,name,age):
        super().basic_features()
        self.name=name
        self.color="Orange"
        self.age=age
    def print_features(self):
        print("Created Tiger with name",self.name+".")
        print("It is",self.color,"in color.")
        print("It is",self.age,"years old.")
        super().print_features()

class Lion(Animals):
    def __init__(self,name,age):
        super().basic_features()
        self.name=name
        self.color="Yellow"
        self.age=age
    def print_features(self):
        print("Created Lion with name",self.name+".")
        print("It is",self.color,"in color.")
        print("It is",self.age,"years old.")
        super().print_features()

class Rhino(Animals):
    def __init__(self,name,age):
        super().basic_features()
        self.name=name
        self.color="Gray"
        self.age=age
    def print_features(self):
        print("Created Rhino with name",self.name+".")
        print("It is",self.color,"in color.")
        print("It is",self.age,"years old.")
        super().print_features()

class Hippo(Animals):
    def __init__(self,name,age):
        super().basic_features()
        self.name=name
        self.color="Gray"
        self.age=age
    def print_features(self):
        print("Created Hippo with name",self.name+".")
        print("It is",self.color,"in color.")
        print("It is",self.age,"years old.")
        super().print_features()

class Fox(Animals):
    def __init__(self,name,age):
        super().basic_features()
        self.name=name
        self.color="Orange"
        self.age=age
    def print_features(self):
        print("Created Fox with name",self.name+".")
        print("It is",self.color,"in color.")
        print("It is",self.age,"years old.")
        super().print_features()

class Cheetah(Animals):
    def __init__(self,name,age):
        super().basic_features()
        self.name=name
        self.color="Yellow"
        self.age=age
    def print_features(self):
        print("Created Cheetah with name",self.name+".")
        print("It is",self.color,"in color.")
        print("It is",self.age,"years old.")
        super().print_features()

class Giraffe(Animals):
    def __init__(self,name,age):
        super().basic_features()
        self.name=name
        self.color="Yellow"
        self.age=age
    def print_features(self):
        print("Created Giraffe with name",self.name+".")
        print("It is",self.color,"in color.")
        print("It is",self.age,"years old.")
        super().print_features()

class Hyena(Animals):
    def __init__(self,name,age):
        super().basic_features()
        self.name=name
        self.color="Gray"
        self.age=age
    def print_features(self):
        print("Created Hyena with name",self.name+".")
        print("It is",self.color,"in color.")
        print("It is",self.age,"years old.")
        super().print_features()
