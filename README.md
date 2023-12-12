# Quality Assurance Engineer Technical Assessment

## Booking - UpdateBooking

Create multiple test scripts for the Update Booking endpoint of the restful booker API, covering scenarios

Study the Restful Booker API, focusing on the "Update Booking" Endpoint.

Identify different test scenarios, factoring in various user states and data conditions

Develop scripts to automate scenarios.

[LINK](https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-UpdateBooking)

`PUT`

### `https://restful-booker.herokuapp.com/booking/:id`

`https://restful-booker.herokuapp.com/booking/1`

# API Test Script Development for Restful Booker

## Automation of Test Case Scenarios With The Below Payload

```
{
  "firstname": "James",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": true,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
}
```

Install the Requests Library

```
pip install requests
```

Python Script that Automates the Test Case Scenarios

```
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
```
