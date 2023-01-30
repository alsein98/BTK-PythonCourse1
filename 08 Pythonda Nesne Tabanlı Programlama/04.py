# inheretence

class Person:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
        print("Person Created")
        
    def eat(self):
        print("Person ate")
    def run(self):
        print("Person run")
    def drink(self):
        print("Person drinked")
    def whoAmI(self):
        print("I am a Person")
    
class Student(Person):
    
    def __init__(self,name,lastname):
        pass
        self.name=name
        self.lastname=lastname
        self.stuNo=1821200
        print("Student Created")
        #supper.__init__(self)
        
    def eat(self):
        print("Student ate")
    def run(self):
        print("Student run")
    def drink(self):
        print("Student drinked")
        
class Teacher(Person):
    def __init__(self,name,lastname,salary=0):
        super().__init__(name, lastname)
        self.salary=salary
        #self.name=name
        #self.lastname=lastname
        print("Teacher Created")
        #supper.__init__(self)
        
    def eat(self):
        print("Teacher ate")
    def run(self):
        print("Teacher run")
    def drink(self):
        print("Teacher drinked")
#s1=Student("Ali", "Huseyin")
#s1.eat()
#s1.whoAmI()
t1=Teacher("Ahmad", "Khaled",15000)
print(t1.salary)