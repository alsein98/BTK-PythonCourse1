cars=["BMW","Mercedes","Opel","Mazda"]
print(len(cars))
print(cars[0],cars[-1])
#tmp=cars.find("Mazda")
print(cars) #4
print("Mercedes" in cars) #5 
print(cars[-2])
print(cars[:3])
cars2=cars
cars2[-2:]=["Toyota","Renault"]
print(cars2)
cars2.append("Audi")#.append("Nissan")
cars2.append("Nissan")
print("**",cars+["Audi","Nissan"])

print(cars2)
cars2.pop()
print(cars2)
cars2.reverse()
print(cars2)
print("reversed ",cars[::-1])
s1=[2010,(70,60,70)]
print(s1)