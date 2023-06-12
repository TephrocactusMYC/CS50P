import os
import sys
import csv
from tabulate import tabulate


def main():
    """Pass the data in the sys.argv to tabulate."""
    if len(sys.argv) != 2:
        print("Wrong number of command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    else:
        # Do the thing!
        with open(sys.argv[1], "r") as csv_file:
            table = csv.DictReader(csv_file)
            # Format the rest of the rows using tabulate
            print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
