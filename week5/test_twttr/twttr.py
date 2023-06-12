def main():
    """Gets input from the user, calls shorten() function, and prints the shortened string"""
    text = input("Input: ")
    shortened_text = shorten(text)
    print(f"Output: {shortened_text}")

def shorten(word):
    """Shortens the given string by removing all vowels"""
    vowels = set("aeiouAEIOU")
    return ''.join([c for c in word if c not in vowels])

if __name__ == "__main__":
    main()
