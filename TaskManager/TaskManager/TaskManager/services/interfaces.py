from typing import List
from models.task import Task

class ITaskManager:
    def add_task(self, task: Task): pass
    def mark_task_done(self, index: int): pass
    def delete_task(self, index: int): pass
    def get_tasks(self) -> List[Task]: pass
