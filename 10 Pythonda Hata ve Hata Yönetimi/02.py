n  ="10"
m  ="8"
try :
    print(4/2 )
except ZeroDivisionError as z:
    print("ZeroDivisionError")
    print(z)
except (ValueError,KeyError)  as v:
    print("Value Error")
    print(v)
except Exception as e:
    print("Error")
    print(e)
else :
    print("Done")
finally:
    print("Her zaman çalışır")