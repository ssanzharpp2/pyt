import os
for(root, dirs, files) in os.walk("C:/Users/Admin/work/lab4"):
    print("%s"%root)
print("-"*40)
for(root, dirs, files) in os.walk("C:/Users/Admin/work/lab4"):
    print("%s"%root)
    print("%s"%files)
print("-"*40)
for(root, dirs, files) in os.walk("C:/Users/Admin/work/lab4"):
    print("%s"%files)



import os
pat = input("Input path: ")
if os.path.exists(pat):
    print("The path exists")
    if os.access(pat, os.R_OK):
        print("Readable")
    else:
        print("Unreadable")
    if os.access(pat, os.W_OK):
        print("Writable")
    else:
        print("Unwritable")
    if os.access(pat, os.X_OK):
        print("Executable")
    else:
        print("Unexecutable")
else:
    print("The path does not exist")



import os

pat = input("Input path: ")
if os.path.exists(pat):
    print("The path exists")
    dir = os.path.dirname(pat)
    file = os.path.basename(pat)
    print(dir)
    print(file)
else:
    print("The path does not exist")





path = input("Input the path to text file: ")
file = open(f"{path}", "r")
cnt = 0
for row in file:
    cnt = cnt + 1
print(cnt)
file.close()


file = open("text.txt", 'w')
lst = ["cow", "horse", "sheep", "camel", "goat"]
for x in lst:
    file.write(x + "\n")
file.close()


for x in range(26):
    y = x + ord("A")
    l = chr(y)
    with open(f"{l}.txt", "w") as file:
        file.write(f"Just {l}.txt file")



path = input("Input path from text file: ")
file1 = open(f"{path}", "r")
copy = file1.read()
file2 = open("text.txt", "w")
file2.write(copy)
file1.close()
file2.close()


import os
pat = input("Input path: ")
if os.path.exists(pat):
    print("The path exists")
    if os.access(pat, os.R_OK):
        print("Readable")
    else:
        print("Unreadable")
    if os.access(pat, os.W_OK):
        print("Writable")
    else:
        print("Unwritable")
    if os.access(pat, os.X_OK):
        print("Executable")
    else:
        print("Unexecutable")
    os.remove(pat)
else:
    print("The path does not exist")