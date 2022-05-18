import os, praw


# -------------------------- Reddit Setup ------------------------
reddit = praw.Reddit(
    client_id= 'UIOqsHrBEwDpxxCgaXdiBw',
	client_secret= 'sVAPDIXglzN5_vU0ZXXyg28Hse94pg',
    user_agent='<console:reddit_bot:0.0.7 (by /u/IchDeutschLerne)>',
	username = 'IchDeutschLerne',
	password = 'cagDLp5LRYUriw4'
	)

print(reddit.read_only)

CALL = ["!TranslatorBot", "Translator Bot"]

# -------------------------- Google Setup -------------------------
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/thors/Desktop/This is the JSON key file tied to my Google Cloud account/neural-foundry-347119-43c0fd9de30b.json"

from google.cloud import translate_v2 as translate

client = translate.Client()

# -------------------------- Main ---------------------------------

def process_submission(submission):
    # Ignore titles with more than 10 words as they probably are not simple translations and cost me and Google more $
	if len(submission.title.split()) > 10:
		return
	
	client = translate.Client()
	text = submission.title
	target = 'de'
	# Ka = Georgian,  en = English , ja = Japanese, pa= Punjabi, de = German
	Translated_title = client.translate(text, target_language = target, format_='text')
	Translation_string = Translated_title['translatedText']
	print(f"German Title Translation Bot: {Translation_string}")
	submission.reply(body= 'Translation of title to German: ' + Translation_string)
	# A reply has been made so do not attempt to match other phrases.


subreddit = reddit.subreddit("learnpython")
for submission in subreddit.stream.submissions():
       process_submission(submission) # now we have our submission object
