import requests

API_KEY = "00ae7a5a0781e8dd24365ea2938b5e96"

def fetch_poster(movie_name):

    try:

        url = "https://api.themoviedb.org/3/search/movie"

        response = requests.get(
            url,
            params={
                "api_key": API_KEY,
                "query": movie_name
            },
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        data = response.json()

        if data.get("results"):

            poster_path = data["results"][0].get("poster_path")

            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"

        return "https://via.placeholder.com/300x450?text=No+Poster"

    except Exception as e:
        print("TMDB ERROR:", e)
        return "https://via.placeholder.com/300x450?text=No+Poster"