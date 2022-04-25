import csv
import pandas

def getMovies():
    movies = "databases/movies.csv"
    theList = []
    with open(movies, 'r') as csvfile:
        movieList = csv.reader(csvfile)
        for item in movieList:
            theList += item

    return(theList)


print(getMovies())