import requests

# Call #2: When Will the ISS Pass?
parameters = {"lat": 37.7749, "lon": -122.4194}

response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)

print("Call #2")
print(response.content)

