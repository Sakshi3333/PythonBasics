fd = open("SHINDE.txt", 'r')
print("Information of the file:", fd)
print("Contents of the file")
print(fd.read())

print("Reading singleline from the file")
print(fd.readline())

print("Current location of the file is:", fd.tell())
fd.seek()

print("Contents of the whole file")
print(fd.read())

fd.close()

fd = open("SHINDE.txt", 'a+r')
fd.write("SAKSHI SAMPAT SHINDE\n")
fd.write("PARK INFINIA BHEKRAINAGAR FURSUNGHI PUNE 412308")
fd.seek(0)
print(fd.read())
fd.close()