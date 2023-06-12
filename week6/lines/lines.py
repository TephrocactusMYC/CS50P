import sys
import os

def count_lines(file_path):
    """
    Count the number of lines in a file, excluding comments and blank lines.

    Args:
        file_path: the path of the target file

    Returns:
        The number of non-comment and non-whitespace lines in the given file.
    """
    ignored_lines = 0
    with open(file_path, "r", encoding="utf-8") as f:
        # Get a list of all the lines in the file, alongside their line numbers.
        total_lines = list(enumerate(f.readlines(), start=1))
        for line_number, line in total_lines:
            # If the line is a comment or a blank line, count it as ignored.
            if (line.lstrip().startswith("#") or line.isspace()):
                ignored_lines += 1
        # Return the total number of lines minus the ignored lines.
        return len(total_lines) - ignored_lines


def main():
    """
    Entry point of the script.

    Reads the command-line arguments and invokes count_lines() to count the number of code lines
    in the specified Python file.
    """
    # Check that there is exactly one command-line argument.
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    # Check that the specified file is a Python file.
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    # Check that the specified file exists.
    if not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")

    # Count the number of code lines in the specified file.
    try:
        line_count = count_lines(sys.argv[1])
        print(line_count)
    except Exception as e:
        sys.exit("Error: " + str(e))


if __name__ == "__main__":
    main()
