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

    def __init__(self, username, email, password):
        self.username = username
        self.__email = email
        self.password = password

    def say_hi_to_user(self, user):

        print(f'''Sending message to {user.username}: hey {user.username}, it is {self.username}''')

user1 = User("IronMan", "email", "123")
user2 = User("batman", "email2", "1234")

user1.say_hi_to_user(user2)

print(user1._User__email)
user1._User__email = "gmail"
print(user1._User__email)