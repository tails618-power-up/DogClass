class Dog:
    name="BOBERT"
    color="PURPLE"

    def Bark(self):
        print("Woof! My name is "+self.name)
    
mydog=Dog()
print(mydog.name)
mydog.name="DREWSENBERG"
print(mydog.name)

neighbordog=Dog()
neighbordog.name="ASHERMANDUDEYAAAA"
print (neighbordog.name)


mydog.Bark()
neighbordog.Bark()
