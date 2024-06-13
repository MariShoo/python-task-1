# create class with name of your choice. give it an __init__ decoreator with one argument in it.
# create one methd to simply print that variable. to do so u need to create class objct and call 
# the methodon it 
#  

# ##################################################################################



class Task2():

    def __init__(self, value1):
        self.value1 = value1


    def method(self):
        print(self.value1)


val1 = "hello world"
obj= Task2(val1)

obj.method()

    
"""
crate class with init decoreator which gets 3 positional arguments.
import 'person'dictionary fromm info.py  Ex:  from info import person 
craet methd which uses person dict and loops thdough and prints each value from dict
create another method that gets all looped values and creates a list of tham.( use loop )
if you can, dont create two methods but create one with both functionalityes implemented inside of it
use raplace values of init function which where given from the beginign and asign that to dictionary values as collows 
example: 

def __init__(self, name, age, city):
  ` rest of the code `

def replace(self):
    ` logic how to asign values to init variables `

"""

from info import person
class Person():

    def __init__(self ,name ,age, city):
        self.info = person

    # def replace(self):
         
    def about_person(self):
            print(self.info)

person1 = person()

person1.about_person



