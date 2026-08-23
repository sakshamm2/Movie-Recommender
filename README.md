# Movie Recommendation System

A movie recommendation system built using **Machine Learning, Flask, and the TMDB API**. The application recommends similar movies using content-based filtering and displays movie posters, ratings, and other details through a streaming-platform-style web interface.

## Features

* Content-Based Movie Recommendations
* Machine Learning Powered Recommendation Engine
* Dynamic Movie Posters using the TMDB API
* Movie Ratings and Details Integration
* Netflix-Inspired User Interface
* Flask Web Application
* Responsive Design

## Tech Stack

* Python
* Flask
* Pandas
* Scikit-Learn
* HTML5
* CSS3
* JavaScript
* TMDB API
* Git & GitHub

## Project Structure

```text
Movie-Recommender/
│
├── app.py
├── tmdb.py
├── requirements.txt
├── templates/
│   └── index.html
├── services/
│   └── recommend.py
├── data/
│   └── movies.csv
└── README.md
```

## How It Works

1. The user selects a movie.
2. The recommendation engine calculates similarity scores using content-based filtering.
3. The top similar movies are retrieved.
4. The TMDB API is used to fetch movie posters and additional details.
5. The results are displayed through a Netflix-style interface.

## Running the Project

### Prerequisites

Make sure you have the following installed:

* Python 3.x
* pip
* Git
* A TMDB API key

### 1. Clone the Repository

```bash
git clone https://github.com/sakshamm2/Movie-Recommender.git
cd Movie-Recommender
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the TMDB API

The application uses the TMDB API to retrieve movie posters, ratings, and movie details.

Add your TMDB API key according to the configuration used in `tmdb.py`.

> Do not commit your API key directly to GitHub. If the project uses environment variables, create a `.env` file locally and add the key there.

### 5. Run the Application

Start the Flask application:

```bash
python app.py
```

The application should start locally.

### 6. Open the Application

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## Screenshots


### Recommendations

![Recommendations](screenshots/recommendations.png)

## Note

Large model files (`*.pkl`) are excluded from this repository due to GitHub file size limitations.

If the required model files are not included in the repository, they need to be generated or added locally before running the application.

## Author

**Saksham Yadav**

GitHub: https://github.com/sakshamm2

LinkedIn: https://www.linkedin.com/in/saksham-yadav-047562250/
