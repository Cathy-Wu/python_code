class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('dog is running...')

    def eat(self):
        print('dog is eating...')
    

class Cat(Animal):
    pass

