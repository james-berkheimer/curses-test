
import curses
from curses import wrapper

def main(stdscr):  # pragma: no cover
    stdscr.clear()
    stdscr.addstr("Hello World")
    stdscr.refresh()
    stdscr.getch()    

wrapper(main)
