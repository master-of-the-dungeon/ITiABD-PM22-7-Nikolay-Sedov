import curses
import os
import platform
from file_functions import *
from ui_functions import *
from util import *

def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        os.system(f"open '{path}'")
    else:
        os.system(f"xdg-open '{path}'")

def display_command_line(command_win):
    command_win.clear()
    command_win.addstr(0, 0, "Введите команду: ")
    command_win.refresh()
    curses.echo()  # Включить отображение вводимых символов
    command_str = command_win.getstr().decode('utf-8').strip()
    curses.noecho()  # Отключить отображение вводимых символов после ввода
    return command_str

def draw_aliases(stdscr, aliases, start_y, start_x):
    stdscr.attron(curses.color_pair(1))
    for i, alias in enumerate(aliases):
        stdscr.addstr(start_y + i, start_x, alias)
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

def main(stdscr):
    # Инициализация интерфейса и базовые настройки
    stdscr.clear()
    curses.curs_set(0)  # Скрыть курсор
    stdscr.keypad(True) # Разрешить специальные клавиши
    max_y, max_x = stdscr.getmaxyx()

    # Создание окон
    left_win = curses.newwin(max_y, max_x // 2, 0, 0)
    command_win = curses.newwin(1, max_x, max_y - 1, 0)

    left_win.keypad(True)
    command_win.keypad(True)

    # Инициализация цветов
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    aliases = [
        "F1: Создать папку", "F2: Удалить папку", "F3: Удалить файл", 
        "F4: Копировать файл", "F5: Переместить файл", "F6: Переименовать файл", 
        "F7: Открыть файл", "F8: Список файлов", "F9: Сменить директорию", 
        "F10: Свойства файла"
    ]

    # Отрисовка начального состояния окон
    left_contents = list_directory('.')
    draw_window(left_contents, left_win)
    draw_aliases(stdscr, aliases, 0, max_x // 2 + 1)

    selected_index = 0
    mode = "navigation"  # Режим "command" или "navigation"

    # Главный цикл
    while True:
        draw_window(left_contents, left_win, selected_index)
        draw_aliases(stdscr, aliases, 0, max_x // 2 + 1)
        command_win.clear()
        command_win.addstr(0, 0, "Введите команду: ")
        command_win.refresh()
        key = left_win.getch()

        if key == curses.KEY_UP:
            selected_index = max(0, selected_index - 1)
        elif key == curses.KEY_DOWN:
            selected_index = min(len(left_contents) - 1, selected_index + 1)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            selected_item = left_contents[selected_index]
            if selected_item == "..":
                change_directory("..")
                left_contents = list_directory('.')
                selected_index = 0
            elif os.path.isdir(selected_item):
                change_directory(selected_item)
                left_contents = list_directory('.')
                selected_index = 0
            else:
                open_file(selected_item)
        elif key == 9:  # клавиша Tab
            mode = "command"
            curses.echo()
            command = command_win.getstr().decode('utf-8').strip()
            curses.noecho()
            if command.lower() == 'exit':
                break
            parse_command(command, stdscr, left_win, left_win, command_win)  # обновление только левого окна
            left_contents = list_directory('.')
            selected_index = 0
            refresh_windows(stdscr, left_win, left_win, command_win)
        
        # Обработка нажатий клавиш F1-F12
        elif key == curses.KEY_F1:
            # Создание новой папки
            command_win.addstr(0, 0, "Введите имя новой папки: ")
            command_win.refresh()
            curses.echo()
            folder_name = command_win.getstr().decode('utf-8').strip()
            curses.noecho()
            message = create_directory(folder_name)
            update_status(stdscr, message)
            left_contents = list_directory('.')
        elif key == curses.KEY_F2:
            # Удаление папки
            command_win.addstr(0, 0, "Введите имя папки для удаления: ")
            command_win.refresh()
            curses.echo()
            folder_name = command_win.getstr().decode('utf-8').strip()
            curses.noecho()
            message = remove_directory(folder_name)
            update_status(stdscr, message)
            left_contents = list_directory('.')
        elif key == curses.KEY_F3:
            # Удаление файла
            command_win.addstr(0, 0, "Введите имя файла для удаления: ")
            command_win.refresh()
            curses.echo()
            file_name = command_win.getstr().decode('utf-8').strip()
            curses.noecho()
            message = delete_file(file_name)
            update_status(stdscr, message)
            left_contents = list_directory('.')
        elif key == curses.KEY_F4:
            # Копирование файла
            command_win.addstr(0, 0, "Введите источник и место назначения для копирования файла (через пробел): ")
            command_win.refresh()
            curses.echo()
            paths = command_win.getstr().decode('utf-8').strip().split()
            curses.noecho()
            if len(paths) == 2:
                message = copy_file(paths[0], paths[1])
            else:
                message = "Неверный формат ввода."
            update_status(stdscr, message)
            left_contents = list_directory('.')
        elif key == curses.KEY_F5:
            # Перемещение файла
            command_win.addstr(0, 0, "Введите источник и место назначения для перемещения файла (через пробел): ")
            command_win.refresh()
            curses.echo()
            paths = command_win.getstr().decode('utf-8').strip().split()
            curses.noecho()
            if len(paths) == 2:
                message = move_file(paths[0], paths[1])
            else:
                message = "Неверный формат ввода."
            update_status(stdscr, message)
            left_contents = list_directory('.')
        elif key == curses.KEY_F6:
            # Переименование файла или папки
            command_win.addstr(0, 0, "Введите старое и новое имя (через пробел): ")
            command_win.refresh()
            curses.echo()
            names = command_win.getstr().decode('utf-8').strip().split()
            curses.noecho()
            if len(names) == 2:
                message = rename_file(names[0], names[1])
            else:
                message = "Неверный формат ввода."
            update_status(stdscr, message)
            left_contents = list_directory('.')
        elif key == curses.KEY_F7:
            # Открытие файла
            command_win.addstr(0, 0, "Введите имя файла для открытия: ")
            command_win.refresh()
            curses.echo()
            file_name = command_win.getstr().decode('utf-8').strip()
            curses.noecho()
            message = open_file(file_name)
            update_status(stdscr, message)
            left_contents = list_directory('.')
        elif key == curses.KEY_F8:
            # Список файлов
            command_win.addstr(0, 0, "Введите путь для отображения списка файлов: ")
            command_win.refresh()
            curses.echo()
            path = command_win.getstr().decode('utf-8').strip()
            curses.noecho()
            left_contents = list_directory(path)
            update_status(stdscr, f"Содержимое директории {path}")
        elif key == curses.KEY_F9:
            # Сменить директорию
            command_win.addstr(0, 0, "Введите путь для смены директории: ")
            command_win.refresh()
            curses.echo()
            path = command_win.getstr().decode('utf-8').strip()
            curses.noecho()
            message = change_directory(path)
            update_status(stdscr, message)
            left_contents = list_directory('.')
        elif key == curses.KEY_F10:
            # Свойства файла
            command_win.addstr(0, 0, "Введите путь к файлу для отображения свойств: ")
            command_win.refresh()
            curses.echo()
            path = command_win.getstr().decode('utf-8').strip()
            curses.noecho()
            properties = get_file_properties(path)
            update_status(stdscr, str(properties))
        # Добавьте другие команды для F11-F12 по аналогии при необходимости

        refresh_windows(stdscr, left_win, left_win, command_win)

    # Выход из программы
    exit_program(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)