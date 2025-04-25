import shutil
import os


source = "./assignment/mock.py"
destination = "./backup_file"


if os.path.exists(source):
    shutil.copy(source,destination)
    print("The "+source+" has been backed up in the "+destination+" file")
else:
    print("The files "+source+" does not exist")