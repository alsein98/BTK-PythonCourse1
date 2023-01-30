class Person:
   # pass 
    # class attributes
    address="no info"
    
        # construct.
    def __init__(self,name="",year=0):# this
        
        # object attricutes
        self.name=name
        self.year=year
        print("**Object Created**")
        
    # methods
    def intro(self):
        print("Hello there I am",self.name,"And i am",self.year,"Years old")
    
    
p1=Person("Ali",24)
p1.intro()


class Circle:
    PI=3.14
    
    def __init__(self,yaricap=1):
        self.yaricap=yaricap
        
    def cevre(self):
        return 2* self.PI + self.yaricap
    
c1=Circle(4)
print(c1.cevre())