
import os

def list_the_files(folder_name):
        print("\nThe folder " +folder_name+  " contains the following files:\n")
        new = os.listdir(folder_name)
        if not new:
             print("\nNo files Found in this Folder")
        else:
          for i in new:
               
            print(i)

def main():
    folder_name = os.getcwd()
    print("\nThe Folder which Iam about to list is: ",folder_name)
    list_the_files(folder_name)



if __name__ == "__main__":
    main()