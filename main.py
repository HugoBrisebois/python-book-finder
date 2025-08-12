import requests

# Base URL - Fixed the endpoint
Base_URL = "https://openlibrary.org/search.json"

# Getting Libraries  
def get_books(book, limit=100):
    # Add limit parameter to control number of results
    URL = f"{Base_URL}?q={book}&limit={limit}"
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
limit = input("How many results do you want? (Press Enter for all): ")

# Convert limit to integer, default to 100 if empty
try:
    limit = int(limit) if limit else 100
except ValueError:
    limit = 100

books_found = get_books(book, limit)

if books_found:
    total_results = books_found['numFound']
    displayed_results = len(books_found['docs'])
    
    print(f"\nFound {total_results} total results, displaying {displayed_results}:")
    print("-" * 40)
    
    # Display all results (or limited results based on user input)
    for i, book in enumerate(books_found['docs']):  # Show all results
        print(f"\n{i+1}. Title: {book.get('title', 'N/A')}")
        print(f"   Author(s): {', '.join(book.get('author_name', ['Unknown']))}")
        print(f"   First Published: {book.get('first_publish_year', 'N/A')}")
        if 'isbn' in book:
            print(f"   ISBN: {book['isbn'][0] if book['isbn'] else 'N/A'}")
        
        # Add a pause every 10 results for readability (optional)
        if (i + 1) % 10 == 0 and i < len(books_found['docs']) - 1:
            input("\nPress Enter to see more results...")
    
else:
    print("No books found or there was an error with the request.")