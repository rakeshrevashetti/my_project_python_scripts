import os

def create_file(filename):
             try:
                 with open(filename, "w") as file:
                     file.write("Hey guys welcome devops world 2023") 
                     print("We have successfully created file " +filename+ " in pwd")
             except IOError:
                      print("error occured while createing" +filename+ " file")


def read_file(filename):
        try:
                with open(filename, "r") as file1:
                        content = file1.read()
                        print("content of " +filename+ " file is: ",content)
        except IOError:
                print("error occured while reading " +filename+ " file") 


def appending_file(filename):
        try:
                with open(filename, "a") as file2:
                        file2.write("\n""we have learnt some file handling in python") 
                        print("We have successfully appended content to " +filename+ " file")
        except IOError:
                print("error occured while appending " +filename+ " file") 


def rename_file(filename, new_filename):
        try:
                os.rename(filename, new_filename)
                print("We have successfully renamed " +filename+ " file to " +new_filename+ " file")
        except IOError:
                print("error occured while renaming " +filename+ " file") 


def delete_file(filename):
        try:
                os.remove(filename)
                print("We have successfully deleted " +filename+ " file")
        except IOError:
                print("error occured while deleting " +filename+ " file") 



if __name__ == "__main__":
    filename = "My_first_file.txt"
    new_filename = "My_second_file.txt"

    create_file(filename)
    read_file(filename)
    appending_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename) 