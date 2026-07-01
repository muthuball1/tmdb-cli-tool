
import argparse
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.themoviedb.org/3/movie/{}?language=en-US&page=1"
VALID_TYPES = ["upcoming", "top_rated", "popular", "now_playing"]
API_KEY = os.getenv("API_KEY")


def get_movie(type):
    if type not in VALID_TYPES:
        print("Invalid type")
        return
    url = BASE_URL.format(type)
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    response = requests.get(url, headers=headers)
    return response.json()

#print movies in a readable format
def display_movie(movie):
    if not data or "results" not in data:
        print("No movies found")
        return
    for movie in data["results"]:
        print(f"Title: {movie['title']}")
        print(f"Released: {movie['release_date']}")
        print(f"Rating: {movie['vote_average']}")
        print(f"Overview: {movie['overview']}")
        print("-------------------------")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TMDB CLI tool")
    parser.add_argument("-t", "--type", help="type of movie")
    args = parser.parse_args()
    data = get_movie(args.type)
    display_movie(data)