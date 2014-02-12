import praw
import json
from upload_imgur import upload_imgur
from time import sleep
import re
from collections import deque

done = deque(maxlen=200)

keys = json.loads(open("api_keys").read())

r = praw.Reddit("ImgurMirrorBot by /u/Thirdegree")

def _login():
	USERNAME = raw_input("Username?\n> ")
	PASSWORD = raw_input("Password?\n> ")
	r.login(USERNAME, PASSWORD)
	return USERNAME

Trying = True
while Trying:
	try:
		USERNAME = _login()
		Trying = False
	except praw.errors.InvalidUserPass:
		print "Invalid Username/password, please try again."

