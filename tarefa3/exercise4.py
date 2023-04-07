# INSTANCE, CLASS AND STATIC METHODS

class Person:

    group = 'Humans'

    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def presentation(self):
        print('My name is '+ self.name + ' and i am '+ str(self.age) + ' years old')

    @classmethod
    def info(cls):
        print(cls.group + ' are the most common and widespread species of primate in the great ape family Hominidae, and also the most common species of primate overall')

    @staticmethod
    def hability():
        print('People need to breath, eat and sleep.')

me = Person('Kalil', 22)

# instance methods can only be called by instance
print('Instance methods')
me.presentation()

# class methods can only be called by the class
print('\nClass methods')
Person.info()

# static methods can be called by both instance and class
print('\nStatic methods')
Person.hability()
me.hability()


