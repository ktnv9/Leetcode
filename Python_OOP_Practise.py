'''
# black formatter, pylance, python debugger, python

# https://github.com/DoableDanny/oop-in-python-course

# everthing we create in python is an object


name = "Varma"
id = 2

print(type(name))
print(type(id))

class Dog:

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof whoof")
    
class Owner:

    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

owner1 = Owner("Danny", "America", 90897)
dog1 = Dog("Dog1", "Breed1", owner1)

print(dog1.owner.name)


# self refers to the object itself.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def Greet():
        print(f'Hello')

person = Person("Varma", 30)
person.Greet()
'''

class User:

    def __init__(self, name, email):
        self.name = name
        self._email= email

    @property
    def email(self):
        return self._email
        
    @email.setter
    def email(self, new_email):
        self._email = new_email

    

user = User("Var", "  VARMA@gmAIL.cOM  ")

print(user.email)
user.email = "ktnvarma@gmail.com"
print(user.email)
