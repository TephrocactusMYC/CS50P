def main():
    text=input("File name: ").strip().lower()
    if "." in text:
        extension=text.split(".")[-1]
        match extension:
            case "gif":
                print("image/gif")
            case "jpeg":
                print("image/jpeg")
            case "jpg":
                print("image/jpeg")
            case "png":
                print("image/png")
            case "pdf":
                print("application/pdf")
            case "zip":
                print("application/zip")
            case "txt":
                print("text/plain")
            case _ :
                print("application/octet-stream")
    else:
        print("application/octet-stream")

main()