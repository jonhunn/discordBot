import random
import csv

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
    print(m)
    rm = random.sample(m, 3)
    str = ""
    numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]
    for i in range(3):
        str += numbers[i] + "  " + rm[i] +  "\n"
    return str