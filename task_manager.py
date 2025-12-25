tasks = []

def main():
    print("Task Manager CLI")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "4":
        print("Goodbye!")

if __name__ == "__main__":
    main()
