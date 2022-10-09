from urllib import response
import requests
#to get the response from get method 
response = requests.get("https://dog.ceo/api/breeds/image/random")
#to get the the server response code 
print(response.status_code)
#to convert that data into python dict format
print(response.json())