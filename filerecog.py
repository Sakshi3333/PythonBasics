from datetime import datetime
from pathlib import Path

# create a path object
our_files = Path("C:\Windows\System32\cmd.exe")

# Is the path a file?
print(our_files.is_file())               # Returns false

# Is path the directory?
print(our_files.is_dir())                # Returns true

# What is the parent of the file?
print(our_files.parent)                    # Returns C:\Windows\System32\cmd.exe

# What is the base of the filename?
print(our_files.stem)                     # Returns files

# What are extensions of file?
print(our_files.suffix)                   # Returns "" (since its not a file)

for file in our_files.iterdir():
    print(file)