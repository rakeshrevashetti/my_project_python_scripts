import shutil

total , used , free = shutil.disk_usage("/")

def bytes_to_gb(a):
    return round(a / (1024 ** 3),2)

value1 = bytes_to_gb(total)
value2 = bytes_to_gb(used)
value3 = bytes_to_gb(free)

print(f"The total memory is ==> {value1} GB")
print(f"The total used memory is ==> {value2} GB")
print(f"The total free memory available is ==> {value3} GB")