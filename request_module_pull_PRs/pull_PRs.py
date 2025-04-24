import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

details = response.json()

print(details[4]["user"]["login"])
print("------------------------------")

for i in range(len(details)):    
     print("Created by:", details[i]["user"]["login"])


