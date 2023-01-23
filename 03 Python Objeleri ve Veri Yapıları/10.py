# Strings Methods
str1="  abc defg    *"
str1.upper() # does not chang the var value 
print(str1.upper().lower())
print(str1.title())
print(str1.capitalize())
print(str1.strip())
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
print(str1.center(20))
print(str1.center(50,"*"))
print(str1.split(" "))
print("*".join(str1.split(" ")))
print(str1.find("de")) # -1 if not
print(str1.startswith('a'))
print("ikdfaüç".replace("ü","U").replace("ç","C"))
