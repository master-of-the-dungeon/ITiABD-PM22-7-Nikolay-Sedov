import curses
from file_functions import *
from ui_functions import *
from util import *

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

    # Отрисовка начального состояния окон
    left_contents = list_directory('.')
    draw_window(left_contents, left_win)
    right_contents = list_directory('.')
    draw_window(right_contents, right_win)

    # Главный цикл
    while True:
        command_str = display_command_line(command_win)
        if command_str.lower() == 'exit':
            break

        parse_command(command_str, stdscr, left_win, right_win, command_win)
        refresh_windows(stdscr, left_win, right_win, command_win)

    # Выход из программы
    exit_program(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
