import praw
import json
from uploads import *
from time import sleep, time
import re
from collections import deque
import obot

done = deque(maxlen=200)

keys = json.loads(open("api_keys").read())
upload = {'imgur':upload_imgur, 'gfycat':upload_gfycat}


r = obot.login()

def _login():
	USERNAME = raw_input("Username?\n> ")
	return USERNAME

Trying = True
while Trying:
	try:
		USERNAME = _login()
		Trying = False
	except praw.errors.InvalidUserPass:
		print "Invalid Username/password, please try again."

def main():
	comments = r.helpers.comment_stream(r, "all")
	for post in comments:
		pattern = "(?<=\+/u/"+USERNAME+" )([\S]+) ([\S]+)"
		s = re.search(pattern, post.body)
		if s and post.id not in done:
			done.append(post.id)
			where, url = s.groups()
			if where in upload:
				end_url = upload[where](url, keys['client_id'])
				print "%s -> %s"%(url, end_url)
				post.reply(end_url)
				sleep(2)
					

running = True
while running:
	try:
		print time()
		main()
		########################
		#running = False
		########################
		sleep(10)
	except KeyboardInterrupt:
		raise
	except praw.errors.RateLimitExceeded:
		print "Rate limit exceeded, sleeping 10 min"
		sleep(590)
	except:
		print "Unknown Error"
		sleep(60)
