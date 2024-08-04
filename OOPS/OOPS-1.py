# Python program to create a person class.
# Include attributes  like name, country and date of birth.
# Implement a method to  determine the person’s age.

from datetime import date
class Person:
    name = None
    country = None
    dob = None

    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        today = date.today()
        birth_date = date.fromisoformat(self.dob)
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

# List to store multiple Person instances
people = [
    Person('Prisha', 'India', '1995-11-22'),
    Person('Alice', 'USA', '1990-04-15'),
    Person('John', 'UK', '1985-06-10')
]

for person in people:
    print(f"{person.name} from {person.country} is {person.calculate_age()}"
    f" years old.")












