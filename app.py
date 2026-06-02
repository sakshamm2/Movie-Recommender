from flask import Flask, render_template, request
import pickle
from tmdb import fetch_poster

app = Flask(__name__)

movies = pickle.load(open("saved_models/movies.pkl", "rb"))
similarity = pickle.load(open("saved_models/similarity.pkl", "rb"))

movie_list = movies["title"].values


def recommend(movie_name):
    try:
        idx = movies[movies["title"] == movie_name].index[0]

        distances = similarity[idx]

        movie_list_sorted = sorted(
            list(enumerate(distances)),
            key=lambda x: x[1],
            reverse=True
        )[1:6]

        recommendations = []

        for movie in movie_list_sorted:
            title = movies.iloc[movie[0]].title

            year = "N/A"
            if "(" in title:
                year = title.split("(")[-1].replace(")", "")

            clean_title = title.split("(")[0].strip()

            poster_url = fetch_poster(clean_title)

            print("\nMovie:", title)
            print("Poster:", poster_url)
            print("-" * 50)

            recommendations.append({
                "title": title,
                "poster": poster_url,
                "year": year
            })

        return recommendations

    except Exception as e:
        print("ERROR:", e)
        return []


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    selected_movie = ""

    if request.method == "POST":
        selected_movie = request.form.get("movie")
        recommendations = recommend(selected_movie)

    return render_template(
        "index.html",
        movies=movie_list,
        recommendations=recommendations,
        selected_movie=selected_movie,
        total_movies=len(movie_list)
    )


if __name__ == "__main__":
    print("Starting Flask App...")
    app.run(debug=True)

    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)