import tkinter as tk
from tkinter import messagebox

import data_manager
import analysis
import visualization

# CREATE MAIN WINDOW

window = tk.Tk()

window.title("Reading Group Recommendation System")
window.geometry("600x700")


# TITLE

title = tk.Label(
    window,
    text="Reading Group Recommendation System",
    font=("Arial", 18, "bold")
)

title.pack(pady=20)


# BOOK NAME

tk.Label(
    window,
    text="Book Name"
).pack()

book_entry = tk.Entry(
    window,
    width=40
)

book_entry.pack(pady=5)


# GENRE

tk.Label(
    window,
    text="Genre"
).pack()

genre_entry = tk.StringVar()

genre_entry.set("Fiction")

genre_menu = tk.OptionMenu(
    window,
    genre_entry,
    "Fiction",
    "Fantasy",
    "Self Help",
    "Finance",
    "Mystery",
    "Science"
)

genre_menu.pack(pady=5)

# RECOMMENDER

tk.Label(
    window,
    text="Recommender"
).pack()

recommender_entry = tk.Entry(
    window,
    width=40
)

recommender_entry.pack(pady=5)


# RATING

tk.Label(
    window,
    text="Rating (1-5)"
).pack()

rating_entry = tk.StringVar()

rating_entry.set("1")

rating_menu = tk.OptionMenu(
    window,
    rating_entry,
    "1",
    "2",
    "3",
    "4",
    "5"
)

rating_menu.pack(pady=5)



# USEFUL

tk.Label(
    window,
    text="Was it useful?"
).pack()

useful_entry = tk.StringVar()

useful_entry.set("Yes")

useful_menu = tk.OptionMenu(
    window,
    useful_entry,
    "Yes",
    "No"
)

useful_menu.pack(pady=5)


# ADD RECOMMENDATION

def add_recommendation():

    book = book_entry.get()
    genre = genre_entry.get()
    recommender = recommender_entry.get()
    rating = rating_entry.get()
    useful = useful_entry.get()

    # Check empty fields
    if book == "" or genre == "" or recommender == "":

        messagebox.showerror(
            "Error",
            "Please fill all fields."
        )

        return

    # Check rating
    try:

        rating = int(rating)

        if rating < 1 or rating > 5:

            messagebox.showerror(
                "Error",
                "Rating must be between 1 and 5."
            )

            return

    except ValueError:

        messagebox.showerror(
            "Error",
            "Rating must be a number."
        )

        return

    # Check useful value
    if useful != "Yes" and useful != "No":

        messagebox.showerror(
            "Error",
            "Please select Yes or No."
        )

        return

    # Save record
    success = data_manager.add_record(
        book,
        genre,
        recommender,
        rating,
        useful
    )

    if success:

        messagebox.showinfo(
            "Success",
            "Recommendation added successfully."
        )

        clear_fields()

    else:

        messagebox.showerror(
            "Error",
            "Could not save the recommendation."
        )


# CLEAR FIELDS

def clear_fields():

    book_entry.delete(
        0,
        tk.END
    )

    recommender_entry.delete(
        0,
        tk.END
    )

    genre_entry.set("Fiction")

    rating_entry.set("1")

    useful_entry.set("Yes")


# VIEW ALL RECORDS

def view_records():

    records = data_manager.get_records()

    if len(records) == 0:

        messagebox.showinfo(
            "Records",
            "No records found."
        )

        return

    text = ""

    for record in records:

        text = text + (
            "Book: " + record["Book"] + "\n"
            "Genre: " + record["Genre"] + "\n"
            "Recommender: " + record["Recommender"] + "\n"
            "Rating: " + record["Rating"] + "\n"
            "Useful: " + record["Useful"] + "\n"
            "-----------------------------\n"
        )

    show_window(
        "All Recommendations",
        text
    )


# SHOW ANALYSIS

def show_analysis():

    total = analysis.total_recommendations()

    average = analysis.average_rating()

    genre = analysis.preferred_genre()

    useful = analysis.useful_count()

    recommenders = analysis.recommender_count()

    text = (
        "Total Recommendations: "
        + str(total)
        + "\n\n"

        "Average Rating: "
        + str(average)
        + "\n\n"

        "Most Preferred Genre: "
        + genre
        + "\n\n"

        "Useful Recommendations: "
        + str(useful.get("Useful", 0))
        + "\n\n"

        "Not Useful Recommendations: "
        + str(useful.get("Not Useful", 0))
        + "\n\n"

        "Recommendations by Recommender:\n"
    )

    for name in recommenders:

        text = text + (
            name
            + " : "
            + str(recommenders[name])
            + "\n"
        )

    show_window(
        "Analysis",
        text
    )


# SEARCH RECORDS

def search():

    keyword = search_entry.get()

    if keyword == "":

        messagebox.showerror(
            "Error",
            "Enter something to search."
        )

        return

    results = data_manager.search_records(
        keyword
    )

    if len(results) == 0:

        messagebox.showinfo(
            "Search",
            "No records found."
        )

        return

    text = ""

    for record in results:

        text = text + (
            "Book: " + record["Book"] + "\n"
            "Genre: " + record["Genre"] + "\n"
            "Recommender: " + record["Recommender"] + "\n"
            "Rating: " + record["Rating"] + "\n"
            "Useful: " + record["Useful"] + "\n"
            "-----------------------------\n"
        )

    show_window(
        "Search Results",
        text
    )



# SHOW RESULT WINDOW

def show_window(title_text, text):

    new_window = tk.Toplevel(window)

    new_window.title(title_text)

    new_window.geometry("500x500")

    text_box = tk.Text(
        new_window,
        width=60,
        height=25
    )

    text_box.pack(
        padx=10,
        pady=10
    )

    text_box.insert(
        tk.END,
        text
    )

    text_box.config(
        state="disabled"
    )



# BUTTONS

tk.Button(
    window,
    text="Add Recommendation",
    command=add_recommendation,
    width=25
).pack(pady=10)


tk.Button(
    window,
    text="Clear",
    command=clear_fields,
    width=25
).pack(pady=5)


tk.Button(
    window,
    text="View All Records",
    command=view_records,
    width=25
).pack(pady=5)


tk.Button(
    window,
    text="Show Analysis",
    command=show_analysis,
    width=25
).pack(pady=5)


# SEARCH

tk.Label(
    window,
    text="Search Book / Genre / Recommender"
).pack(pady=10)

search_entry = tk.Entry(
    window,
    width=40
)

search_entry.pack()


tk.Button(
    window,
    text="Search Records",
    command=search,
    width=25
).pack(pady=5)


# GRAPH BUTTONS

tk.Button(
    window,
    text="Genre Recommendation Graph",
    command=visualization.genre_graph,
    width=30
).pack(pady=10)


tk.Button(
    window,
    text="Genre Rating Graph",
    command=visualization.rating_graph,
    width=30
).pack(pady=5)



# EXIT BUTTON

tk.Button(
    window,
    text="Exit",
    command=window.destroy,
    width=25
).pack(pady=15)


# START APPLICATION

window.mainloop()