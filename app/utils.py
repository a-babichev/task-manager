import json
from typing import Any
from pathlib import Path

DATA_FILE = Path('data.json')


def load_data() -> list[dict[str, Any]]:
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open('r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_data(data: list[dict[str, Any]]) -> bool:
    try:
        with DATA_FILE.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except TypeError as e:
        print('ОШИБКА: Невозможно сохранить данные в JSON.')
        print(f'Причина: {e}')
        return False
    except OSError as e:
        print('ОШИБКА: Не удалось записать файл.')
        print(f'Причина: {e}')
        return False
    except Exception as e:
        print(f'Неожиданная ошибка: {e}')
        return False
