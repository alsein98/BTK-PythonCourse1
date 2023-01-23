# Dictionary cont.
number=input("number ")
name=input("name ")
surname=input("surname ")
phone=input(   "phone ")

students={}
students.update({
                 number:{
                     "name" : name,
                     "surname" : surname,
                     "phone" : phone,
                     
                     
                 }
                 
                 })
# repeat fron input() to add many elements to dict
print(students)