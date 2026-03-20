import requests  
  
url = input("Url:")  
response = requests.get(url)  
text = response
print(response)  
print(text)