# class
# class ClassName:
class Person:
   # pass 
    # class attributes
    address="no info"
        # construct.
    def __init__(self,name="",age=0):# this
        self.name=""
        self.age=0
        print("**Object Created**")
            
    

    
    
    # methods
   
     

# object
p1=Person("ali",24)
print(p1)
p2=Person("huseyin",25)
print(type(p2))
print(p1==p2)
print(p1.name,p2.age)
p1.name="Abdullah"
print(p1.name )
p3=Person(name="Ahmad", age=29)
print(p3.address)
if 1>5:
    pass