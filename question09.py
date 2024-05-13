#the class customer will inherit all of the attribute of the person class since the person class is being passed in the parameters

#it is the dunder init method, this means you are setting up instance variables/class attributes

class person:
    def __init__(self, name=''):
        self.name = name


    def repeat_name(self):
        name = 'fred'
        print(f"my name is {name}")

class customer(person):
    name = 'fred'
    person.repeat_name(name)
