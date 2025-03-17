import requests

# JokeAPI Documentation: https://v2.jokeapi.dev/
# Available endpoints:
# 1. Random Joke: https://v2.jokeapi.dev/joke/Any
# 2. Programming Joke: https://v2.jokeapi.dev/joke/Programming
# 3. Miscellaneous Joke: https://v2.jokeapi.dev/joke/Miscellaneous

def get_random_joke():
    # Get a random joke from the API.
    joke_url = "https://v2.jokeapi.dev/joke/Any"
    joke_response = requests.get(joke_url)  # Send the request to get the joke
    
    if joke_response.status_code == 200:  # Check if the request was successful
        joke_data = joke_response.json()  # Convert the JSON response to a Python dictionary
        
        if joke_data['type'] == 'single':
            print(f"Joke: {joke_data['joke']}")  # Print the single-line joke
        else:
            print(f"Setup: {joke_data['setup']}")  # Print the setup part of the joke
            print(f"Delivery: {joke_data['delivery']}")  # Print the punchline
    else:
        print("Error fetching joke.")  # Print an error message if something went wrong

def get_programming_joke():
    # Get a programming-related joke from the API.
    joke_url = "https://v2.jokeapi.dev/joke/Programming"
    joke_response = requests.get(joke_url)  # Get the joke from the API
    
    if joke_response.status_code == 200:  # Check for successful response
        joke_data = joke_response.json()  # Parse JSON response
        
        if joke_data['type'] == 'single':
            print(f"Joke: {joke_data['joke']}")  # Display the joke
        else:
            print(f"Setup: {joke_data['setup']}")  # Display the setup
            print(f"Delivery: {joke_data['delivery']}")  # Display the delivery
    else:
        print("Error getting joke.")  # Display error if request failed

def get_miscellaneous_joke():
    # Get a miscellaneous joke from the API.
    joke_url = "https://v2.jokeapi.dev/joke/Miscellaneous"
    joke_response = requests.get(joke_url)  # Make the API request
    
    if joke_response.status_code == 200:  # Check if the request was OK
        joke_data = joke_response.json()  # Convert the result into a dictionary
        
        if joke_data['type'] == 'single':
            print(f"Joke: {joke_data['joke']}")  # Show single-part joke
        else:
            print(f"Setup: {joke_data['setup']}")  # Show the setup
            print(f"Delivery: {joke_data['delivery']}")  # Show the delivery
    else:
        print("Error getting joke.")  # Show error message

def joke_menu():
    # Display a menu to select joke categories.
    while True:
        print("\nJoke App Menu:")
        print("1. Get Random Joke")
        print("2. Get Programming Joke")
        print("3. Get Miscellaneous Joke")
        print("4. Exit")

        user_choice = input("Choose an option: ")  # Get user's choice

        if user_choice == '1':
            get_random_joke()  # Get a random joke
        elif user_choice == '2':
            get_programming_joke()  # Get a programming joke
        elif user_choice == '3':
            get_miscellaneous_joke()  # Get a miscellaneous joke
        elif user_choice == '4':
            print("Exiting.")  # Exit the program
            break
        else:
            print("Invalid choice, try again.")  # Handle invalid input

# Start the joke menu
joke_menu()
