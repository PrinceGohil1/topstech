#1.Create a Python script that opens a file called lyrics.txt and prints the file pointer's current position using tell() before and after reading the first 10 characters.

file = open("lyrics.txt","r")
print("Before Reading = ",file.tell())

data = file.read(10)
print("First 10 Characters = ", data)

print("After Reading = ",file.tell())
file.close()