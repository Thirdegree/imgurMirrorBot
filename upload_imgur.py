import requests
import json
import base64


def upload_imgur(image_url, api_key):
	url = r"https://api.imgur.com/3/upload.json"
	payload = {'image': image_url,}
	headers = {'Authorization': 'Client-ID ' + api_key}
	r = requests.post(url, data=payload, headers=headers)
	j = json.loads(r.text)
	return j['data']['link']
	
	
