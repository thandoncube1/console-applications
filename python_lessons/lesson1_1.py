# Using main as the entry point for the python interpreter to start
# code execution for all functions defined in main()

from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified."
    sleep(3)
    print("Data processing finished.")
    return modified_data

def main():
    data = "My data read from the web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)

if __name__ and "__main__":
    main()
