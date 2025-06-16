import webbrowser

user_term = input("Enter search term: ").replace(" ", "+")

webbrowser.open("https://www.google.co.uk/search?q=" + user_term)
