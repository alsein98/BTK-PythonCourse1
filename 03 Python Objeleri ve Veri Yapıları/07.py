# string formatting
name ="Ali" ; surname="Ahmad"
print("Hello {} {} ".format(name,surname))
print("Hello {0} {1} ".format(name,surname))
print("Hello {1} {0} ".format(name,surname))
print("Hello {n} {s} ".format(n=name,s=surname))
number=3.1245646545
print('{n:1.4}'.format(n=number))
print('{n:10.4}'.format(n=number),"-")
age=24
print(f"my name is {name} {surname}, and i'm {age} years old")