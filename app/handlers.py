from models import Task
from utils import load_data, save_data


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []
        self._load()

    def _load(self):
        data = load_data()
        self.tasks = [Task(**item) for item in data]

    def _save(self):
        save_data([task.__dict__ for task in self.tasks])

    def add(self, title: str) -> Task:
        """Добавление задачи."""
        next_id = max((task.id for task in self.tasks), default=0) + 1
        task = Task(title=title, id=next_id)
        self.tasks.append(task)
        self._save()
        return task

    def get_all(self) -> list[Task]:
        """Получение всех задач."""
        return self.tasks

    def delete(self, task_id: int) -> bool:
        """Удаление задачи."""
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self._save()
                return True
        return False

    def mark_completed(self, task_id: int) -> bool:
        """Отметка о выполнении."""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self._save()
                return True
        return False
