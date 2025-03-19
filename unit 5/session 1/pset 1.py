class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20:
            for c in new_catchphrase:
                if not (c.isalpha() or c.isspace()):
                    print("Invalid catchphrase")
                    return
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase")


    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def add_item(self, item_name):
        pass

apollo = Villager("Apollo", "Eagle", "pah")
bones = Villager("Bones", "Dog", "yip yap")

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 

# print(bones.name)
# print(bones.species)  
# print(bones.catchphrase) 
# print(bones.furniture)

bones.catchphrase = "ruff it up"

# print(bones.greet_player("Samia"))

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)
