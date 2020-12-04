# Reference: https://requests.readthedocs.io/en/latest/user/quickstart/

# JSON decoding Reference: https://pynative.com/python-json-load-and-loads-to-parse-json/

import requests

# Make HTTP request
r = requests.get('http://localhost:5000/api/payload')

# Convert response to JSON
response = r.json()
print(response)

# Access JSON data using key name
print(response["machine"])

# Access Nested JSON data using key name
print("Data: ", response["machine"]["LHS"]["maincompression_upperlimit"])