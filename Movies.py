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

#get 5 movies from the movie list
def movieNight():
    m = getMovies()
    rm = random.sample(m, 5)
    return rm

#return the list to the bot
def printList():
    rm = movieNight()
    print(rm)
    str = []

    #sets the voting emoji, list at the top
    numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]

    for r in rm:
        str.append(f.getMovie(r)[1])

    #iterates through and appends movies to the end of the list
    #to be called in "Bot"
    def getTitles():
        temp = []
        for i in range(5):
            temp.append(numbers[i] + "  " + rm[i])
        return temp
    t = getTitles()
    str.append(t)

    return str