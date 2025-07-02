#creating a file if doesnot exist
#f1 = open("file_1.txt", "x")
#reading a file
f1 = open("file_1.txt", "r+")
data = f1.read()
f1.write("welcome")

print(data)
