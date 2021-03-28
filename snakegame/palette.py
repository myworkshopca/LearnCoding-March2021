import curses

def colors(stdscr):

    curses.start_color()
    curses.use_default_colors()

    stdscr.addstr(2, 0, "")
    #for i in range(0, curses.COLORS):
    for i in range(0, 20):
        # initialize the color pair
        curses.init_pair(i + 1, i, -1)

        y = 1
        #if i < 16:
        x = i * 3 
        stdscr.addstr(y, x, "{0}".format(chr(9608) * 3), curses.color_pair(i + 1))
        #stdscr.addstr("[{0}{1}]".format(str(i + 1), chr(9608) * 2), curses.color_pair(i + 1))

    stdscr.getch()

curses.wrapper(colors)