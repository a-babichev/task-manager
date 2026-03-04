import sys
from handlers import TaskManager

manager = TaskManager()


def show_menu() -> None:
    """Метод отображения главного меню."""
    print('\n====== TASK MANAGER ======')
    print('1. Показать задачи')
    print('2. Добавить задачу')
    print('3. Отметить выполненной')
    print('4. Удалить задачу')
    print('0. Выход')


def list_tasks() -> None:
    """Метод для отображения списка задач."""
    tasks = manager.get_all()
    if not tasks:
        print('Ваш список задач пуст.')
        return
    print('\n====== Список задач ======')
    for task in tasks:
        status = '+' if task.completed else ' '
        print(f'{task.id}. [{status}] {task.title}')


def action_choicer(choice: str):
    """Метод для управления действиями."""
    actions = {
        '1': _show_tasks,
        '2': _add_task,
        '3': lambda: _process_task('mark_completed', 'отмечена выполненной'),
        '4': lambda: _process_task('delete', 'удалена'),
        '0': _exit_app,
    }

    action = actions.get(choice)
    if action:
        action()
    else:
        print('ОШИБКА: Выберете один из пунктов меню.')


def _show_tasks():
    """Показать все задачи"""
    list_tasks()
    input('\nНажмите Enter, чтобы вернуться в меню...')


def _add_task():
    """Добавить новую задачу"""
    while True:
        title = input(
            'Введите название задачи '
            '(или нажмите Enter, чтобы вернуться в меню): '
        ).strip()
        if not title:
            break

        task = manager.add(title)
        print(f'Задача добавлена с ID {task.id}.')
        break


def _process_task(method_name: str, success_message: str):
    """Общая функция для обработки задач (удаление/отметка)"""
    while True:
        try:
            task_id = input(
                'Введите ID задачи: '
                '(или нажмите Enter, чтобы вернуться в меню): ')
            if not task_id:
                break
            method = getattr(manager, method_name)

            if method(int(task_id)):
                print(f'Задача {success_message}.')
                break

            print('Задача с таким ID не найдена.')

        except ValueError:
            print('ОШИБКА: ID должен быть целым числом.')


def _exit_app():
    """Выход из приложения."""
    print('Выход...')
    sys.exit()
