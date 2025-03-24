'''
Week 1 - Conditionals | Problem Set 1

In a file called extensions.py, implement a program that prompts the user for the name of a file
and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
'''

def main():
    filename = input("File name: ").lower().strip()

    if filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith(".jpeg") or filename.endswith(".jpg"):
        print("image/jpeg")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith(".pdf"):
        print("application/pdf")
    elif filename.endswith(".txt"):
        print("text/plain")
    elif filename.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()

