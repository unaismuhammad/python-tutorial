try:
    fname = input("enter fname to read:")
    with open(fname,'r')as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("error:file not found.")
