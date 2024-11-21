class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task index.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks cleared.")


def main():
    todo_list = TodoList()
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                todo_list.remove_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            todo_list.clear_tasks()
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
