with open("sample_file.txt","r") as file:
    data = file.readlines()
    for each in data:
        splitting = each.split()
        print(splitting)
    