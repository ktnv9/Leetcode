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


# static attributes
#   shared among all instance of the class
#  A static attribute (sometimes called a class attribute)
# is an attribute that belongs to the class itself; not any specific instance of the class.

class User:

    usercount = 0  # static attribute
    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.usercount += 1

    def display(self):
        print(f'Username: {self.username}, Email: {self.email}')

user1 = User("V", "gmail")
user2 = User("V", "ymail")

print(User.usercount)
print(user1.usercount)
print(user2.usercount)

user1.phone = 900

print(user1.phone)

# class level configuration such as counting #.of objects created. 
# default parameters for all the objects.

# To define a static method, we use the @staticmethod decorator.


class BankAccount:

    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: {self._balance}")
        else:
            print("deposit amount must be positive")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = BankAccount("V", 500)
account.deposit(200) # instance method
print(BankAccount.is_valid_interest_rate(4)) # static method
print(BankAccount.is_valid_interest_rate(10)) # static method
print(account.is_valid_interest_rate(9))



    