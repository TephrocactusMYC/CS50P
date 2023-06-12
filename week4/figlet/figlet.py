import sys
import random
from pyfiglet import Figlet

f = Figlet()
available_fonts = f.getFonts()

if len(sys.argv) == 1:
    s = input("Input: ").strip()
    f.setFont(font=random.choice(available_fonts))
    print(f.renderText(s))

elif len(sys.argv) == 3:
    if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in available_fonts:
        s = input("Input: ").strip()
        f.setFont(font=str(sys.argv[2]))
        print(f.renderText(s))
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")