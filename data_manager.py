import csv

# Name of the CSV file
FILE_NAME = "recommendations.csv"


# Add a new recommendation
# Add a new recommendation
def add_record(book, genre, recommender, rating, useful):

    try:

        # Open file in append mode
        with open(FILE_NAME, "a", newline="") as file:

            # Check if file already has data
            file.seek(0, 2)

            if file.tell() > 0:

                file.write("\n")

            writer = csv.writer(file)

            writer.writerow([
                book,
                genre,
                recommender,
                rating,
                useful
            ])

        return True

    except Exception as e:

        print("Error while saving record:", e)

        return False

# Get all records from CSV file
def get_records():

    records = []

    try:
        with open(FILE_NAME, "r", newline="") as file:

            reader = csv.DictReader(file)

            # Check that CSV has correct column names
            if reader.fieldnames is None:
                print("CSV file is empty.")
                return records

            required_columns = [
                "Book",
                "Genre",
                "Recommender",
                "Rating",
                "Useful"
            ]

            for column in required_columns:

                if column not in reader.fieldnames:
                    print("CSV file has incorrect headings.")
                    return records

            # Read each record
            for row in reader:
                records.append(row)

    except FileNotFoundError:

        print("CSV file not found.")

    except Exception as e:

        print("Error while reading file:", e)

    return records


# Search records
def search_records(keyword):

    records = get_records()

    results = []

    # Convert search word to lowercase
    keyword = keyword.lower()

    for record in records:

        book = record["Book"].lower()
        genre = record["Genre"].lower()
        recommender = record["Recommender"].lower()

        if (keyword in book
                or keyword in genre
                or keyword in recommender):

            results.append(record)

    return results