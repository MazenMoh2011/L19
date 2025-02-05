class  Dog:
    breed="Golden retriever"
    def __init__ (self, breed, name):
        self.breed= breed
        self.name= name
Allmight= Dog("Golden retriever", "All might")
Zenitsu= Dog("Golden retriever", "Zenitsu")
print("This dog's name is {} and he's a {}".format(Allmight.name, Allmight.breed))
print("This dog is also a {} and his name is {}".format(Zenitsu.breed, Zenitsu.name))