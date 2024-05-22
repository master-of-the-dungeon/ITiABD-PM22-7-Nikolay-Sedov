import curses

def test(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello, world!")
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(test)
