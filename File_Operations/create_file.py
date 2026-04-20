import os

def create_file(filename):
    if os.path.exists(filename):
        print(f"The file '{filename}' already exists.")
    else:
        with open(filename, 'w') as file:
            file.write("") 
        print(f"The file '{filename}' has been created.")
if __name__ == "__main__":
    filename = input("Enter the name of the file to create: ")
    create_file(filename)
    