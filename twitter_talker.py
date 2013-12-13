#!/usr/bin/env python

# Imports
from twython import Twython

# G Vars

# Class
class Twitter:
    talker     = None # Holder for the Twython object.
    error_code = 0
    #\
    def post_tweet(self, username, message):
        tweet = "%s - %s" % (username, message)
        if len(tweet) > 140:
            self.error_code = 100
            return None
        self.talker.update_status(status=tweet)
    #\
    def __init__(self, app_key, app_secret, oauth_token, oauth_token_secret:
        self.talker = Twython(app_keym app_secret, oauth_token, oauth_token_secret)
    #\

if __name__ == "__main__":
    print "You can only import this lib."