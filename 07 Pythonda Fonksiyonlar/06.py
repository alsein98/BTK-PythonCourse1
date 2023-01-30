# Global and Local Variables
x="global"

def f1():
    x="local"   
    print(x)
f1()
print(x) 

print("-----------------------")
y="global"

def f2():
   # y="local"   
    print(y)
f2()
print(y) 

print("------------------------")
name="Global name"

def f3():
    #name ="huseyin"
    
    def hello():
        print("Hello",name)
    
    hello()
f3()
print(name)
print("------------------------")
x= 50
def f4():
    global x
    
    x*=2
    print(x)
f4()
print(x) # main x changed 
 