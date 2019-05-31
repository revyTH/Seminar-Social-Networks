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
from collections import defaultdict


import networkx as nx
import matplotlib.pyplot as plt







def main():

    G = nx.DiGraph()
    directory = os.listdir('tweets_new/')

    for userfile in directory:
        user_id = userfile[:-4]
        numeratori = defaultdict(int)
        denominatore = 0
        with io.open('tweets_new/' + userfile) as filein:
            filein.readline()
            for line in filein:
                denominatore += 1
                tokens = line.split('\t')
                tweet_id = tokens[0]
                link = tokens[1]
                retweets = tokens[2].split(' ')
                for retweet in retweets:
                    retwitter_id = retweet.split(':')[0]
                    numeratori[retwitter_id] += 1

        for k in numeratori:

            G.add_edge(user_id, k, weight=float(numeratori[k] / denominatore))


    print len(G.nodes())
    print len(G.edges())

    pos = nx.spectral_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=10, alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=0.1, alpha=0.8)
    plt.show()



if __name__ == '__main__':
    main()