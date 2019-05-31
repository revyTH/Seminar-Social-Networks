#!/usr/bin/python
# -*- coding: utf-8 -*-


import io
import time
import json
import requests
import base64
import urllib
import urllib2
import tweepy
from progressbar import ProgressBar



# ---------------------------------- # ---------------------------------- #
#   globals
# ---------------------------------- # ---------------------------------- #

TOKEN_ENDPOINT = "https://api.twitter.com/oauth2/token"
STATUS_CODE_OK = 200

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


CREDENTIALS = [
    [APP_KEY_3, APP_SECRET_3, ACCESS_TOKEN_3, ACCESS_TOKEN_SECRET_3],
    [APP_KEY_1, APP_SECRET_1, ACCESS_TOKEN_1, ACCESS_TOKEN_SECRET_1],
    [APP_KEY_2, APP_SECRET_2, ACCESS_TOKEN_2, ACCESS_TOKEN_SECRET_2],
    [APP_KEY_4, APP_SECRET_4, ACCESS_TOKEN_4, ACCESS_TOKEN_SECRET_4],
    [APP_KEY_5, APP_SECRET_5, ACCESS_TOKEN_5, ACCESS_TOKEN_SECRET_5],
    [APP_KEY_6, APP_SECRET_6, ACCESS_TOKEN_6, ACCESS_TOKEN_SECRET_6],
    [APP_KEY_7, APP_SECRET_7, ACCESS_TOKEN_7, ACCESS_TOKEN_SECRET_7],
    [APP_KEY_8, APP_SECRET_8, ACCESS_TOKEN_8, ACCESS_TOKEN_SECRET_8],
    [APP_KEY_9, APP_SECRET_9, ACCESS_TOKEN_9, ACCESS_TOKEN_SECRET_9],
]


















# client_credentials flow ---------------------------------
def get_bearer_token():
    # istruzioni per ottenere il token a questo link: https://dev.twitter.com/oauth/application-only
    credentials = APP_KEY_1 + ":" + APP_SECRET_1
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
    with open('result2.json', 'w') as fout:
        json.dump(response.json(), fout)
# --------------------------------------------------------------







def set_oauth_api(credential_index):
    # auth = tweepy.OAuthHandler(CREDENTIALS[credential_index][0], CREDENTIALS[credential_index][1], "oob")
    auth = tweepy.OAuthHandler(CREDENTIALS[credential_index][0], CREDENTIALS[credential_index][1])
    auth.access_token = CREDENTIALS[credential_index][2]
    auth.access_token_secret = CREDENTIALS[credential_index][3]
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    return api





# ---------------------------------- # ---------------------------------- #
#   main
# ---------------------------------- # ---------------------------------- #
if __name__ == '__main__':

    credential_index = 0
    # sleep time plus a little overhead
    sleep_time = ((15 / len(CREDENTIALS) * 60) / 180) + 0.05
    pbar = ProgressBar(56048).start()
    progress = 0
    threshold = 180
    count_requests = 0



    with io.open("artists.txt", "r", encoding='ISO-8859-1') as infile:
        api = set_oauth_api(credential_index)
        s = "id" + "\t" + "screen_name" + "\t" + "followers_count" + "\n"
        for line in infile:
            count_requests += 1
            progress += 1
            pbar.update(progress)
            query = line.strip()

            print count_requests, query

            try:
                # we take the first result as the most relevant
                result = api.search_users(query, 1)
                for entry in result:
                    s += str(entry["id"]) + "\t" + entry["screen_name"] + "\t" + str(entry["followers_count"]) + "\n"
            except:
                print ("Error")


            if (count_requests == threshold):
                count_requests = 0
                # next set of credentials
                credential_index = (credential_index + 1) % len(CREDENTIALS)
                api = set_oauth_api(credential_index)
                with open("twitter_artists.csv", "a") as fout:
                    fout.write(s)
                    s = ""

            time.sleep(sleep_time)



    pbar.finish()
    print "Job done!"





