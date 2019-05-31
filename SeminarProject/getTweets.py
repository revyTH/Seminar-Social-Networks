#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
import time
import json
import requests
import urllib
import urllib2
import base64
import tweepy
from progressbar import ProgressBar
from ttp import ttp
from application_only_auth import Client




# ---------------------------------- # ---------------------------------- #
#   globals
# ---------------------------------- # ---------------------------------- #

TOKEN_ENDPOINT = 'https://api.twitter.com/oauth2/token'
STATUS_CODE_OK = 200
STATUS_CODE_TOO_MANY_REQUESTS = 429

APP_KEY_1 = "vQkVvrzMdd3qoHUlfwuRHq0yt"
APP_SECRET_1 = "CsiuSgOc2mssobQp9NG5UDBkiFS5FWUD5UZ498RwtRd00gRguq"
ACCESS_TOKEN_1 = "3131580664-jJJeW8J8EyiysI3LMRKFxK7NcPtjU03tSDclQLw"
ACCESS_TOKEN_SECRET_1 = "lGnnvSQ5aWrxdpo9yT5a8iaGD8uKTapjVwvvHnfCXwMRp"

APP_KEY_2 = "PMpwtY2q2jhrXcStuB6DSqMon"
APP_SECRET_2 = "dFa7BZHJk6invBMj5oXaTHupgzzsLq8AWVH5rs6xoingZ8kR7f"
ACCESS_TOKEN_2 = "751751316171530240-e2jGWtBkj0JjWgqX1XQP23mXqEfjy7u"
ACCESS_TOKEN_SECRET_2 = "zbAr2gJkvZpE5GT2NxCAgMvpxbL76jBS3xjzWmBZoU0EC"

APP_KEY_3 = "GwjWhonSt1tkFRouH7RInoZbY"
APP_SECRET_3 = "hDLw3J0R8t3HZI3GlGa1Mn2marHm7RCiAMrwurqV0oa0lI5brH"
ACCESS_TOKEN_3 = "751753220024856576-tz5C7oPfb4X4FjHbzyaMkhe0tECxh1y"
ACCESS_TOKEN_SECRET_3 = "Blzp3BGgypO4iSG3UbdZAe9Y1vIrPcIO2iT1OUuh0BcB7"

APP_KEY_4 = "AMuexwVdlm2Gj2Iz1rtG8uoih"
APP_SECRET_4 = "ghVycWA7CwZpW4rKPkFU8rL3OSo5Z14pOAmFOjXBHlEPEGSfbr"
ACCESS_TOKEN_4 = "827508924-A1Hst1aaGmsXPH66d83uNwx7RMkmUJCMj5tNQ3aJ"
ACCESS_TOKEN_SECRET_4 = "rE2lD1PVfn8OubUBvnw1CgXBPwEE2KLqDmmLQuItVQgWL"

APP_KEY_5 = "gMSliBOrvWf2fT0WGJuggyjxo"
APP_SECRET_5 = "ZcornpJyaW3LsoJVzRXAVJ9ryc1KW7QA0SLynvbtjD5qaf7L5t"
ACCESS_TOKEN_5 = "751885856504414208-iYzgfZxUDj2hP0tIb3iprnN1cEdxa83"
ACCESS_TOKEN_SECRET_5 = "OK3hxtegJXzgALi8GrwpTjSDtu781vcVSdIjivAIw3w98"

APP_KEY_6 = "MLb3sn5qPLg0cvuzIsR8gYHj6"
APP_SECRET_6 = "23x1GzPgfUFPEnHLG2xpqGxPIKRFYlIymNO5sJte3p7QHsqCHo"
ACCESS_TOKEN_6 = "751887445889867777-HbV4b1EOJZFfHTsf0AiFitkzBQhtHs3"
ACCESS_TOKEN_SECRET_6 = "S9ps7pY5QycnCHQFNUGjeT6RUsphbob7cAgs5hxWGUCvg"

APP_KEY_7 = "pofui9SndvXLB1UKrhmrKc4oc"
APP_SECRET_7 = "7YWVnfL5viKNrxATLhTfxb36o81dsm83IFmVhzOAKiXs2lRrTV"
ACCESS_TOKEN_7 = "751889723648532480-IukNMQmTS6ZQ7A8BBWgjywyDkKgi02P"
ACCESS_TOKEN_SECRET_7 = "WIwtM3ggsYOBYwhQfX5dELLhBltB0IRtQiZbbdw8q9paA"

APP_KEY_8 = "5hX7GGgx0gNcSRmwaeXkIqt9L"
APP_SECRET_8 = "oj7YZkZDriGK9Dns41vXayZgO27LxALellxXW0dRp1XPHMNH0G"
ACCESS_TOKEN_8 = "751891213171695616-V0UqkB0VhZ5JCobWWYiTa24S8VBtlgW"
ACCESS_TOKEN_SECRET_8 = "6elUToWVX3cuwnLMNgbJsGnBitLTgdhUCLENXYy46WlZD"

APP_KEY_9 = "5vzaW8bYW2BzJ1WRFe2WGXiiE"
APP_SECRET_9 = "5IpiVXqaGhyQlfnlNEfGI3j0UYsXLNTKbF0UXBBVyEFGtBrsyp"
ACCESS_TOKEN_9 = "751893976953872384-CepV14fgTqHud2cxReFrR3TW4NZYY1b"
ACCESS_TOKEN_SECRET_9 = "YyzpNGcwVtFCUa5kornB8ugZaDR0wCas85k3llJqxwuNr"

APP_KEY_10 = "4PdKIRyQ0FijbMyLp8nkGhDHi"
APP_SECRET_10 = "hiJjRsWNAI0TsAP1ecm6MTrUyBn55qVtTuM7AdthYRIXPnRAp7"
ACCESS_TOKEN_10 = "752437121412136960-m47P8Xvf27Sn4VSMGDzSLVDe6egLGb9"
ACCESS_TOKEN_SECRET_10 = "xLJSnKZkORtbHmVd7lD4ZP7vlKBzUYZNihlx8GRto7S1e"

APP_KEY_11 = "Cdix5oykuLxA7X9zDO66JGGUe"
APP_SECRET_11 = "PxbtprNMfusUOTdk1pMlqvUPIYbCWpmV2ybMKY6yiPhzGCPdpr"
ACCESS_TOKEN_11 = "753148037774643200-ApBZ742kIQ6sBHllSgAJcUvHPfOMzWE"
ACCESS_TOKEN_SECRET_11 = "WmW6sTklCUuUuxaYkYgZ8WCsxjuwhSZ8oLXkvNPDxns6J"


CREDENTIALS = [
    [APP_KEY_1, APP_SECRET_1, ACCESS_TOKEN_1, ACCESS_TOKEN_SECRET_1],
    [APP_KEY_2, APP_SECRET_2, ACCESS_TOKEN_2, ACCESS_TOKEN_SECRET_2],
    [APP_KEY_3, APP_SECRET_3, ACCESS_TOKEN_3, ACCESS_TOKEN_SECRET_3],
    [APP_KEY_4, APP_SECRET_4, ACCESS_TOKEN_4, ACCESS_TOKEN_SECRET_4],
    [APP_KEY_5, APP_SECRET_5, ACCESS_TOKEN_5, ACCESS_TOKEN_SECRET_5],
    [APP_KEY_6, APP_SECRET_6, ACCESS_TOKEN_6, ACCESS_TOKEN_SECRET_6],
    [APP_KEY_7, APP_SECRET_7, ACCESS_TOKEN_7, ACCESS_TOKEN_SECRET_7],
    [APP_KEY_8, APP_SECRET_8, ACCESS_TOKEN_8, ACCESS_TOKEN_SECRET_8],
    [APP_KEY_9, APP_SECRET_9, ACCESS_TOKEN_9, ACCESS_TOKEN_SECRET_9],
    [APP_KEY_10, APP_SECRET_10, ACCESS_TOKEN_10, ACCESS_TOKEN_SECRET_10],
    [APP_KEY_11, APP_SECRET_11, ACCESS_TOKEN_11, ACCESS_TOKEN_SECRET_11],
]







# client_credentials flow ---------------------------------
def get_bearer_token(credential_index):
    # istruzioni per ottenere il token a questo link: https://dev.twitter.com/oauth/application-only
    credentials = CREDENTIALS[credential_index][0] + ":" + CREDENTIALS[credential_index][1]
    credentials = base64.urlsafe_b64encode(credentials)

    request_headers = {
        "Authorization": "Basic " + credentials,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }

    request_body = "grant_type=client_credentials"

    response = requests.post(TOKEN_ENDPOINT, headers=request_headers, data=request_body)

    if response.status_code == STATUS_CODE_OK:
        json_response = response.json()
        return json_response["access_token"]
    else:
        raise ValueError("Message: " + response.text + ".\nStatus_code: " + str(response.status_code))




def call_twitter_api(url, token):

    request_headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=request_headers)
    return response
# --------------------------------------------------------------





# class AppAuthHandler(tweepy.auth.AuthHandler):
#     TOKEN_URL = 'https://api.twitter.com/oauth2/token'
#
#     def __init__(self, consumer_key, consumer_secret):
#         token_credential = urllib.quote(consumer_key) + ':' + urllib.quote(consumer_secret)
#         credential = base64.b64encode(token_credential)
#
#         value = {'grant_type': 'client_credentials'}
#         data = urllib.urlencode(value)
#         req = urllib2.Request(self.TOKEN_URL)
#         req.add_header('Authorization', 'Basic ' + credential)
#         req.add_header('Content-Type', 'application/x-www-form-urlencoded;charset=UTF-8')
#
#         response = urllib2.urlopen(req, data)
#         json_response = json.loads(response.read())
#         self._access_token = json_response['access_token']
#
#     def apply_auth(self, url, method, headers, parameters):
#         headers['Authorization'] = 'Bearer ' + self._access_token


class AppAuthHandler(tweepy.auth.AuthHandler):
    TOKEN_URL='https://api.twitter.com/oauth2/token'

    def __init__(self,consumer_key,consumer_secret):
        token_credential = '{}:{}'.format(*map(urllib.quote, [consumer_key, consumer_secret]))
        credential = base64.b64encode(token_credential)
        value = {'grant_type': 'client_credentials'}
        data = urllib.urlencode(value)
        req = urllib2.Request(self.TOKEN_URL)
        req.add_header('Authorization', 'Basic {}'.format(credential))
        req.add_header('Content-Type', 'application/x-www-form-urlencoded;charset=UTF-8')
        response=urllib2.urlopen(req, data)
        json_response=json.loads(response.read())
        self._access_token=json_response['access_token']

    def apply_auth(self,url,method,headers,parameters):
        headers['Authorization'] = 'Bearer {}'.format(self._access_token)



def set_oauth_api_app_only(credential_index):

    api = tweepy.API(auth)
    return api




def set_oauth_api(credential_index):
    auth = tweepy.auth.OAuthHandler(CREDENTIALS[credential_index][0],
                                    CREDENTIALS[credential_index][1], 'oob')
    auth.set_access_token(CREDENTIALS[credential_index][2],
                          CREDENTIALS[credential_index][3])
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    return api


# ---------------------------------- # ---------------------------------- #
#   main
# ---------------------------------- # ---------------------------------- #
def main():
    credential_index = 0
    pbar = ProgressBar(56306).start()
    progress = 0
    page_limit = 200
    followers_threshold = 10000
    parser = ttp.Parser()

    with io.open('twitter_artists.csv', 'r', encoding='ISO-8859-1') as infile:
        numberofartists = sum((1 for line in infile)) - 1

    with io.open('twitter_artists.csv', 'r', encoding='ISO-8859-1') as infile:
        print 'Using credential: ' + str(credential_index)
        # api = set_oauth_api(credential_index)
        api = set_oauth_api_app_only(credential_index)


        for line in infile:
            progress += 1
            print str(progress) + '/' + str(numberofartists)
            line = infile.readline() #skip header
            tokens = line.split("\t")
            id = tokens[0]
            followers_count = tokens[2]
            if followers_count < followers_threshold:
                print "Artist skipped"
                continue


            list_data = []

            # pagination loop
            for i in xrange(1,3):

                while True:
                    try:
                        result = api.user_timeline(id, page=i, count=page_limit)
                        print '\t', id, i, len(result)
                    except tweepy.error.RateLimitError:
                        # next set of credentials
                        credential_index = ((credential_index + 1) %
                                            len(CREDENTIALS))
                        print 'Rate Limit.'
                        print 'Using credential: ' + str(credential_index)
                        api = set_oauth_api_app_only(credential_index)
                        time.sleep(1)
                    except Exception as ex:
                        print(str(type(ex)) + ':' + str(ex))
                        time.sleep(1)

                    if len(result) == 0:
                        break

                    for tweet in result:
                        tweet_id = tweet['id']
                        list_link = parser.parse(tweet["text"]).urls

                        # we consider only tweets with at least one link
                        if len(list_link) > 0:

                            # get retweets for this tweet
                            while True:
                                try:
                                    retweets_str = get_retweets(api, tweet_id, id)
                                    break
                                except tweepy.error.RateLimitError:
                                    # next set of credentials
                                    credential_index = ((credential_index + 1) %
                                                        len(CREDENTIALS))
                                    print 'Rate Limit.'
                                    print 'Using credential: ' + str(credential_index)
                                    api = set_oauth_api(credential_index)


                            list_data.append((tweet_id, list_link[0], retweets_str))






                    # break del while True
                    break

                if len(result) == 0:
                    break

            if len(list_data) > 0:
                with io.open("tweets/" + id + ".csv", "wb") as outfile:
                    s = "tweet_id" + "\t" + "link" + "\t" + "retweets" + "\n"
                    for tuple in list_data:
                        s += str(tuple[0]) + "\t" + tuple[1] + "\t" + tuple[2] + "\n"
                    try:
                        outfile.write(s)
                    except Exception as ex:
                        print(str(type(ex)) + ':' + str(ex))
                        time.sleep(1)



    print 'Job done!'







def get_retweets(api, tweet_id, id):
    retweets = api.retweets(tweet_id)
    s = ""
    for retweet in retweets:
        s += str(retweet["user"]["id"]) + ":" + str(retweet["id"])
        s += "|"

    if len(s) > 0:
        s = s[:-1]

    print "\t\t" + "retweets: " + s


    return s




if __name__ == '__main__':
    # main()

    # auth = AppAuthHandler(CREDENTIALS[0][0], CREDENTIALS[0][1])
    # api = tweepy.API(auth)
    #
    # result = api.retweets("711265829539581954")
    # print result


    # client = Client(CREDENTIALS[0][0], CREDENTIALS[0][1])
    # result = client.request("https://api.twitter.com/1.1/users/lookup.json?screen_name=pinkfloyd")
    # status = client.rate_limit_status()
    # print status['resources']['search']


    token = get_bearer_token(10)
    for i in xrange(62):
        response = call_twitter_api("https://api.twitter.com/1.1/statuses/user_timeline.json?id=18946688", token)
        if response.status_code == STATUS_CODE_TOO_MANY_REQUESTS:
            print "RATE LIMIT"
    exit()
