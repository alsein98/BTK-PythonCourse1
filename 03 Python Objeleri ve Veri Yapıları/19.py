# set

s1={1,2,3,3}
print(s1) # {1,2,3}
# immutable
# iterable
for x in s1:
    print(x)
s1.add(99)
print(s1)
s1.update([88,77,66])
print(s1)
s1.remove(77)
print(s1)
s1.discard(88)
print(s1)
# .pop / clear