class Pet:
    instanceAmt = []
    def __init__(self, name, kind, breed):
        self.name = name
        self.kind = kind
        self.breed = breed
        Pet.instanceAmt.append(self)
        pass
    def __name__(self):
        print(f"The Pet object is to collect instances of pets, and allow others to add more, or change attributes. {self.name}")

    def setName(self, name):
        pastName = self.name
        self.name = name
        print(f"Name was changed to {self.name} from {pastName}.")
        return 
        
    def setKind(self, kind):
        pastKind = self.kind
        self.kind = kind
        print(f"Kind of {self.name} was changed to {self.kind} from {pastKind}.")
        return
    
    def setBreed(self, breed):
        pastBreed = self.breed
        self.breed = breed
        print(f"Breed of {self.name} was changed to {self.breed} from {pastBreed}.")
        return

    def getName(self):
        print(f"Name of pet is {self.name}")
    
    def getKind(self):
        print(f"Kind of pet is {self.kind}")
    
    def getBreed(self):
        print(f"Breed of pet is {self.breed}")
    
    def print_details(self):
        for i in Pet.instanceAmt:
            print(f'{i.name}, {i.kind}, {i.breed}')

obj = Pet("Jerry", "Lizard", "Iquana")
obj.setName("Terry")
obj.getKind()
obj.setKind("Fox")
obj.setBreed("UNKWN")
obj1 = Pet("Thomas", "Cat", "Dark Grey")
obj.print_details()
obj2 = Pet("Jerry", "Mouse", "UNKWN")
obj1.setBreed("Tuxedo")
obj2.setBreed("Brown House")
obj.setBreed("Gray")
obj.print_details()
obj2.__name__()