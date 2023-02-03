
"""
with open("file2.txt","r+") as file: # read and write
    file.seek(0)
    file.write( "File 2, Line 0")

with open("file2.txt","r+") as file: # read and write
    print(file.read())
"""
l=["1","2","3"]
with open("file2.txt","a") as file: # write in end
    file.write( "File 2, Line extra\n")

with open("file2.txt","r+") as file: # read and write
    print(file.read())

with open("file2.txt","r+") as file: # read and write
    file.writelines(l)
    print(file.read())
    
