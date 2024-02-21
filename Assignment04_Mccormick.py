tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

def mark_completed(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def delete_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        print("Task deleted.")
    else:
        print("Invalid task index.")

while True:
    print("\nSelect and option by entering the desired number:")
    print("1. Add new task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Quit program")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the new task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Enter the index of the task you would like to be marked as completed: "))
        mark_completed(index)
    elif choice == "4":
        index = int(input("Enter the index of the task you would ike to delete: "))
        delete_task(index)
    elif choice == "5":
        print("Exiting program")
        break
    else:
        print("Invalid choice, please choose a number 1-5")