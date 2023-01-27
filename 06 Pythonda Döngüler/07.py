num1=[x**2 for x in range(10)]
print(num1)

num1=[x**2 for x in range(10) if x%3==0]
print(num1)

string="hello world"
l=[s for s in string if s!=" "]
print(str(l))

years=[1983,1999,2008,1956,1986]
l2=[ x if x%2==0 else "tek" for x in range(10)]
print(l2)

l3= [ (x,y)  for x in range(3) for y in range(3)]
print(l3)
l4= [ (x,y,z)  for x in range(3) for y in range(3) for z in range(3)]
print(l4)