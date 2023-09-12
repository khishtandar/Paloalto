import requests

# Define your PaloAlto API credentials and URL
api_url = 'https://your-paloalto-firewall/api'
username = 'your-username'
password = 'your-password'

# Create a session and authenticate with the firewall
session = requests.session()
login_payload = {
    'username': username,
    'password': password
}
login_url = f'{api_url}/login'
response = session.post(login_url, data=login_payload)

if response.status_code != 200:
    print(f'Failed to authenticate: {response.text}')
    exit()

# Read the CSV file and loop through the rows
with open('nat_rules.csv', 'r') as file:
    for line in file:
        source_ip, dest_ip, translated_ip, service = line.strip().split(',')
        
        # Define the NAT rule payload
        payload = {
            'source': source_ip,
            'destination': dest_ip,
            'translated': translated_ip,
            'service': service,
            # Add other parameters as needed
        }
        
        # Make an API POST request to create the NAT rule
        response = session.post(f'{api_url}/nat/rules', json=payload)
        
        if response.status_code == 200:
            print(f'Successfully created NAT rule for {source_ip}')
        else:
            print(f'Failed to create NAT rule for {source_ip}: {response.text}')

# Logout to end the session
logout_url = f'{api_url}/logout'
session.post(logout_url)
