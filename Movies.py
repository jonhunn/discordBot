import random
import csv
import Fetch as f

#get list of movies from csv
def getMovies():
    movies = "databases/movies.csv"
    theList = []
    with open(movies, 'r') as csvfile:
        movieList = csv.reader(csvfile)
        for item in movieList:
            theList += item

    return(theList)


#return the list to the bot
def printList():
    m = getMovies()
    #get random list of movies
    rm = random.sample(m, 5)
    str = ""
    #sets the voting emoji, list at the top
    numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]
    for i in range(5):
        str += numbers[i] + "  " + rm[i] +  "\n"

    for r in rm:
        str+= f.getMovie(r)

    return str