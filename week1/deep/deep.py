print("What is the Answer to the Great Question of Life, the Universe, and Everything?", end="")

text=input().strip().title()
if text=="42" or text=="Forty-Two" or text=="Forty Two":
    print("Yes", end="")
else:
    print("No", end="")