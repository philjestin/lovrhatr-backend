#!/usr/bin/env python

from twitter_talker import Twitter
from parse import parse

config = {
    'parse':{
        'app_id':'',
        'api_key':'',
    },
    'twitter':{
        'app_key':'',
        'app_secret':'',
        'oauth_token':'',
        'oauth_token_secret':'',
    },
}
#\
def main():
    # Create parse object
    parse_id  = config['parse']['app_id']
    parse_key = config['parse']['api_key']
    parse_object = parse(parse_id, parse_key)
    # Create twitter object
    tw_ak = config['twitter']['app_key']
    tw_as = config['twitter']['app_secret']
    tw_ot = config['twitter']['oauth_token']
    tw_ots = config['twitter']['oauth_token_secret']
    twitter = Twitter(tw_ak, tw_as, tw_ot, tw_ots)
    #\
    #\
    #Check The jobs list
    jobs_to_do = parse.get_jobs()
    #Loop through existing jobs, which exists as twitter_name:type_of_tweet	
    for current_job in jobs_to_do:
        reciever = current_job[0]
        job_type = int(current_job[1]) # Force the type to be an int
        #\
        tweet_string = '' # Here for backup
        #If the tweet type is set to compliment
        if job_type == 0:
        	tweet_string = parse_object.get_compliment()
        #If the tweet type is set to insult
        elif job_type == 1:
        	tweet_string = parse_object.get_insult()
        #\
        #Tweet the results
        twitter.post_tweet(reciever, tweet_string)
#\
if __name__ == '__main__':
	main()


