from file_functions import *
from ui_functions import *
def parse_command(command, stdscr, left_win, right_win, command_win):
    args = command.split()
    if not args:
        return
    cmd = args[0].lower()
    if cmd == 'cd' and len(args) > 1:
        message = change_directory(args[1])
        update_status(stdscr, message)
        new_contents = list_directory('.')
        draw_window(new_contents, left_win)  # Перерисовка окна с новым содержимым
        refresh_windows(stdscr, left_win, right_win, command_win)



def log_event(event):
    with open("file_manager_log.txt", "a") as log_file:
        log_file.write(f"{event}\n")

def exit_program(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    print("Программа завершена корректно.")


