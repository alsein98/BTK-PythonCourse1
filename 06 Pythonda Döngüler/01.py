# Loops
numbers=[1,2,3,4,5]

for i in numbers:
    print(i,end="")
print()
    
names=["ali","huseyin","yousef"]
for n in names:
    print(f"may name is {n}",end=" ")
print()
    
tuple=(1,2,3)
for t in tuple:
    print(t,end="-")
print()
t2=([1,2],[3,4],[5,6])
for t,d in t2:
    print(t,d,end="+") #1 2+3 4+5 6+
print()
    
set1={1,2,3}
for s in set1:
    print(s,end=" * ")
print()

dict={"name":"ali","age":24,"no":1257}
for k,v in dict.items():
    print(k,end=" ")  # name age no
    print(v,end=" ")   #ali 24 1257
    print(k,v,end=" ") #name ali age 24 no 1257
print()
for k in dict.items():
    print(k,end=" ") #('name', 'ali') ('age', 24) ('no', 1257)