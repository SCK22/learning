## Understand the uses of property decorator in python

#Defining a class
class Details:

    def __init__(self):
        self.__name = " "

    # using the @property decorator
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self, value):
        self.__name = None
        #or
        # def self.__name 

d = Details()

d.name = "me"
print(d.name)

d.name = "still me"
print(d.name)

del d.name

print(d.name)