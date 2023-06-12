def main():
    text=input()
    if ":)" in text or ":(" in text:
        text=convert(text)
        print(text)
def convert(thestr):
    thestr=thestr.replace(":)", "🙂")
    thestr=thestr.replace(":(", "🙁")
    return thestr
main()