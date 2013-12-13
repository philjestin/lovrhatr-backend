#!/usr/bin/env python

# Imports
import urllib2
import json
import random
from time import ctime

# G Vars
rnd0 = random

# Class
class parse:
    #\
    app_id  = ""
    app_key = ""
    #\
    def get_jobs(self):
        return self.__get_something_from_parse("Jobs")
    #\
    def get_compliment(self):
        return self.__basic_pull_one_item("Compliments", "Compliment")
    #\
    def get_insult(self):
        return self.__basic_pull_one_item("Insults", "Insult")
    #\
    def __basic_pull_one_item(self, class_name, res_name):
        data = self.__get_something_from_parse(class_name)
        res_list = []
        for current_item in data:
            toAppend = None
            if class_name == "Jobs":
                toAppend = (current_item['receiver'], current_item['type'])
            else:
                toAppend = current_item[res_name]
            res_list.append(toAppend)
        if class_name != "Jobs":
            choice = res_list[(rnd0.randomrange(0, len(res_list)))] # Should pick one random entry
        return choice
    #\
    def __get_something_from_parse(self, what_to_get):
        data = self.__talk_to_parse(what_to_get)
        return data['results']
    #\
    def __talk_to_parse(self, class_name):
        headers = {'X-Parse-Application-Id':self.app_id,'X-Parse-REST-API-Key':self.app_key}
        url = "https://api.parse.com/1/classes/%s" % class_name
        request = urllib2.Request(path, data = None, headers = headers) # Build a request to talk to parse
        w0 = urllib2.urlopen(request) # Build a link to parse
        data = w0.read() # Read data from the built link
        return json.loads(data) # Should return a dict of variables from parse
    #\
    def __init__(self, app_id, api_key):
        global rnd0
        rnd0.seed(ctime())
        self.app_id = app_id
        self.api_key = api_key
    #\

if __name__ == "__main__":
    print "You can only import this python lib."