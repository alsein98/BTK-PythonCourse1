# Applicaion on strings

website = "http://www.google.com"
course = "Python course: Python from basics to adv (40 Hours)"
# 1- 'Course'  how much char in 'course' vbariable
print(len(course))

# 2- print the www chars from 'wwebsite'
print(website[7:10])
# 3- print the com chars from 'wwebsite'
print(website[-3:])
# 4- print first 15 and last 15 chars from Course
print(course[:16],"-",course[-15:])
# 5- print the reverse of course
print(course[::-1])
#--------------------------------
# 6- replace w letter to W in "Hello world"
s="Hello world" # strings are immutable
s= s[:6]+"W"+s[-4:]
print(s.replace('l','*') )# dont change the original var
print(s) 
# 7- print ab as ababab 
str1="ab"
print(str1*3)