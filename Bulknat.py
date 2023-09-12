import requests
import xml.etree.ElementTree as ET

# Define the Palo Alto device URL, username, and password
device_url = "https://your-palo-alto-device/api"
username = "your-username"
password = "your-password"

# Define the API endpoint to get the system information
api_endpoint = f"{device_url}/?type=op&cmd=<show><system><info></info></system></show>"

# Make an HTTP GET request to the Palo Alto API
response = requests.get(api_endpoint, auth=(username, password), verify=False)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML response
    root = ET.fromstring(response.text)
    
    # Find the hostname element in the XML
    hostname_element = root.find(".//hostname")
    
    # Extract and print the hostname
    if hostname_element is not None:
        hostname = hostname_element.text
        print(f"Palo Alto hostname: {hostname}")
    else:
        print("Hostname not found in the response.")
else:
    print(f"Failed to retrieve hostname. Status code: {response.status_code}")
