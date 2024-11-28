import wikipedia


def main():
    while True:
        search_input = input("Enter a page title or search phrase (press Enter to quit): ")
        if not search_input.strip():  # If input is blank
            print("Program terminated.")
            break
        try:
            summary = wikipedia.summary(search_input)
            print(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print("Ambiguous term. Please be more specific.")
        except wikipedia.exceptions.PageError as e:
            print("Page not found. Please try another search.")


if __name__ == "__main__":
    main()
