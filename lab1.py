"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a base class for an animal and derived classes for specific 
               types of animals in an animal kingdom program.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Animal that represents a generic animal in an animal kingdom.
# This class should have an initialiser with at least three attributes. E.g. name, age, and habitat.
# Add at least two methods for common animal behaviors. E.g. eat and sleep.
class Animal:

    def __init__(self, name, type, habitat):
        self.name = name
        self.type = type
        self.habitat = habitat

    def hunting(self):
        print(f"{self.name} is hunting") 

    def sleep(self):
        print(f"{self.name} is sleeping")
 
    def __str__(self):
        return f"Animal: {self.name}, Type: {self.type}, Habitat: {self.habitat}"

# Create at least two derived classes from the Animal class. E.g. Bird and Fish.
# Give each of the derived classes at least one specific behavior. E.g. fly and swim.
class Lion(Animal):

    def __init__(self, name, type, habitat, mane_length):
        super().__init__(self, name, type, habitat)
        self.mane_length = mane_length

    def growl(self):
        print(f"{self.name} growls")

    def scratch(self):
        print(f"{self.name} scratches")

# Create at least two instances of the Animal derived classes with different data.

lion1 = Lion("bob", "mammal", "africa", "18m")


# Write code that prints out the details of each animal and calls their specific behaviors.
print(lion1)



