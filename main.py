import praw
import json
from upload_imgur import upload_imgur
from time import sleep, time
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

def main():
	comments = r.get_comments("Thirdegree")
	for post in comments:
		pattern = "(?<=\+/u/"+USERNAME+" )[\S]+"
		s = re.search(pattern, post.body)
		if s and post.id not in done:
			done.append(post.id)
			new_url = upload_imgur(s.group(), keys['client_id'])
			if new_url:
				print "%s -> %s"%(s.group(), new_url)
				post.reply(new_url)
				sleep(2)

running = True
while running:
	try:
		print time()
		main()
		########################
		running = False
		########################
	except KeyboardInterrupt:
		raise
	except praw.errors.RateLimitExceeded:
		print "Rate limit exceeded, sleeping 10 min"
		sleep(590)
	except:
		print "Unknown Error"
		sleep(60)