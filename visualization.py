import matplotlib.pyplot as plt
import analysis


# Graph 1: Number of recommendations by genre
def genre_graph():

    data = analysis.genre_count()

    if len(data) == 0:
        print("No data available.")
        return

    genres = list(data.keys())
    counts = list(data.values())

    # Create a new graph
    plt.figure()

    plt.bar(genres, counts)

    plt.xlabel("Genre")
    plt.ylabel("Number of Recommendations")
    plt.title("Recommendations by Genre")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# Graph 2: Average rating by genre
def rating_graph():

    data = analysis.genre_rating()

    if len(data) == 0:
        print("No data available.")
        return

    genres = list(data.keys())
    ratings = list(data.values())

    # Create a new graph
    plt.figure()

    plt.bar(genres, ratings)

    plt.xlabel("Genre")
    plt.ylabel("Average Rating")
    plt.title("Average Rating by Genre")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()