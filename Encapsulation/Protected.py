# create class
class Employee:
    def __init__(self,emp_name, salary):
        self.emp_name = emp_name # Public variable.
        self._salary = salary # Protected variable.
    
    def display(self):
        print(f"The Employee {self.emp_name} has a salary of {self._salary}") # Public method.
    

class Manager(Employee):
    def display_protected(self):
        print(f"The Employee {self.emp_name} has a salary of {self._salary}") # Public method.
    
# Create object of Employee class.
e = Manager("Aniket", 50000)
e.display() # Call public method.
e.display_protected() # Call public method.
# Access protected variable outside the class.
print(f'The Employee {e.emp_name} has a salary of {e._salary}') # Still accessible (but conventionally protected.
