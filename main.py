import json
import os
from datetime import datetime
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

    print("\nChoose a priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    priority_choice = input("Enter priority (1-3): ")

    priorities = {
        "1": "High",
        "2": "Medium",
        "3": "Low"
    }

    if priority_choice not in priorities:
        print("Invalid priority. Please choose 1, 2, or 3.")
        return

    priority = priorities[priority_choice]

    due_date = input("Enter due date (YYYY-MM-DD): ")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Please use YYYY-MM-DD.")
        return

    tasks.append({
        "task": task_name,
        "completed": False,
        "priority": priority,
        "due_date": due_date
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

        
        priority = task.get("priority", "Medium")
        due_date = task.get("due_date", "Not set")

        print(
            f"{number}. {task['task']} "
            f"[{status}] [Priority: {priority}] "
            f"[Due: {due_date}]"
        )
def filter_tasks():
    if not tasks:
        print("You have no tasks to filter.")
        return

    print("\n========== FILTER TASKS ==========")
    print("1. Filter by priority")
    print("2. Filter by status")
    print("3. Return to main menu")

    filter_choice = input("Choose a filter option: ")

    matching_tasks = []

    if filter_choice == "1":
        print("\nChoose a priority:")
        print("1. High")
        print("2. Low")
        print("3. Medium")

        priority_choice = input("Enter priority (1-3): ")

        priorities = {
            "1": "High",
            "2": "Low",
            "3": "Medium"
        }

        if priority_choice not in priorities:
            print("Invalid priority choice.")
            return

        selected_priority = priorities[priority_choice]

        for task in tasks:
            if task.get("priority", "Medium") == selected_priority:
                matching_tasks.append(task)

        filter_label = f"{selected_priority} priority"

    elif filter_choice == "2":
        print("\nChoose a status:")
        print("1. Pending")
        print("2. Completed")

        status_choice = input("Enter status (1-2): ")

        if status_choice == "1":
            for task in tasks:
                if not task["completed"]:
                    matching_tasks.append(task)

            filter_label = "Pending"

        elif status_choice == "2":
            for task in tasks:
                if task["completed"]:
                    matching_tasks.append(task)

            filter_label = "Completed"

        else:
            print("Invalid status choice.")
            return

    elif filter_choice == "3":
        return

    else:
        print("Invalid filter option.")
        return

    if not matching_tasks:
        print(f"No {filter_label} tasks found.")
        return

    print(f"\n========== {filter_label.upper()} TASKS ==========")

    for number, task in enumerate(matching_tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        priority = task.get("priority", "Medium")
        due_date = task.get("due_date", "Not set")

        print(
            f"{number}. {task['task']} "
            f"[{status}] [Priority: {priority}] "
            f"[Due: {due_date}]"
        )

def search_tasks():
    if not tasks:
        print("You have no tasks to search.")
        return

    search_term = input("Enter a task name to search for: ").strip().lower()

    if search_term == "":
        print("Please enter a search term.")
        return

    matching_tasks = []

    for task in tasks:
        if search_term in task["task"].lower():
            matching_tasks.append(task)

    if not matching_tasks:
        print("No matching tasks found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for number, task in enumerate(matching_tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        priority = task.get("priority", "Medium")
        due_date = task.get("due_date", "Not set")

        print(
            f"{number}. {task['task']} "
            f"[{status}] [Priority: {priority}] "
            f"[Due: {due_date}]"
        )
def sort_tasks_by_due_date():
    if not tasks:
        print("You have no tasks to sort.")
        return

    print("\n========== SORT TASKS ==========")
    print("1. Sort by due date")
    print("2. Sort by priority")
    print("3. Return to main menu")

    sort_choice = input("Choose a sorting option (1-3): ")

    if sort_choice == "1":
        print("\n1. Earliest to latest")
        print("2. Latest to earliest")

        date_choice = input("Choose a date sorting option (1-2): ")

        if date_choice == "1":
            sorted_tasks = sorted(
                tasks,
                key=lambda task: task.get("due_date", "9999-12-31")
            )
            sort_label = "EARLIEST TO LATEST"

        elif date_choice == "2":
            sorted_tasks = sorted(
                tasks,
                key=lambda task: task.get("due_date", "9999-12-31"),
                reverse=True
            )
            sort_label = "LATEST TO EARLIEST"

        else:
            print("Invalid date sorting option.")
            return

    elif sort_choice == "2":
        print("\nChoose a priority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        priority_choice = input("Choose a priority (1-3): ")

        priorities = {
            "1": "High",
            "2": "Medium",
            "3": "Low"
        }

        if priority_choice not in priorities:
            print("Invalid priority choice. Please choose 1, 2, or 3.")
            return

        selected_priority = priorities[priority_choice]

        sorted_tasks = sorted(
            [
                task for task in tasks
                if task.get("priority", "Medium") == selected_priority
            ],
            key=lambda task: task.get("due_date", "9999-12-31")
        )

        sort_label = f"{selected_priority.upper()} PRIORITY"

    elif sort_choice == "3":
        return

    else:
        print("Invalid sorting option. Please choose 1, 2, or 3.")
        return

    print(f"\n========== TASKS: {sort_label} ==========")

    for number, task in enumerate(sorted_tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        priority = task.get("priority", "Medium")
        due_date = task.get("due_date", "Not set")

        print(
            f"{number}. {task['task']} "
            f"[{status}] [Priority: {priority}] "
            f"[Due: {due_date}]"
        )
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
    print("5. Search tasks")
    print("6. Filter tasks")
    print("7. Sort tasks")
    print("8. Exit")

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
        search_tasks()

    elif choice == "6":
        filter_tasks()

    elif choice == "7":
        sort_tasks_by_due_date()

    elif choice == "8":
        print("Thank you for using Python Task Manager!")
        break

    else:
        print("Invalid choice. Please choose 1-8.")
