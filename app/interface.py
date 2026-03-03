import sys
from handlers import TaskManager

manager = TaskManager()


def show_menu() -> None:
    print('\n====== TASK MANAGER ======')
    print('1. Показать задачи')
    print('2. Добавить задачу')
    print('3. Отметить выполненной')
    print('4. Удалить задачу')
    print('0. Выход')


def list_tasks() -> None:
    tasks = manager.get_all()
    if not tasks:
        print('Ваш список задач пуст.')
        return
    print('\n====== Список задач ======')
    for task in tasks:
        status = '+' if task.completed else ' '
        print(f'{task.id}. [{status}] {task.title}')


def action_choicer(choice: str):
    if choice == '1':
        list_tasks()
        print('\nНажмите Enter, чтобы вернуться в меню')
        input()

    elif choice == '2':
        while True:
            title = input('Введите название задачу: ').strip()
            if title:
                task = manager.add(title)
                print(f'Задача добавлена с ID {task.id}.')
                break
            else:
                print('Название задачи не может быть пустым.')

    elif choice == '3':
        while True:
            try:
                task_id = int(input('Введите ID задачи: '))
                if manager.mark_completed(task_id):
                    print('Задача отмечена выполненной.')
                    break
                else:
                    print('Задача с таким ID не найдена.')
            except ValueError:
                print('ОШИБКА: ID должен быть целым числом.')

    elif choice == '4':
        while True:
            try:
                task_id = int(input('Введите ID задачи: '))
                if manager.delete(task_id):
                    print('Задача удалена.')
                    break
                else:
                    print('Задача с таким ID не найдена.')
            except ValueError:
                print('ОШИБКА: ID должен быть целым числом.')

    elif choice == '0':
        print('Выход...')
        sys.exit()

    else:
        print('ОШИБКА: Выберете один из пунктов меню.')
