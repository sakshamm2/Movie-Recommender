from turtle import title


def recommend(movie_name):

    try:
        print("Selected movie:", movie_name)

        idx = movie_dict.get(movie_name)

        if idx is None:
            print("Movie not found!")
            return []

        distances = similarity[idx]

        movie_list = sorted(
    list(enumerate(distances)),
    key=lambda x: x[1],
    reverse=True
)[1:11]

        recommendations = []

        for i in movie_list:

            full_title = movies.iloc[i[0]].title

            year = ""

            if "(" in full_title:
                year = full_title.split("(")[-1].replace(")", "")

            poster = fetch_poster(full_title)

            recommendations.append({
                "title": full_title,
                "year": year,
                "poster": poster
            })

        print("Recommendations generated:", len(recommendations))

        return recommendations[:5]

    except Exception as e:
        print("ERROR:", e)
        return []
    
print("Movies loaded:", len(movies))
print("Available example:", movies["title"].head(5).tolist())

year = ""

if "(" in title and ")" in title:
    year = title.split("(")[-1].replace(")", "")
  recommendations.append({
    "title": title,
    "year": title[-5:-1] if "(" in title else "N/A",
    "poster": poster
})