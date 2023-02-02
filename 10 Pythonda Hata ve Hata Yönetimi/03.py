x=1945

#if x<1950:
#   raise Exception("Archive unavilable")
psw="0asassas56132sa@"
def f(psw):
    import re
    if len(psw)<8:
        raise Exception("password is short")
    elif (not re.search("[a-z]", psw)):
        raise Exception("password must contain letters")
    elif (not re.search("[0-9]", psw)):
        raise Exception("password must contain digits")
    elif (not re.search("[_#$@]", psw)):
        raise Exception("password must contain special char")
    else :
        print("Password Accepted")
try :
    f(psw)
except Exception as e:
    print(e)

class Person:
    def __init__(self,name="",id=0):
        if id<=0:
            raise Exception("Wrong id")
        else:
            self.name=name
try:
    p1=Person("Ali",-12)
except Exception as e:
    print(e)
        