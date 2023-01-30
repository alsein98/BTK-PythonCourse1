# Lambda , Map , Filter
def f(num): return num **  2
nums=[1,2,3,4,5,6,7]

print(map(f,nums))
# Map
print(list(map(f,nums)))

for i in map(f,nums):
    print(i,end=" ") 

# Lambda
print()
mapped = list(map(lambda n:n**2,nums))
print(mapped)

f2= lambda num:num**3
print(list(map(f2,nums)))

# Filter
def f3(num):
    return num>3
filtered = list(filter(f3, nums))
print(filtered)

print(list(filter(lambda n:n%2!=0, nums)))