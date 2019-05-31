#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
import os
import time
import json
import requests
import urllib
import urllib2
import base64
from progressbar import ProgressBar
from ttp import ttp
from datetime import datetime
# import datetime
import tweepy
import pytz



# ---------------------------------- # ---------------------------------- #
#   globals
# ---------------------------------- # ---------------------------------- #

MAX_DATE = datetime(2016, 6, 29).replace(tzinfo=None)
SINCE_DATE = datetime(2016, 3, 22).replace(tzinfo=None)

TOKEN_ENDPOINT = 'https://api.twitter.com/oauth2/token'
STATUS_CODE_OK = 200
STATUS_CODE_NOT_AUTHORIZED = 401
STATUS_CODE_NOT_FOUND = 404
STATUS_CODE_TOO_MANY_REQUESTS = 429
TWEETS_URL = "https://api.twitter.com/1.1/statuses/user_timeline.json"
RETWEETS_URL = "https://api.twitter.com/1.1/statuses/retweets/"


FOLLOWERS_THRESHOLD = 10000



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

APP_KEY_12 = "Q0ZJ22syB2n6WU5Tuf0Lhkpr3"
APP_SECRET_12 = "7j54UCHx6feLTyAfzOqtnn4uL7dyjkqHfJbs4oNhgJ2aV0bpyD"

APP_KEY_13 = "h9k3wqrAXWtjXPPvEJHXvWUqq"
APP_SECRET_13 = "4xM0yZoGg15ufxDFJlpQto2HN0Od2Do3QpLzrqJsWYuiMz8FHz"

APP_KEY_14 = "qv8HjrTqWcBiMs9QrsG2nBlfp"
APP_SECRET_14 = "ehBL45SBLhC7vy3bSBTXCbeQ2WlH84n6mHtgGDgzf7B4r0tPXD"

APP_KEY_15 = "T11cw37GtURv9E7KWJCxDYsXe"
APP_SECRET_15 = "2E1sG39OyTt9dua4UfjbWpRJ2HzhbsduY4ftIllJpz4pRGpdDx"

APP_KEY_16 = "WDu0u9Fo3bWq9zskAa18N5xw5"
APP_SECRET_16 = "pq8VEkt3KkfOc6yglGZMkV8pNbNc7BSaIVPwZNU7HmVEMTCaRc"

APP_KEY_17 = "i2qUnyrXdig08duOnUw5wRk1L"
APP_SECRET_17 = "xTxPvjnZ7eQf4hkOfOlsFz2XA0CI9SmvIwu0MV1HNgX86LPxgr"

APP_KEY_18 = "aQVaBFeZ4iGumBtMfwIAFMsYO"
APP_SECRET_18 = "UqBITIBNgvm38zNZAl0wE26CdS5PA65NsJRsnM4k3BnQrh31lm"

APP_KEY_19 = "OR9YwgsPhXNl7vFUtGYwEVjQS"
APP_SECRET_19 = "vCBHT7MkhX7Ww1hlQ38C73SgHFiRRzggD0wtcDTnGU1T2aZ9Be"

APP_KEY_20 = "x05jGKUwu6HusqQN00RecBrl1"
APP_SECRET_20 = "mr6ur3j19KcQ2CcTZmTPtCu6XMIyVu4c0emNGu5AMyLLpR1z1Z"

APP_KEY_21 = "1ePWn7Qwh37VRyoNohgkkqmDj"
APP_SECRET_21 = "KXl1KCjB5ck7NY2O3ZTlBTYxGBg24NxX9J9VYN8PGa481Sx2nY"

APP_KEY_22 = "ttJAoR6qe08gRHbpOohAmqe0F"
APP_SECRET_22 = "KuNMOPLVKWBOEMi9EUNUPEcSgweNIKPGRQWgT47Tya6UHM84iV"

APP_KEY_23 = "ysQS1cWFuOYog5VFcM3orBolI"
APP_SECRET_23 = "qIaYGbCtYjAjmIwwZK9CNd41K4QJKKQ7NftKaR91yK5nzfho9y"

APP_KEY_24 = "GCIJKOynNZ1CyEc9JXZO7l89z"
APP_SECRET_24 = "MLtotGUoHKxTVtJuchWRC7rbCyQiE3ydh3UMf1dUFWG2TpawA5"

APP_KEY_25 = "DDpuuTS08sQNoUiJlRswOKAI4"
APP_SECRET_25 = "BnOO0rb4MpyIdviTRz1SfEn4FtdVLq1pqZYDMYckeRQkAsGxZT"

APP_KEY_26 = "jHaTyuEh81SZHTsFn1Fm0rw0K"
APP_SECRET_26 = "U3petlUYcsDbIv86ZG9faeWotP0wpOfXwet9r6fthy5q88Uyb8"

APP_KEY_27 = "Xul1tE2oq6I8HIA0c4YkVTEYf"
APP_SECRET_27 = "I9ilz5w3AamVBHmpETvC7eYyZKfmmZxixtJAJO3CW8OD3qeyDk"

APP_KEY_28 = "ifkrbOdM8E08Hcvb9LCsHiaGS"
APP_SECRET_28 = "AWpZ9G3bfgFEZ1nTzJ1QWSd7G2s3k1wltCwXCsjlnS5yz1WxIk"

APP_KEY_29 = "0mqJWhOYQJBoFq5b7XqqxLib6"
APP_SECRET_29 = "Wm77FjpmgHhDzKhNjwTUf2IiEBVm9rOeoaVp9SkXpR0BfMaimv"

APP_KEY_30 = "ak6Ndwp0xvNdOkm1kqYAv1i7a"
APP_SECRET_30 = "2OU3NEq1msdNbfLzMiCgnOE5yRJjeAiCCdLUDZX57GQPt6WHF1"

APP_KEY_31 = "ypzti8EpTmKTLeazgpvrvm069"
APP_SECRET_31 = "tE5cqHd5pfcdivi331x30nBOcuY3CT7LRNOtGQAISm7Vxudotv"

APP_KEY_32 = "K1jfwHmeMVEtGqg7n5MI1BZhr"
APP_SECRET_32 = "OPALBzjfIJrXf0iTSAoJIoAyfKn3Wd7x8mp9LVOYgthtKkmtWl"

APP_KEY_33 = "gETIw1OOoqRSRZckVXNnA9iN6"
APP_SECRET_33 = "cONN8iHYfF1v55N6xzyt7rzHQ8BdwIlTWyZadqrpamE6pdXTqn"

APP_KEY_34 = "zhlhpx6K6WkHjh43ExdbYKtRu"
APP_SECRET_34 = "Et3w423unlnnLtYPzg8ZkisJ3Xa31wiMcBIUnKvq1O35Jea9P3"

APP_KEY_35 = "XEAWKIhv7k5WfoXvLiOvAltX1"
APP_SECRET_35 = "hSTAHR972cfZ3p0VHfI585d6mdPfKcT9gHrtULmFlnYUWHeZPl"

APP_KEY_36 = "I4U5oMVdGArr9TmzT65kPw4Tc"
APP_SECRET_36 = "0FX1inGUlcwS3FC4Zp4G1eWTbc4FoufXHkITBG6Wm3P1m6pwNN"

APP_KEY_37 = "YHu9tV5AOvP6rcl4rul6BJhs6"
APP_SECRET_37 = "32e8yLVR30rMRZJw2hM2KYnh5nf4gy4ZwydafMOc7abr7UpYAt"

APP_KEY_38 = "0OphVNbFlLHKJfs9sAKd5Lyuk"
APP_SECRET_38 = "mLq2VimcucgVuQ92uHVJysypteqLkNtrbQ3ItnyykCBSklK8lv"

APP_KEY_39 = "Q5LLDSWtvwHosMVsBvQdp6Yqt"
APP_SECRET_39 = "kNfdZXZ3hr12jMvNpSYG7rA6CybHqpzaHq9BllQNw4aUYac7Rp"

APP_KEY_40 = "CcAGABXcTiNLKvkJQRBM4W3A0"
APP_SECRET_40 = "lPTdly5zSblcsApVGh2lsiYCKhDFzDgrIvCK9HAUrowADuIS3m"

APP_KEY_41 = "I1K604yzzdyo77w1qelBFr27L"
APP_SECRET_41 = "mDWgasiqIsmfyt4dpeK0kGIYQnTfT3aJjbiLqcNH5fLnh88mtf"

APP_KEY_42 = "VK5kypNGdXf3X75dKEZbV5kI8"
APP_SECRET_42 = "EbswoI3WQ3kXQhygl5uHOUObiS65qmhsATKNIdSjTw9Cg4wbYI"

APP_KEY_43 = "ZsECRcnv6i3x04tDsJSDRwsg5"
APP_SECRET_43 = "sNngvfk3UO2zKClfUNO9zjA4jRNwQggtNbaglluBZCR6JYIi38"

APP_KEY_44 = "IA5RLZTJpZ9aRq2Z97rVPv6DJ"
APP_SECRET_44 = "ZqQtB89HrfsOzuzW4vXxACzm5MhUpvwtiSpWnTblfkN80ZXxKy"



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

    [APP_KEY_12, APP_SECRET_12],
    [APP_KEY_13, APP_SECRET_13],
    [APP_KEY_14, APP_SECRET_14],
    [APP_KEY_15, APP_SECRET_15],
    [APP_KEY_16, APP_SECRET_16],
    [APP_KEY_17, APP_SECRET_17],
    [APP_KEY_18, APP_SECRET_18],
    [APP_KEY_19, APP_SECRET_19],
    [APP_KEY_20, APP_SECRET_20],
    [APP_KEY_21, APP_SECRET_21],
    [APP_KEY_22, APP_SECRET_22],
    [APP_KEY_23, APP_SECRET_23],
    [APP_KEY_24, APP_SECRET_24],
    [APP_KEY_25, APP_SECRET_25],
    [APP_KEY_26, APP_SECRET_26],
    [APP_KEY_27, APP_SECRET_27],
    [APP_KEY_28, APP_SECRET_28],
    [APP_KEY_29, APP_SECRET_29],
    [APP_KEY_30, APP_SECRET_30],
    [APP_KEY_31, APP_SECRET_31],
    [APP_KEY_32, APP_SECRET_32],
    [APP_KEY_33, APP_SECRET_33],
    [APP_KEY_34, APP_SECRET_34],
    [APP_KEY_35, APP_SECRET_35],
    [APP_KEY_36, APP_SECRET_36],
    [APP_KEY_37, APP_SECRET_37],
    [APP_KEY_38, APP_SECRET_38],
    [APP_KEY_39, APP_SECRET_39],
    [APP_KEY_40, APP_SECRET_40],
    [APP_KEY_41, APP_SECRET_41],
    [APP_KEY_42, APP_SECRET_42],
    [APP_KEY_43, APP_SECRET_43],
    [APP_KEY_44, APP_SECRET_44]
]


CREDENTIAL_INDEX = 0
CURRENT_TOKEN = ""




# client_credentials flow ---------------------------------
def get_bearer_token(credential_index):

	while True:
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
	    	CREDENTIAL_INDEX = ((CREDENTIAL_INDEX + 1) % len(CREDENTIALS))
	    	time.sleep(5)







def call_twitter_api(url):

    global CURRENT_TOKEN
    global CREDENTIAL_INDEX

    if len(CURRENT_TOKEN) == 0:
        CURRENT_TOKEN = get_bearer_token(CREDENTIAL_INDEX)

    request_headers = {
        "Authorization": "Bearer " + CURRENT_TOKEN,
        "Accept": "application/json"
    }

    while True:
    	# time.sleep(0.1)
        response = requests.get(url, headers=request_headers)

        if response.status_code == STATUS_CODE_OK or response.status_code == STATUS_CODE_NOT_FOUND or response.status_code == STATUS_CODE_NOT_AUTHORIZED:
            break

        elif response.status_code == STATUS_CODE_TOO_MANY_REQUESTS:
            CREDENTIAL_INDEX = ((CREDENTIAL_INDEX + 1) % len(CREDENTIALS))
            print "\n\nRate Limit: switched to credentials "  + str(CREDENTIAL_INDEX) + "\n\n"
            CURRENT_TOKEN = get_bearer_token(CREDENTIAL_INDEX)
            request_headers["Authorization"] = "Bearer " + CURRENT_TOKEN

        else:
        	print "\n\n WHO ARE YOU? \n\n"
        	time.sleep(5)


    return response
# --------------------------------------------------------------







# ---------------------------------- # ---------------------------------- #
#   main
# ---------------------------------- # ---------------------------------- #
def main():

    global CURRENT_TOKEN
    global CREDENTIAL_INDEX

    # initialize access token
    CURRENT_TOKEN = get_bearer_token(CREDENTIAL_INDEX)





    parser = ttp.Parser()

    with io.open('twitter_artists.csv', 'r', encoding='ISO-8859-1') as infile:
        numberofartists = sum((1 for line in infile)) - 1

    with io.open('twitter_artists.csv', 'r', encoding='ISO-8859-1') as infile:
        print 'Using credential: ' + str(CREDENTIAL_INDEX)

        already_processed_lines = 0

        # temporary file to store the number of processed lines
        if os.path.isfile("already_processed.txt"):
            with open("already_processed.txt", "r") as temp_in_file:
                already_processed_lines = int(temp_in_file.readline().strip())
        else:
            with open("already_processed.txt", "w") as temp_out_file:
                temp_out_file.write("0")


        if already_processed_lines > 0:
            progress = already_processed_lines - 2
        else:
            progress = 0

        infile.readline() #skip header


        # skip already processed lines
        if already_processed_lines > 0:
            for i in xrange(already_processed_lines - 1):
            	infile.readline()


        for line in infile:

            progress += 1
            print str(progress) + '/' + str(numberofartists)

            # update the temporary file
            with open("already_processed.txt", "w") as temp_out_file:
                temp_out_file.write(str(progress))


            tokens = line.split("\t")

            try:
                id = tokens[0]
                followers_count = int(tokens[2])

                if followers_count < FOLLOWERS_THRESHOLD:
                    print "\n\n Too few followers: artist skipped \n\n"
                    continue
                else:
                    print "\n\nFOLLOWERS COUNT = " + str(followers_count) + "\n\n"
            except Exception as ex:
                print ex
                continue;



            list_data = []


            url = TWEETS_URL + "?id=" + id + "&count=200"
            # get tweets for the current user(id)
            response = call_twitter_api(url)

            if response.status_code == STATUS_CODE_NOT_AUTHORIZED or response.status_code == STATUS_CODE_NOT_FOUND:
                continue

            jsonTweets = json.loads(response.content)

            for tweet in jsonTweets:
                tweet_id = tweet['id']
                list_link = parser.parse(tweet["text"]).urls
                tweet_date = datetime.strptime(tweet["created_at"], '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=None)

                if tweet_date >= MAX_DATE or tweet_date <= SINCE_DATE:
                    print "Tweet out of time window: ", tweet_date.strftime('%Y-%m-%d')
                    continue



                # we consider only tweets with at least a link
                url = RETWEETS_URL + str(tweet_id) + ".json"
                retweets_str = ""
                if len(list_link) > 0:



                    # get retweets for the current tweet(tweet_id)
                    response = call_twitter_api(url)
                    jsonRetweets = json.loads(response.content)


                    for retweet in jsonRetweets:
                        retweets_str += str(retweet["user"]["id"]) + ":" + str(retweet["id"])
                        retweets_str += " "

                    retweets_str = retweets_str.strip()

                    print "\t" + str(tweet_id) + "\t" + retweets_str


                    list_data.append((tweet_id, list_link[0], retweets_str))


            # if the user didn't post any tweet with a link, skip
            if len(list_data) == 0:
                continue


            with io.open("tweets_new/" + id + ".csv", "wb") as outfile:
                s = "tweet_id" + "\t" + "link" + "\t" + "retweets" + "\n"
                for tuple in list_data:
                    s += str(tuple[0]) + "\t" + tuple[1] + "\t" + tuple[2] + "\n"
                try:
                    outfile.write(s)
                except Exception as ex:
                    print(str(type(ex)) + ':' + str(ex))
                    time.sleep(1)










def prendiamo_time_bound():
    # url = "https://api.twitter.com/1.1/statuses/user_timeline.json" + "&screen_name=fattoquotidiano&count=1"
    # response = call_twitter_api(url)
    # jsonTweets = json.loads(response.content)







    auth = tweepy.auth.OAuthHandler(CREDENTIALS[0][0],
                                    CREDENTIALS[0][1], 'oob')
    auth.set_access_token(CREDENTIALS[0][2],
                          CREDENTIALS[0][3])
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    result = api.user_timeline(screen_name="fattoquotidiano", count=1)


    # d = datetime.strptime(result[0]["created_at"],'%a %b %d %H:%M:%S %z %Y');
    d = datetime.strptime(result[0]["created_at"],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)
    print d.strftime('%Y-%m-%d')

    now = datetime.now()

    print now.replace(tzinfo=None) > d.replace(tzinfo=None)













if __name__ == '__main__':

	try:
		main()
	except:
		time.sleep(10)
		main()

    # prendiamo_time_bound()




