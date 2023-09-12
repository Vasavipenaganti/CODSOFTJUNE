class Task:
    def _init_(self, title, description):
        self.title = title
        self.description = description
        self.complete = False

class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "Complete" if task.complete else "Incomplete"
            print(f"{i+1}. {task.title} ({status})")

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete = True
        else:
            print("Invalid task index")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter the task index to mark as complete: ")) - 1
            todo_list.mark_complete(index)
        elif choice == '4':
            index = int(input("Enter the task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
