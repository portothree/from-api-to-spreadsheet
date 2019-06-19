import json
import base64
import requests

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

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


auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}
auth_data = {
    'grant_type': 'client_credentials'
}
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

# Get the acess key from the response formated as json
access_token = auth_resp.json()['access_token']

user_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

user_params = {
    'screen_name': 'portothree',
    'count': '1'
}

user_url = '{}1.1/statuses/user_timeline.json'.format(base_url)

user_resp = requests.get(user_url, headers=user_headers, params=user_params).json()

#Parse the json

for item in user_resp:
    name = item['user']['name']
    username = item['user']['screen_name']
    tweet_id = item['id']
    tweet_text = item['text']

tweet_URL = 'https://twitter.com/{}/status/'.format(username)+str(tweet_id)

print(name, username, tweet_text, tweet_URL)