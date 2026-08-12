"""Core logic for TaskCLI - a simple JSON-backed task manager."""
import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks(path=DATA_FILE):
    """Load tasks from the JSON file. Returns an empty list if it doesn't exist."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, path=DATA_FILE):
    """Persist the list of tasks to the JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(description, tasks=None, path=DATA_FILE):
    """Add a new task and return the updated list."""
    if tasks is None:
        tasks = load_tasks(path)
    new_id = (max((t["id"] for t in tasks), default=0)) + 1
    tasks.append({"id": new_id, "description": description, "done": False})
    save_tasks(tasks, path)
    return tasks


def list_tasks(tasks=None, path=DATA_FILE):
    """Return the list of tasks."""
    if tasks is None:
        tasks = load_tasks(path)
    return tasks


def complete_task(task_id, tasks=None, path=DATA_FILE):
    """Mark a task as done. Returns True if found, False otherwise."""
    if tasks is None:
        tasks = load_tasks(path)
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks, path)
            return True
    return False


def remove_task(task_id, tasks=None, path=DATA_FILE):
    """Remove a task by id. Returns True if found, False otherwise."""
    if tasks is None:
        tasks = load_tasks(path)
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            save_tasks(tasks, path)
            return True
    return False