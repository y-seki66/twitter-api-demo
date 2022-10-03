import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import schedule
import time
import datetime

load_dotenv()

def getCurrentTime():
	now = datetime.datetime.now()
	message = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
	print(message)
	return message

def tweet():
  twitter = OAuth1Session(
    os.environ['CONSUMER_API_KEY'],
    os.environ['CONSUMER_API_SECRET_KEY'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET']
  )
  url = "https://api.twitter.com/2/tweets"
  text = getCurrentTime()
  params = {
    "text": text
  }
  res = twitter.post(url, json=params)
  print(res.status_code)

schedule.every().hour.do(tweet)

while True:
  schedule.run_pending()
  time.sleep(1)