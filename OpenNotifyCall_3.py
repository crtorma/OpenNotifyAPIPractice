import requests

# Call #3: How many people are on the ISS?
response = requests.get("http://api.open-notify.org/astros.json")

print("Call #3")
print(response.content)
