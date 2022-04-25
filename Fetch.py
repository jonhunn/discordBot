from __future__ import with_statement                                                        
from imdb import Cinemagoer
import contextlib
try:
    from urllib.parse import urlencode          
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys

ia = Cinemagoer()


#fetches movie and creates a string of movie title, plot, and poster 
def getMovie(x):
    str = ""
    l = []
    movie = ia.search_movie(x)
    id = movie[0].movieID
    movie = ia.get_movie(id)
    title = movie['title']
    l.append(title)
    str += "**" + title + "** \n"
    plot = movie['plot'][0]
    str += plot + "\n"
    poster = make_tiny(movie['full-size cover url'])
    str += poster + "\n \n"
    l.append(str)
    return l


#create tinyurl for images
def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))   
    with contextlib.closing(urlopen(request_url)) as response:                      
        return response.read().decode('utf-8 ')