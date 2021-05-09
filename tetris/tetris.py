import curses

def tetris(stdscr):

    curses.curs_set(False)

    #stdscr.addstr(1, 3, chr(9608))
    #stdscr.addstr(1, 4, chr(9608))
    #stdscr.addstr(2, 3, chr(9608))
    #stdscr.addstr(2, 4, chr(9608))
    
    # 2 x 2 square
    stdscr.addstr(5, 3, chr(9609))
    stdscr.addstr(5, 5, chr(9609))
    stdscr.addstr(6, 3, chr(9609))
    stdscr.addstr(6, 5, chr(9609))

    # line
    stdscr.addstr(5, 9, chr(9609))
    stdscr.addstr(5, 11, chr(9609))
    stdscr.addstr(5, 13, chr(9609))
    stdscr.addstr(5, 15, chr(9609))

    # l shape
    stdscr.addstr(5, 23, chr(9609))
    stdscr.addstr(6, 19, chr(9609))
    stdscr.addstr(6, 21, chr(9609))
    stdscr.addstr(6, 23, chr(9609))
    
    stdscr.addstr(8, 19, chr(9609))
    stdscr.addstr(9, 19, chr(9609))
    stdscr.addstr(10, 19, chr(9609))
    stdscr.addstr(10, 21, chr(9609))

    stdscr.getch()
    
    # move the 2x2 square Down.
    stdscr.addstr(7, 3, chr(9609))
    stdscr.addstr(7, 5, chr(9609))
    stdscr.addstr(5, 3, ' ')
    stdscr.addstr(5, 5, ' ')

    stdscr.getch()

    # move the 2x2 square Right.
    stdscr.addstr(6, 7, chr(9609))
    stdscr.addstr(7, 7, chr(9609))
    stdscr.addstr(6, 3, ' ')
    stdscr.addstr(7, 3, ' ')

    stdscr.getch()

curses.wrapper(tetris)