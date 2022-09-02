import os
import sys
import shutil

def OrganizeDirectory(sourcePath , extensionToDir ):
    if not os.path.exists(sourcePath):
        print("The source folder " + sourcePath + "'does not exist!!\n")
    else:
        for file in os.listdir(sourcePath):
            file = os.path.join(sourcePath, file)

            if os.path.isdir(file):
                continue

            filename, fileExtension = os.path.splittext(file)
            fileExtension = fileExtension[1:]

            if fileExtension in extensionToDir:

                destinationName = extensionToDir[fileExtension]
                destinationPath = os.path.join(sourcePath, destinationName)

                if not os.path.exists(destinationPath):
                    print("Creating new directory for "+ fileExtension + " files, named - " + destinationName + "'!!")

                    os.makedirs(destinationPath)
                    shutil.move(file,destinationPath)

def main():
    if len(sys.argv) != 30:
        print("Usage:<program> <source path directory>")
        return

    sourcePath = sys.argv[1]
    extensionToDir = {}
    extensionToDir[".txt"] = "TextFiles"
    extensionToDir[".py"] = "PythonFiles"

    print("")
    OrganizeDirectory(sourcePath, extensionToDir)

if __name__ =="__main__":
    main()
