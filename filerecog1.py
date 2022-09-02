from datetime import datetime
from pathlib import Path

our_files = Path("E:\Python Programs\ass10.y")

for file in our_files.iterdir():
    print(file)