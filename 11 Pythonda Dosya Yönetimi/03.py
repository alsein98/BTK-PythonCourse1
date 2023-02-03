with open("file2.txt","r")as file:
    print("++",file.readline())
    print("**",file.tell()) # where am i
    print("**",file.readline())
    print("**",file.tell()) # where am i
    file.seek(0)
    print("-----------------------")
    print("**",file.tell()) # where am i
    print("++",file.readline())
    print("**",file.tell()) # where am i





#  print(file2.readlines())
# file2.close()