import curses
from curses import textpad

def game(stdscr):

    # turn off the default cursor
    curses.curs_set(False)

    # get the size of the screen
    sh, sw = stdscr.getmaxyx()
    # paint the border
    textpad.rectangle(stdscr, 3, 3, sh - 3, sw - 3)

    # define the sanke body variable.
    snake = [
        [sh // 2, sw // 2 + 1],
        [sh // 2, sw // 2],
        [sh // 2, sw // 2 - 1]
    ]
    snake_ch = chr(9608)

    # paint the snake
    for item in snake:
        stdscr.addstr(item[0], item[1], snake_ch)

    while True:

        # holde the screen the see the snake.
        userkey = stdscr.getch()
        if userkey in [ ord('q') ]:
            break

        # move the snake one unit right.
        # get the current head
        head = snake[0]
        # calc the new head coordinates.
        new_head = [head[0], head[1] + 1]
        # paint the new head
        stdscr.addstr(new_head[0], new_head[1], snake_ch)
        # add new head to the snake variable.
        snake.insert(0, new_head)
        # erease the tail unit.
        stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
        snake.pop()

    stdscr.getch()

curses.wrapper(game)