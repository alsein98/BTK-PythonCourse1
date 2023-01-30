# Functions
def f1():
    return 0
print(type(f1)) #<class 'function'>

#---------------------------------
def f2(name):
    print(f"hello {name}")
f2("ali")

def f3(name="user"):
    print(f"hello {name}")
f3()

def f4(name="user"):
    return f"hello {name}"
print(f4("huseyin"))
#---------------------------------
def f5(n,m):
    '''
FUNCTİON 5
DOCSTRING: info
    '''
    return n+m
print(f5(1,5))
help(f5) # if print it -> None
#---------------------------------
help("".upper)
#---------------------------------
print(dir([1,2,3]))
#---------------------------------
print(locals())
#---------------------------------

#---------------------------------

#---------------------------------

#---------------------------------

#---------------------------------