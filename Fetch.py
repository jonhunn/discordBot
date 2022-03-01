from imdb import Cinemagoer

ia = Cinemagoer()


#fetches movie and creates a string of movie title, plot, and poster 
def getMovie(x):
    i = 0
    numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]
    str = ""
    movie = ia.search_movie(x)
    id = movie[0].movieID
    movie = ia.get_movie(id)
    title = movie['title']
    str += "**" + title + "** \n"
    plot = movie['plot'][0]
    str += plot + "\n"
    poster = movie['full-size cover url']
    str += poster + "\n \n"
    return str