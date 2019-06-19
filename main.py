import json
import base64

with open('twitter_credentials.json', 'r') as file:
    creds = json.load(file)

# Get keys from twitter_credentials.json
client_key = creds['CONSUMER_KEY']
client_secret = creds['CONSUMER_SECRET']

# Encode and reformat keys
key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')

# Bytes to bytes that can be printed
b64_encoded_key = base64.b64encode(key_secret)

# From bytes back into unicode
b64_encoded_key = b64_encoded_key.decode('ascii')