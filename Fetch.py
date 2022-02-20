from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

movies = ["ghostbusters", "power rangers", "rat race", "fateful findings"]


def getMovie(x):
    str = ""
    movie = ia.search_movie(x)
    id = movie[0].movieID
    movie = ia.get_movie(id)
    title = movie['title']
    str += "**" + title + "** \n"
    plot = movie['plot'][0]
    str += plot + "\n"
    poster = movie['full-size cover url']
    str += poster + "\n \n \n \n"
    return str


# for movie in movies:
#     print(getMovie(movie))

# # get a movie
# movie = ia.search_movie("ghostbusters")
# id = movie[0].movieID
# movie = ia.get_movie(id)
# #print(movie.keys())
# plot = movie['plot'][0]
# print(plot)
# print(movie.keys())
# cover = movie['full-size cover url']
# print(cover)