
import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    task_name = input("Enter your task: ")

    if task_name.strip() == "":
        print("Task cannot be empty!")
        return

    tasks.append({
        "task": task_name,
        "completed": False
    })

    save_tasks()
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("You have no tasks yet.")
        return

    print("\n========== YOUR TASKS ==========")

    for number, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{number}. {task['task']} [{status}]")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            save_tasks()
            print(f"Deleted task: {deleted_task['task']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


tasks = load_tasks()


while True:
    print("\n================================")
    print("       PYTHON TASK MANAGER")
    print("================================")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using Python Task Manager!")
        break

    else:
        print("Invalid choice. Please choose 1-5.")
