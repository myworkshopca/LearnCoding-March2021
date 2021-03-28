import curses

def hello(stdscr):

    # get the size of the screen.
    sh, sw = stdscr.getmaxyx();
    msg = "Welcome to my keyboard game! Press any key to start! Press ESC to exit!"
    stdscr.addstr(3, sw // 2 - len(msg) // 2, msg)

    while True:
        # get user's input.
        code = stdscr.getch()
        if code == 27:
            break
        # get ready message to paint
        msg = "ASCII Code {0}, Character: {1}".format(code, chr(code))
        stdscr.addstr(10, sw // 2 - len(msg) // 2, msg)

curses.wrapper(hello)