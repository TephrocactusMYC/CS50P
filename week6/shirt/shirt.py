import os
import sys
from PIL import Image, ImageOps


def main():
    """Dress a puppet in a Harvard CS50 Shirt."""
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f"Invalid input - Path")
        sys.exit(1)
    elif not format_check(sys.argv[1]) and format_check(sys.argv[2]):
        print("Invalid input")
        sys.exit(1)
    elif not format_same(sys.argv[1], sys.argv[2]):
        print("Input and output have different extensions")
        sys.exit(1)
    else:
        fit_shirt(sys.argv[1], sys.argv[2])
def format_check(input_filetype):
    valid_formats = {"jpg", "jpeg", "png"}
    return input_filetype.endswith(tuple(valid_formats))

def format_same(input_file, output_file):
    _, input_ext = os.path.splitext(input_file)
    _, output_ext = os.path.splitext(output_file)
    return input_ext == output_ext
def fit_shirt(input_file, output_file):
    shirt = Image.open("shirt.png")
    photo = Image.open(input_file)

    a, b = shirt.size
    photo = ImageOps.fit(photo, (a, b))

    photo.paste(shirt, shirt)
    photo.save(output_file)
    
if __name__ == "__main__":
    main()