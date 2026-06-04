from flask import Flask, render_template, request
import pickle
import os
from tmdb import get_movie_details

app = Flask(__name__)

# Load models
movies = pickle.load(open("saved_models/movies.pkl", "rb"))
similarity = pickle.load(open("saved_models/similarity.pkl", "rb"))

movie_list = movies["title"].values

# Hero Banner
FEATURED_MOVIE = {
    "title": "Interstellar",
    "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
    "poster": "https://image.tmdb.org/t/p/w1280/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg"
}

# Trending Section
TRENDING_MOVIES = [
    "Interstellar",
    "Inception",
    "Avatar",
    "Titanic",
    "The Dark Knight",
    "Avengers: Endgame"
]


def clean_movie_title(title):
    """
    Convert:
    Matrix, The -> The Matrix
    Beautiful Mind, A -> A Beautiful Mind
    """

    if ", The" in title:
        title = "The " + title.replace(", The", "").strip()

    if ", A" in title:
        title = "A " + title.replace(", A", "").strip()

    return title


def recommend(movie_name):
    try:

        if movie_name not in movie_list:
            return []

        idx = movies[movies["title"] == movie_name].index[0]

        distances = similarity[idx]

        movie_list_sorted = sorted(
            list(enumerate(distances)),
            key=lambda x: x[1],
            reverse=True
        )[1:6]  # 5 recommendations

        recommendations = []

        for movie in movie_list_sorted:

            title = movies.iloc[movie[0]].title

            year = "N/A"

            if "(" in title:
                year = title.split("(")[-1].replace(")", "")

            clean_title = title.split("(")[0].strip()
            clean_title = clean_movie_title(clean_title)

            details = get_movie_details(clean_title, year)

            recommendations.append({
                "title": title,
                "poster": details["poster"],
                "year": year,
                "rating": details["rating"],
                "overview": details["overview"][:150]
            })

        return recommendations

    except Exception as e:
        print("Recommendation Error:", e)
        return []


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    selected_movie = ""

    if request.method == "POST":

        selected_movie = request.form.get("movie")

        if selected_movie:
            recommendations = recommend(selected_movie)

    return render_template(
        "index.html",
        movies=movie_list,
        recommendations=recommendations,
        selected_movie=selected_movie,
        total_movies=len(movie_list),
        featured_movie=FEATURED_MOVIE,
        trending_movies=TRENDING_MOVIES
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )
    