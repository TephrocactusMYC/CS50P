import re


def count(s):
    # Convert the line to lowercase
    s = s.lower()

    # Count the number of times 'um' appears as a word
    count = len(re.findall(r'\bum\b', s))

    return count


def main():
    print(count(input("Text: ")))


if __name__ == "__main__":
    main()
