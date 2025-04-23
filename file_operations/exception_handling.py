
import os

def list_files_in_folder(folder_name):
    try:
         files = os.listdir(folder_name)
         if not files:
            print(f"The folder {folder_name} is empty.")
            return None
         else:
            print("\nThe folder " +folder_name+  " contains the following files:")
            for i in files:
            
             print(i)
         return files
    except FileNotFoundError:
        print("\nError: The folder " +folder_name+ " does not exist.")
        return None 
        


def main():
   folder_name = input("Enter the folder name: ").split() 
   for folder_path in folder_name:
       print("\nThe folder name is: ", folder_path)

       list_files_in_folder(folder_path)
                
if __name__ == "__main__":
   
   main()
   
   