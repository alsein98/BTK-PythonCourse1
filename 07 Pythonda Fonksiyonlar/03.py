# Parameters
name="ahmad"
def f1(n): # pass by value
    n="mujtahid"
f1(name)
print(name)
#-------------------------------
l=[[1,2,3],"ankara","istanbul"]
l2=l[:]
l3=l
l4=l.copy()
l5= []
l5.append(l)

def f2(n):  # pass by pointer
    n[0][0]="Aleppo"
f2(l)
print(l) 
print(l2) # no changed not actual copy  
print(l3) #  changes not actual copy
print(l4) # no changed not actual copy
print(l5) # not actual copy
#-------------------------------
def f3(a,b,c=0):
    print((a+b+c))
f3(1,2,3)
f3(1,2)
#-------------------------------
print("-----")
def f4(*par):
    print(par)
    print(sum(par))
f4(1,2,3)
f4(1,2)
f4(1,2,6,8,5,2,1,5,6,2)
#-------------------------------
print("-----")
def f5(*par):
    for p in par:
        print(p,end=" ")

f5(1,2,6,8,5,2,1,5,6,2)
#-------------------------------
print("-----")
def f6(**args):
    for k,v in args.items():
        print(k,v)
        print(f"{k} is {v} ")

f6(name="ali",age=24,city="istanbul")
f6(name="ali",age=24,city="istanbul",phone=357784)
f6(name="ali",age=24,city="istanbul",phone=357784,mail="ali@gmail.com")
#-------------------------------
print("-----")
def f7(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
f7(1,2,3,4,5,6,7,k1="key1",k2="key2",key3="key3Value")
#-------------------------------
print("-----")
def f8(a,b,*args,c):
    print("a",a)
    print("b",b)
    print("args",args)
    print("c",c)
f8(1,2,3,4,5,6,c=7) 
#-------------------------------
print("-----")
def f9(a,b,*args,c=0): # C always is 0
    print("a",a)
    print("b",b)
    print("args",args)
    print("c",c)
f9(1,2,3,4,5,6,7,889789) 