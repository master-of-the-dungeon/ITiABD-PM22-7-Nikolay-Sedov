import curses
from file_functions import *

def init_ui():
    stdscr = curses.initscr()  
    curses.noecho()  
    curses.cbreak()  
    stdscr.keypad(True)  
    return stdscr

def draw_window(contents, window, selected_index=0):
    window.clear()
    for idx, item in enumerate(contents):
        if idx < window.getmaxyx()[0] - 1:
            if idx == selected_index:
                window.attron(curses.color_pair(1))
                window.addstr(idx + 1, 1, item)
                window.attroff(curses.color_pair(1))
            else:
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
    stdscr.clrtoeol()
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

    if k == curses.KEY_UP:
        pass
    elif k == curses.KEY_DOWN:
        pass
    elif k == curses.KEY_LEFT:
        pass
    elif k == curses.KEY_RIGHT:
        pass
    elif k == ord('q'):
        exit_program(stdscr)

def draw_status_bar(stdscr, messages):
    height, width = stdscr.getmaxyx()
    lines = []
    current_line = ""
    
    for message in messages:
        if len(current_line) + len(message) + 3 > width:  # +3 for " | "
            lines.append(current_line)
            current_line = message
        else:
            if current_line:
                current_line += " | " + message
            else:
                current_line = message
    
    if current_line:
        lines.append(current_line)
    
    stdscr.attron(curses.color_pair(1))
    for i, line in enumerate(lines):
        stdscr.addstr(height - len(lines) + i, 0, line)
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()




