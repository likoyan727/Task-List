class TaskList:
    def __init__(self):
        # Initialize an empty list to store tasks.
        self.tasks = []

    def add_task(self, task):
        # Add a new task to the list.
        self.tasks.append(task)
        print(f"Task '{task['name']}' added successfully!")

    def remove_task(self, task_name):
        # Remove a task by name from the list.
        for task in self.tasks:
            if task['name'] == task_name:
                self.tasks.remove(task)
                print(f"Task '{task_name}' removed successfully!")
                return
        print(f"Task '{task_name}' not found.")

    def display_priority_list(self):
        # Implement your method to display tasks based on priority here.
        pass

    def list_all_tasks(self):
        # List all tasks with details such as name and priority.
        if not self.tasks:
            print("No tasks in the list.")
            return
        
        print("List of all tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. Task Name: {task['name']}, Priority: {task.get('priority', 'Not specified')}")

# Example usage
task_list = TaskList()
task_list.add_task({'name': 'Task 1', 'priority': 'High'})
task_list.add_task({'name': 'Task 2', 'priority': 'Medium'})
task_list.list_all_tasks()
