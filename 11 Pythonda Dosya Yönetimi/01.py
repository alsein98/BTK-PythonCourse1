# open(filepath,mod)
#--------------------------------------------------
# "w" write - creating - old data will be deleted
file1=open("file1.txt","w",encoding='utf-8')   
#print(file1)
file1.write("Line 1 Ö") 
file1.close()
#--------------------------------------------------
# "a" append - creating
file2=open("file2.txt","a")
file2.write("File 1, Line 1 \n")
file2.close()
#--------------------------------------------------
# "x" create - if exists raise Error
try:
    file3=open("file2.txt","x")
except Exception as e:
    print(e)
try:
    file3=open("file3.txt","x")
except Exception as e:
    print(e)
#--------------------------------------------------
# "r" read - if didnt exist raise Error
