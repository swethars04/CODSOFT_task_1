import json
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date=None, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

def create_task(title, description, due_date=None):
    return Task(title, description, due_date)

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4, default=str)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks_data = json.load(f)
            tasks = []
            for task_data in tasks_data:
                if 'completed' not in task_data:
                    task_data['completed'] = False
                tasks.append(Task(**task_data))
            return tasks
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    print("\n==== Tasks ====")
    for i, task in enumerate(tasks, 1):
        due_date = task.due_date if task.due_date else "No due date"
        status = 'Completed' if task.completed else 'Incomplete'
        print(f"{i}. {task.title} - {task.description} - Due: {due_date} - {status}")

def main():
    tasks = load_tasks()

    while True:
        print("\n==== To-Do List Menu ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
            due_date = datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
            task = create_task(title, description, due_date)
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!")
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            if tasks:
                display_tasks(tasks)
                task_number = int(input("Enter the task number to mark as completed: "))
                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1].mark_as_completed()
                    save_tasks(tasks)
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to complete.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
