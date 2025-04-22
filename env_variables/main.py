
from dotenv import load_dotenv
import os

load_dotenv()

name = os.getenv("Name")
age = os.getenv("age")
city = os.getenv("city")


print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}") 

