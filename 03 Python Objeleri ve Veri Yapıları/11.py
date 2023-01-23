website = "http://www.google.com"
course = "Python course: Python from basics to adv (40 Hours)"
# 1-
print(" Hello World ".strip())
print("*******",website.strip("htppm"))
# 2- 
print(website[11:-4])
print(website.strip("w.com"))
# 3- 
print(course.upper())
# 4-
print(website.count("a",0,10))
# 5-
print(website.startswith("www"))
print(website.endswith(".com"))
# 6- 
print(website.find(".com",0,10)) # return -1 if false
print("rfind ",website.rfind(".com"))
#print("lfind ",website.lfind(".com"))
print("index ",website.index("g")) # rindex make error
print(website.find("g"))
# 7- 
print(course.isalpha())
# 8- 
print("Countent".center(50,"*"))
print("Countent".ljust(20,"*"))
print("Countent".rjust(20,"*"))
# 9-
print(course.replace(" ","-"))
print(course.replace(" ","-",2))
# 10-
print("Hello world".replace("world","There"))
# 11-
print(course.split(" "))

