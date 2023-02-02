list=["1","2","5a","10b","abc"]
# 1-
for l in list:
    try:
        print(int(l))
    except Exception as e:
        continue
# 2-
"""
while True:
    x=input("Enter ")
    if x !="q":
        try :
            x= int(x)
        except Exception as e:
            print(e)
    elif x =="q":
        print("Loop exit")
        break
    else :
        print(x)
"""
# 3-
psw="çasasas"
def f(psw):
    if "ç" in psw or "ş" in psw or "ı"in psw or "ö"in psw or "ü"in psw:
        raise Exception("turkish  alphap. founded")  
try:
    f(psw)
except Exception as e:
    print(e)
# 4- find fact. if x > 0

