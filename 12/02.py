# return func

def f1(x):
    
    def f2(y):
        return x**y
    return f2


a=f1(2)
print(type(a))
print(a(3))
print(a(4))

#-----------------------------

def check(page):
    def inner(role):
        if role=="Admin":
            return f"{role} role can access {page} page"
        else :
             return f"{role} role can not access {page} page"
    return inner
user1=check("Product page")
print(type(user1))
print(user1)
print(user1("Admin"))
print(user1("user"))
#-----------------------------
def ops(op):
    def summ(*args):
        return sum(args)
    
    def multi(*args):
        total=1
        for a in args:
            total*=a
        return total
    if op =="sum":
        return summ
    elif op=="mult":
        return multi
Q=ops("sum")
print(Q(1,2,3,100))
P=ops("mult")
print(P(2,4,8))