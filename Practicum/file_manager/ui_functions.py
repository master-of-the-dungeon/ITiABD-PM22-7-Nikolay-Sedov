import curses
from file_functions import *

def init_ui():
    stdscr = curses.initscr()  
    curses.noecho()  
    curses.cbreak()  
    stdscr.keypad(True)  
    return stdscr

def draw_window(contents, window):
    window.clear()
    for idx, item in enumerate(contents):
        if idx < window.getmaxyx()[0] - 1:
            window.addstr(idx + 1, 1, item)
    window.box()
    window.refresh()

def refresh_windows(stdscr, left_win, right_win, command_win):
    stdscr.refresh()
    left_win.refresh()
    right_win.refresh()
    command_win.refresh()


def handle_key_press(key, stdscr, left_panel, right_panel, command_win):
    if key == curses.KEY_UP:  
       
        pass
    elif key == curses.KEY_DOWN:  
        
        pass


def display_command_line(command_win):
    command_win.clear()
    command_win.addstr(0, 0, "Введите команду: ")
    command_win.refresh()
    curses.echo()  
    command_str = command_win.getstr().decode('utf-8')  
    curses.noecho()  
    return command_str


def update_status(stdscr, message):
    stdscr.addstr(0, 0, message)
    stdscr.refresh()

def exit_program(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def clear_command_line(command_win):
    command_win.clear()
    command_win.addstr(0, 0, "Команда: ")
    command_win.refresh()

def process_key_press(stdscr, left_win, right_win, current_panel):
    k = stdscr.getch()  # Считывание нажатой клавиши
    max_y, max_x = current_panel.getmaxyx()  # Получаем размеры текущего окна

    # В зависимости от текущего активного окна
    if k == curses.KEY_UP:
        # Код для перемещения курсора вверх
        pass
    elif k == curses.KEY_DOWN:
        # Код для перемещения курсора вниз
        pass
    elif k == curses.KEY_LEFT:
        # Переключить фокус на левую панель
        pass
    elif k == curses.KEY_RIGHT:
        # Переключить фокус на правую панель
        pass
    elif k == ord('q'):  # Выход из программы по нажатию 'q'
        exit_program(stdscr)
