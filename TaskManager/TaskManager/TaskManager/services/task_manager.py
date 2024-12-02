from typing import List
from models.task import Task
from services.interfaces import ITaskManager

class TaskManager(ITaskManager):
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def mark_task_done(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()

    def delete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_tasks(self) -> List[Task]:
        return self.tasks
