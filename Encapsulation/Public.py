# create class.

class Student:
    def __init__(self,name):
        self.name = name # Public variable.
        
    def display(self):
        print("Student Name : ", self.name) # Public method.
        
# Create object of Student class.
s = Student("Aniket")
s.display() # Call public method.
print("Student Name : ", s.name) # Access public variable.
# Accessing public variable outside the class.