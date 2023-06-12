import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    """Extract a YouTube URL from a given string of embedded HTML."""
    try:
        url = re.search('embed\/(.*?)"', s).group(0)
        url=url.replace("embed/","")
        url=url.replace('"',"")
        return "https://youtu.be/" + url
    except Exception:
        return None


if __name__ == "__main__":
    main()