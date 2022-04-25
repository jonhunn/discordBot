import os
from dotenv import load_dotenv
from plexapi.server import PlexServer

load_dotenv()
PLEX_URL = os.getenv('PLEX_URL')
PLEX_TOKEN = os.getenv('PLEX_TOKEN')

plex = PlexServer(PLEX_URL, PLEX_TOKEN)
beeMovies = plex.library.section("_Beemovie")

def findMovie(title):
    x = plex.search(title)
    return x


x = beeMovies.get("Star Worms II: Attack of the Pleasure Pods")
print(x.title)
print(x.summary)
#findMovie("The Fifth Element")

