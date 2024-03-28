import json
import os
from datetime import datetime

# Function to load tasks from a file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    else:
        return {"tasks": []}

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    tasks["tasks"].append({
        "name": task_name,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks):
    print_tasks(tasks)
    task_index = int(input("Enter task index to remove: "))
    del tasks["tasks"][task_index]
    save_tasks(tasks)
    print("Task removed successfully.")

# Function to mark a task as completed
def complete_task(tasks):
    print_tasks(tasks)
    task_index = int(input("Enter task index to mark as completed: "))
    tasks["tasks"][task_index]["completed"] = True
    save_tasks(tasks)
    print("Task marked as completed.")

# Function to display tasks
def print_tasks(tasks):
    print("\n=== TASKS ===")
    for index, task in enumerate(tasks["tasks"]):
        print(f"{index}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")
    print()

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print_tasks(tasks)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
