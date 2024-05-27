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

def main(stdscr):
    # Инициализация интерфейса и базовые настройки
    stdscr.clear()
    curses.curs_set(0)  # Скрыть курсор
    stdscr.keypad(True) # Разрешить специальные клавиши
    max_y, max_x = stdscr.getmaxyx()

    # Создание окон
    left_win = curses.newwin(max_y - 1, max_x // 2, 0, 0)
    right_win = curses.newwin(max_y - 1, max_x // 2, 0, max_x // 2)
    command_win = curses.newwin(1, max_x, max_y - 1, 0)

    left_win.keypad(True)
    right_win.keypad(True)
    command_win.keypad(True)

    # Инициализация цветов
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Отрисовка начального состояния окон
    left_contents = list_directory('.')
    draw_window(left_contents, left_win)
    right_contents = list_directory('.')
    draw_window(right_contents, right_win)

    selected_index = 0
    mode = "navigation"  # Режим "command" или "navigation"

    # Главный цикл
    while True:
        draw_window(left_contents, left_win, selected_index)
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
            parse_command(command, stdscr, left_win, right_win, command_win)
            left_contents = list_directory('.')
            selected_index = 0
            refresh_windows(stdscr, left_win, right_win, command_win)

    # Выход из программы
    exit_program(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)

