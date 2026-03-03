from dataclasses import dataclass


@dataclass
class Task:
    """Модель задачи."""
    id:  int
    title: str
    completed: bool = False
