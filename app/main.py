from interface import show_menu, action_choicer


def main() -> None:
    while True:
        show_menu()
        choice = input('Выберите действие: ').strip()
        action_choicer(choice)


if __name__ == '__main__':
    main()
