import requests

# URL and payload data
url = 'https://restful-booker.herokuapp.com/booking/1'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cookie': 'token=abc123'
}
payload = {
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

# Send PUT request
response = requests.put(url, headers=headers, json=payload)

# Check response status and content
if response.status_code == 200:
    print("Booking created successfully!")
    print("Response:", response.json())
else:
    print("Failed to create booking.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
