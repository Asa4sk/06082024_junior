with open("file.txt", "r") as source_file:
    content = source_file.read()
    print(content)
    dest_file.write(content)
