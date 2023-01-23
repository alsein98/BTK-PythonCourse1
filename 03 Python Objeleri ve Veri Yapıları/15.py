# List Application


names=["Ali","Yagmur","Hakan","Deniz"]
years=[1998,2000,1998,1987]

# 1-
names.append("Cenk")
print("Append",names)
# 2-
names.insert(0,"Sena")
print("İnsert",names)
# 3-
names.remove("Deniz")
print("Remove",names)
# 4-
#print(names.index("Deniz"))
# 5-
print(names.index("Ali"))
print("Ali" in names)
# 6-
names.reverse()
print("Reverse",names)
# 7-
names.sort()
print("Sort",names)
# 8-
years.sort()
print(years)
# 9-
str="Chevrolet, Dacia"
print(str.split(","))
# 10-
print(max(years),min(years))
# 11-
print(years.count(1998))
# 12-
years.clear()
print(years)
# 13-
i1=input("Enter 1 ")
i2=input("Enter 2 ")
i3=input("Enter 3 ")
marka=[]
marka.append(i1)
marka.append(i2)
marka.append(i3)
print(marka)
# 14-