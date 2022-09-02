import os

location = 'E:\Python Programs'
files_in_dir = []
print("Enter the name of file xtension you want to see:")
name = input()

for r, d, f in os.walk(location):
    for item in f:
        if ('.txt') in item:
            files_in_dir.append(os.path.join(r,item))

for item in files_in_dir:
    print("files in dir:", item)