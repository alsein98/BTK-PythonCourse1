def f1(name):
    print("Hello",name)
f2=f1
f2("Jack")
#del f2

def f3(x):
    print("f3")
    def f4(x):
        print("f4")
        print(x**2)
    f4(x)
f3(2)

x = isinstance(5, int)
print(x)