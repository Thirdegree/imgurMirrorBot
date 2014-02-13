import requests
import json
import base64
from random import randint


def upload_imgur(image_url, api_key):
	url = r"https://api.imgur.com/3/upload.json"
	payload = {'image': image_url,}
	headers = {'Authorization': 'Client-ID ' + api_key}
	r = requests.post(url, data=payload, headers=headers)
	j = json.loads(r.text)
	if not j['success']:
		return False
	return j['data']['link']

def upload_gfycat(image_url, _):
	random_string = randint(11111,9999999999)
	url = "http://upload.gfycat.com/transcode/%d?fetchUrl=%s"%(random_string, image_url)
	r = requests.post(url)
	j = json.loads(r.text)
	return "http://gfycat.com/%s"%(j['gfyname'])	