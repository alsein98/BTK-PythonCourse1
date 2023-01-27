# Wile

numbers=[1,2,3,4]

x=0
while x<100:
    if x%2==0:
        print(x,end=" ")
    x+=1

name ="" # false
while not name.strip():
    name=input("enter name")
print(f"merhaba {name}")