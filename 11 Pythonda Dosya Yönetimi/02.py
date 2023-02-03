# "r" read - if didnt exist raise Error


file2=open("file2.txt","r")
"""
print("--",file2.readline())
print("--",file2.readline())

print(file2)
print("**",file2.read())
print(file2.readable())
print(file2.fileno())
print(file2.isatty())
file2=open("file2.txt","r")
print("**",file2.read())
"""
#print(file2.read(5)) # char
print(file2.readlines())
file2.close()