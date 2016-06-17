#coding:utf-8
#coding
'''
Created on 2016年5月9日

@author: look
'''
class Animal(object):
    def run(self):
        print "Animal is running..."
        
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

dog = Dog()
dog.run()
print dog.__class__
print type(dog)

cat = Cat()
cat.run()
print cat.__class__
print type(cat)
print type(123)

print 'look'




