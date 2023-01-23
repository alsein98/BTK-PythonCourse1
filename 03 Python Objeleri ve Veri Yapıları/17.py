# Dictionary

#key - value

d1={41:"kocaeli",34:"istanbul",1:"adana"}
#print(d1["adana"]) error
print(d1[34])
print(d1.get(1))
print(list(d1.keys()))
print(list(d1.items()))
print(type(list(d1.items())[0]))# list of tuples
d1[2]="maras"
print(d1)
d1[34]="İSTANBUL"
print(d1)

user={"ali":{"fullname":["ali","huseyin"],"id":1257,"phone":5379446,"gender":"male"}}
print(user["ali"]["gender"])
print(" ".join(user["ali"]["fullname"]))