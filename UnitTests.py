import unittest
from TaskList import TaskList

class TestTaskList(unittest.TestCase):
    def setUp(self):
        # Initialize a TaskList instance before each test.
        self.task_list = TaskList()

    def test_add_task(self):
        # Test adding a task.
        task = {'name': 'Task 1', 'priority': 'High'}
        self.task_list.add_task(task)
        # Verify that the task has been added to the list.
        self.assertIn(task, self.task_list.tasks)

    def test_remove_task(self):
        # Test removing a task.
        task = {'name': 'Task 1', 'priority': 'High'}
        # Add the task to the list.
        self.task_list.add_task(task)
        # Remove the task by name.
        self.task_list.remove_task('Task 1')
        # Verify that the task has been removed from the list.
        self.assertNotIn(task, self.task_list.tasks)

if __name__ == '__main__':
    unittest.main()
