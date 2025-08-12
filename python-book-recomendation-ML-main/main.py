import requests

# Base URL - Fixed the endpoint
Base_URL = "https://openlibrary.org/search.json"

# Getting Libraries
def get_books(book):
    # Fixed URL construction - removed /subjects and added proper query parameter
    URL = f"{Base_URL}?q={book}"
    response = requests.get(URL)
    print(f"Request URL: {URL}")
    print(f"Response status: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        return data  # Return the actual data
    else:
        print(f"Retrieval failed with status code: {response.status_code}")
        return None

# Main program
print("Welcome To Your Book Recommendation Center")
print("-" * 40)
book = input("What book are you searching for? ")

books_found = get_books(book)

if books_found:
    print(f"\nFound {books_found['numFound']} results:")
    print("-" * 40)
    
    # Display first few results
    for i, book in enumerate(books_found['docs'][:5]):  # Show first 5 results
        print(f"\n{i+1}. Title: {book.get('title', 'N/A')}")
        print(f"   Author(s): {', '.join(book.get('author_name', ['Unknown']))}")
        print(f"   First Published: {book.get('first_publish_year', 'N/A')}")
        if 'isbn' in book:
            print(f"   ISBN: {book['isbn'][0] if book['isbn'] else 'N/A'}")
else:
    print("No books found or there was an error with the request.")