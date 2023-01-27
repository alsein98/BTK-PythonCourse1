# range - enumerate(iterable)
for i in range(50,100,10):
    print(i,end=" ")
print()
l=list(range(50,100,20))
print(l)

s="hello world"

for i,l in enumerate(s):
    print(f"index : {i}, letter : {s[i]}") 
    print(f"index : {i}, letter : {l}") 

for items in enumerate(s):
    print(items,end="")
print()
for items in enumerate(s):
    print(items[1],end="")
print()
for items in enumerate(s):
    print(items[0],end="")
    
# zip
l1=[1,2,3]
l2=["4","5"]
l3=zip(l1,l2)#zip -> () () ziptype
print(l3)
l3=list(zip(l1,l2)) # [(), (),()]
print(l3)