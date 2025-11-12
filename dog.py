class Dog:
    def __init__(self, name , age ,breed ):
        self.name=name
        self.age=age
        self.breed=breed
    def barks(self):
        print(f"{self.name} barks")
dog1=Dog("james", 3, "pomeranin")
print(dog1.name)        
