#! /usr/bin/python

import urllib2
from BeautifulSoup import BeautifulSoup

url="https://spinitron.com/radio/playlist.php?station=radioboise&playlist=26363"
html=urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

#artist class: 'aw'
playlist_artists=[]
artists=soup.findAll("span", {"class": "aw"})
for artist in artists:
    artist_clean = artist.a.string
    playlist_artists.append(artist_clean)

print playlist_artists

#title class: 'sn'
# we also need to remove leading and trailing double quotes
titles=soup.findAll("span", {"class": "sn"})
playlist_titles=[]
for title in titles:
    title_clean = title.string[1:-1]
    playlist_titles.append(title_clean)

print playlist_titles

print len(artists)
print len(titles)
