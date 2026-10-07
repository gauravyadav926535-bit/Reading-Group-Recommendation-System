import pandas as pd
import numpy as np

FILE_NAME = "recommendations.csv"


# Load data
def load_data():

    try:
        data = pd.read_csv(FILE_NAME)
        return data

    except FileNotFoundError:
        return pd.DataFrame()


# Total number of recommendations
def total_recommendations():

    data = load_data()

    return len(data)


# Average rating
def average_rating():

    data = load_data()

    if len(data) == 0:
        return 0

    return round(data["Rating"].mean(), 2)


# Count each genre
def genre_count():

    data = load_data()

    if len(data) == 0:
        return {}

    return data["Genre"].value_counts().to_dict()


# Average rating of each genre
def genre_rating():

    data = load_data()

    result = {}

    if len(data) == 0:
        return result

    genres = data["Genre"].unique()

    for genre in genres:

        ratings = data[data["Genre"] == genre]["Rating"]

        result[genre] = round(ratings.mean(), 2)

    return result

# Count recommendations by each recommender
def recommender_count():

    data = load_data()

    if len(data) == 0:
        return {}

    recommenders = data["Recommender"].value_counts()

    return recommenders.to_dict()

# Count useful and not useful recommendations
def useful_count():

    data = load_data()

    if len(data) == 0:
        return {}

    useful = np.sum(data["Useful"] == "Yes")
    not_useful = np.sum(data["Useful"] == "No")

    return {
        "Useful": int(useful),
        "Not Useful": int(not_useful)
    }


# Find most preferred genre
def preferred_genre():

    counts = genre_count()

    if len(counts) == 0:
        return "No data"

    genre = max(counts, key=counts.get)

    return genre