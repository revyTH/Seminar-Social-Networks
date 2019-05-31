#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
import time
import urllib2
from bs4 import BeautifulSoup
from progressbar import ProgressBar
from string import ascii_lowercase

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
BASE = 'http://www.billboard.com/artists/'

artists = set()  # to avoid duplicate artists. there are some
letters = [c for c in ascii_lowercase] + ['numbers']

pbar = ProgressBar(len(letters)).start()
progress = 0
for c in letters:
    progress += 1
    pbar.update(progress)
    # download page
    response = opener.open(BASE + c)
    page = response.read()
    soup = BeautifulSoup(page, 'lxml')
    # find section of the page with artists
    items = soup.find_all('span', class_='field-content')
    for item in items:
        # extract the artist name
        link = item.find('a')
        art = ' '.join(link.get_text().split())
        artists.add(art)
    # wait a second before next download
    time.sleep(1)
pbar.finish()

# write artist names to file
with io.open('artists.txt', 'w', encoding='ISO-8859-1') as fout:
    for art in sorted(artists):
        fout.write(art + '\n')
