import requests
import time

API_KEY = "00ae7a5a0781e8dd24365ea2938b5e96"

PLACEHOLDER = "https://via.placeholder.com/300x450?text=No+Poster"


def get_movie_details(movie_name, year=None):

    try:

        time.sleep(0.5)

        if ", The" in movie_name:
            movie_name = "The " + movie_name.replace(", The", "").strip()

        if ", A" in movie_name:
            movie_name = "A " + movie_name.replace(", A", "").strip()

        params = {
            "api_key": API_KEY,
            "query": movie_name
        }

        if year and year != "N/A":
            params["year"] = year

        response = requests.get(
            "https://api.themoviedb.org/3/search/movie",
            params=params,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        results = data.get("results", [])

        if not results:
            return {
                "poster": PLACEHOLDER,
                "rating": "N/A",
                "overview": "No description available."
            }

        movie = results[0]

        poster = PLACEHOLDER

        if movie.get("poster_path"):
            poster = (
                f"https://image.tmdb.org/t/p/w780"
                f"{movie['poster_path']}"
            )

        return {
            "poster": poster,
            "rating": round(movie.get("vote_average", 0), 1),
            "overview": movie.get(
                "overview",
                "No description available."
            )
        }

    except Exception as e:

        print("TMDB ERROR:", e)

        return {
            "poster": PLACEHOLDER,
            "rating": "N/A",
            "overview": "No description available."
        }