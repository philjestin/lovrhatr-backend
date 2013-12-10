import json
import random
import urllib2
from twython import Twython

headers = {
				'X-Parse-Application-Id':'',
				'X-Parse-REST-API-Key':'',
	}

tokens = {
	
				'APP_KEY':''
				'APP_SECRET':''
				'OAUTH_TOKEN':''
				'OAUTH_TOKEN_SECRET':''
	}

def get_insult():
	#Parse Restful API-Keys
	global headers

	#URL for Insults Database
	url = 'https://api.parse.com/1/classes/Insults'

	#Array to hold insults
	insults_array = []
	
	#Request (GET)
	request = urllib2.Request(url, data=None, headers=headers)
	results = urllib2.urlopen(request)
	data = results.read()
	insult_information = json.loads(data)
	insults = insult_information['results']
	for gather in insults:
		insults_array.append(gather['Insult'])

	#Get Random insult from insults_array
	length = len(insults_array)
	random_selection = random.uniform(0, int(length))
	final_tweet = insults_array[int(random_selection)]

	#Return the final_tweet
	return final_tweet

#Find out if tweet is compliment or insult	
def check_jobs():
	global headers

	#URL for Insults Database
	url = 'https://api.parse.com/1/classes/Jobs'

	jobs_array = []

	#Request (GET)
	request = urllib2.Request(url, data=None, headers=headers)
	results = urllib2.urlopen(request)
	data = results.read()
	jobs_information = json.loads(data)
	jobs = jobs_information['results']
	for gather in jobs:
		#Get a dict of reciever:type
		jobs_array.append( ( gather['receiver'], gather['type']) )

	return jobs_array
	pass

def get_compliment():
#Parse Restful API-Keys
	global headers

	#URL for Insults Database
	url = 'https://api.parse.com/1/classes/Compliments'

	#Array to hold insults
	compliment_array = []
	
	#Request (GET)
	request = urllib2.Request(url, data=None, headers=headers)
	results = urllib2.urlopen(request)
	data = results.read()
	compliment_information = json.loads(data)
	compliment = compliment_information['results']
	for gather in compliment:
		compliment_array.append(gather['compliment'])

	#Get Random insult from insults_array
	length = len(compliment_array)
	random_selection = random.uniform(0, int(length))
	final_tweet = compliment_array[int(random_selection)]

	#Return the final_tweet
	return final_tweet
	pass

def post_tweet(tweet_string, username):
	global tokens
	
	twitter = Twython(tokens['APP_KEY'], tokens['APP_SECRET'], tokens['OAUTH_TOKEN'], tokens['OAUTH_TOKEN_SECRET'])
	
	twitter_handle = username
	tweet = twitter_handle + ' ' + tweet_string
	
	#Make sure That the Tweet is less than 140 characters, if it is, repeat the process, (def not the best decision to go about this
	#But for time contraints it will work
	#If the Tweet is less than 140 characters, shoot the tweet off to the twitter sphere
	y = len(tweet)
	if y > 140:
		main()
	else:
		twitter.update_status(status=tweet)
	pass

def main():

	#Check The jobs list
	jobs_to_do = check_jobs()
	
	#Loop through existing jobs, which exists as twitter_name:type_of_tweet	
	for tuple_item in jobs_to_do:
		reciever = tuple_item[0]
		job_type = tuple_item[1]
		
		tweet_string = ''
		#If the tweet type is set to compliment
		if int(job_type) == 0:
			tweet_string = get_compliment()
		#If the tweet type is set to insult
		elif int(job_type) == 1:
			tweet_string = get_insult()
		
		#Tweet the results
		post_tweet(tweet_string, reciever)

if __name__ == '__main__':
	main()


