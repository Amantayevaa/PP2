#1
import os
path = os.getcwd()
print("Only directories:")
print([i for i in os.listdir() if os.path.isdir(os.path.join(path, i)) ])
print("\nOnly files:")
print([i for i in os.listdir() if not os.path.isdir(os.path.join(path, i)) ])
print("\nAll: ")
print(i for i in os.listdir(path))

#2
import os
path = os.getcwd()
print("Existence: ", os.access(path, os.F_OK))
print("Readability: ", os.access(path, os.R_OK))
print("Writability : ", os.access(path, os.W_OK))
print("Executability : ", os.access(path, os.X_OK))

#3
import os
path = os.getcwd()
if (os.access(path, os.F_OK)):
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("\n" + "not exists")


#4
import os
path = r"C:\Users\Acer\Desktop\PP2\lab6\dir-and-files.py"

with open(path, "r") as file:
    lines_count = len(file.readlines())
    print(lines_count)

#5
import os
list = ["Almaty","Astana","Uralsk", "Aktobe"]

with open("dir5task.txt", "w") as file:
    for i in list:
        file.write(i + " ")

#6
import os
path = r"\Users\Acer\Desktop\PP2\lab6\new.letter"

for i in range(65,97):
    name = os.path.join(path, chr(i) +".txt")
    f = open(name, "a")

#7
import os

with open("1.txt", "r") as f1, open("2.txt", "a") as f2:
    for i in f1:
        f2.write(i)

#8
import os

path = os.getcwd()

if os.path.exists("12.txt"):
  os.remove("12.txt")
else:
  print("The file does not exist")