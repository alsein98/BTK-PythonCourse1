# Lists Methods
# append
fruits = ['apple', 'banana', 'cherry']
print(fruits)
fruits.append("orange")
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print("Append ",a)
# Clear
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
print(fruits)
# Copy
fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
fruits[0]="AAA"
print(fruits)
print(x)
# Count

x = fruits.count("cherry")
print(x)
# Extend
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print("extend",fruits)
# İndex
print(fruits.index("Volvo"))
# İnsert
fruits.insert(1, "Cat")
print("insert",fruits)
# pop
print(fruits.pop(0))
print(fruits)
# Remove
print(fruits.remove("banana")) # None
print(fruits)
# Reverse
fruits.reverse()
print(fruits)
# sort
print(fruits.sort()) # None
print(fruits)
fruits.sort(reverse=True)
print(fruits)
# count
print(fruits.count("Cat"))

print(min([1,2,3]))
print(max([1,2,3]))
print(sum([1,2,3]))