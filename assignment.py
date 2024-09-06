def create_file():
    try:
        with open("my_assignment.txt", "w") as file:
            file.write("This is my first Python file handling assignment.\n")
            file.write("File handling is such a fun\n")
            file.write("I thank myself for taking this test.\n")
        print("File created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        with open("my_assignment.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file 'my_assignment.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


def append_to_a_file():
    try:
        with open("my_assignment.txt", "a") as file:
            file.write("I also enjoyed learning about file handling.\n")
            file.write("This is the end of my assignment.\n")
            file.write("File handling in Python is versatile!.\n")
        print("Content appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    print("1. Creating a file and writing content ")
    create_file()
    print("\n2. Reading content from the file ")
    read_file()
    print("\n3. Appending content to the file ")
    append_to_a_file()


if __name__ == "__main__":
    main()