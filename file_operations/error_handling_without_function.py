import os

folder_names = input("\nEnter the folder name: ").split()
for folder_name in folder_names:
    print("\nthe folder name is:", folder_name) 
    try:
        result = os.listdir(folder_name)
        print("\n-------   The files in the folder are    -------")
        for files in result:
            
           # print("The files present in "+folder_name+" are:",files ) 
           print(files)
            
    except FileNotFoundError:
        print("The folder does not exist.")
