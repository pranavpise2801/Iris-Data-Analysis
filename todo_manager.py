import argparse
import os
import json

# File to store tasks
TASK_FILE = "tasks.json"

# Helper functions
def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['description']}")

def delete_task(index):
    """Delete a task by its index."""
    tasks = load_tasks()
    try:
        task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task deleted: {task['description']}")
    except IndexError:
        print("Invalid task number.")

def mark_done(index):
    """Mark a task as done."""
    tasks = load_tasks()
    try:
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"Task marked as done: {tasks[index - 1]['description']}")
    except IndexError:
        print("Invalid task number.")

# Set up argparse
parser = argparse.ArgumentParser(description="To-Do List Manager")
parser.add_argument("action", choices=["add", "list", "delete", "done"], help="Action to perform")
parser.add_argument("--task", type=str, help="Task description (for add action)")
parser.add_argument("--index", type=int, help="Task number (for delete or done actions)")

args = parser.parse_args()

# Perform actions based on the command-line arguments
if args.action == "add":
    if args.task:
        add_task(args.task)
    else:
        print("Error: --task is required for the 'add' action.")
elif args.action == "list":
    list_tasks()
elif args.action == "delete":
    if args.index:
        delete_task(args.index)
    else:
        print("Error: --index is required for the 'delete' action.")
elif args.action == "done":
    if args.index:
        mark_done(args.index)
    else:
        print("Error: --index is required for the 'done' action.")
