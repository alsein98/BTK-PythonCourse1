sayilar=[1,2,3,4,5,6]

# 1- 
c=0
while c<len(sayilar):
    print(sayilar[c])
    c+=1
    
# 2-
start=4#int(input("enter start"))
end=9#int(input("enter end"))
while start <= end:
    if start%2!=0:
        print(start)
    start +=1
# 3-
x=100
while x>0:
    print(x,end=" ")
    x-=1
# 4- 

# 5- 
num=3#int(input("enter products numbers"))
d={}
x=0
while x<num:
    name=input("Enter product name ")
    price =input(   "Enter product price")
    d[x]={"name":name,"price":price}
    x+=1
x=0
while x<num:
    print(f"product {x} name :{list(d[x].values())[0]}  price : {list(d[x].values())[1]}")
    x+=1 