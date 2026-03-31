tasks = []


def add_task(task):
    tasks.append(task)


def remove_task(task):
    tasks.remove(task)


def list_tasks():
    for task in tasks:
        print(task)


if __name__ == "__main__":
    exit = False
    while not exit:
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            task = input("Enter task: ")
            add_task(task)
        elif choice == 2:
            task = input("Enter task: ")
            remove_task(task)
        elif choice == 3:
            list_tasks()
        elif choice == 4:
            exit = True
