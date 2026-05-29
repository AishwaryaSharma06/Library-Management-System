import json

# List to store books
library = []


# Function to add a new book
def add_book():
    title = input("Enter book title: ")

    library.append({
        "title": title,
        "issued": False
    })

    print("Book added successfully")


# Function to display all books
def show_books():

    if not library:
        print("No books available")

    else:
        print("\nLibrary Books:")

        for i, book in enumerate(library):
            status = "Issued" if book["issued"] else "Available"
            print(f"{i + 1}. {book['title']} - {status}")


# Function to issue a book
def issue_book():

    show_books()

    try:
        index = int(input("Enter book number to issue: ")) - 1

        if 0 <= index < len(library):

            if not library[index]["issued"]:
                library[index]["issued"] = True
                print("Book issued successfully")

            else:
                print("Book already issued")

        else:
            print("Invalid choice")

    except ValueError:
        print("Enter a valid number")


# Function to return a book
def return_book():

    show_books()

    try:
        index = int(input("Enter book number to return: ")) - 1

        if 0 <= index < len(library):

            if library[index]["issued"]:
                library[index]["issued"] = False
                print("Book returned successfully")

            else:
                print("Book was not issued")

        else:
            print("Invalid choice")

    except ValueError:
        print("Enter a valid number")


# Function to save data into JSON file
def save_data():

    with open("library.json", "w") as file:
        json.dump(library, file)


# Function to load existing data
def load_data():

    try:
        with open("library.json", "r") as file:
            data = json.load(file)
            library.extend(data)

    except FileNotFoundError:
        pass


# Load previous data when program starts
load_data()


# Main menu loop
while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()

    elif choice == "2":
        show_books()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        save_data()
        print("Data saved successfully")
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select 1-5.")