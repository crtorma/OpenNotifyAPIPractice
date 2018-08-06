import requests

# Call #1: Where is the ISS?

# Makes a request to the OpenNotify API for the latest position of the ISS
response = requests.get("http://api.open-notify.org/iss-now.json")

# Prints the response to the request
print("Call #1:")
print(response.content)
