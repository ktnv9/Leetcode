# OOP Principles



# Encapsulation
    # bundling data & methods.

'''
class BadBankAccount:

    def __init__(self, balance):
        self.balance = balance

    
account = BadBankAccount(0)
account.balance = -1

print(account.balance)


class BankAccount:

    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

account = BankAccount()
print(account.balance)

account.deposit(199)
print(account.balance)

account.withdraw(12)
print(account.balance)

account.withdraw(255j)
print(account.balance)


class EmailService:

    def _connect(self):
        print("connecting to email server")

    def _authenticate(self):
        print("authenticating...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("sending email...")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server.")


email = EmailService()
email.send_email()
'''

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):
    
    def __init__(self, brand, model, year, door_count, wheel_count):
        super().__init__(brand, model, year)
        self.door_count = door_count
        self.wheel_count = wheel_count

class Bike(Vehicle):

    def __init__(self, brand, model, year, wheel_count):
        super().__init__(brand, model, year)
        self.wheel_count = wheel_count

car = Car("Ford", "Focus", 2008,5,4)
bike = Bike("Honda", "Scoopy", 2015, 2)

print(car.__dict__)
print(bike.__dict__)

car.start()
bike.start()

car.stop()
bike.stop()














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
'''


    