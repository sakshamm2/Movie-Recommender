# test_tmdb.py

from tmdb import fetch_poster

movies = [
    "Avatar",
    "Inception",
    "Interstellar",
    "Titanic",
    "Heat"
]

for movie in movies:
    print(movie)
    print(fetch_poster(movie))
    print("-" * 50)