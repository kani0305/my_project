import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file]
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully.")
    else:
        print("⚠ Task cannot be empty.")

def mark_completed(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("\nEnter task number to mark as completed: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1] += " ✅ (Completed)"
                save_tasks(tasks)
                print("🎯 Task marked as completed.")
            else:
                print("⚠ Invalid task number.")
        except ValueError:
            print("⚠ Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("\nEnter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                deleted = tasks.pop(task_no - 1)
                save_tasks(tasks)
                print(f"🗑 Deleted task: {deleted}")
            else:
                print("⚠ Invalid task number.")
        except ValueError:
            print("⚠ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n📋 To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting. Have a productive day!")
            break
        else:
            print("⚠ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()