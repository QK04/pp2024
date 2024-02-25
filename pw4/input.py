import curses

def get_int_input(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(0, 0, prompt)
    stdscr.refresh()

    value = int(stdscr.getstr().decode())
    return value
