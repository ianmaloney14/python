class Pet:
    def __init__(self, name, type="puppy", tricks="peeing everywhere"):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100
    
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        print("*noise*")
        return self

class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
    