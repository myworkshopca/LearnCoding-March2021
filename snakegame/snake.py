import curses
from curses import textpad

def snake(stdscr):

    # hide the default cursor.
    curses.curs_set(False)

    sh, sw = stdscr.getmaxyx()

    textpad.rectangle(stdscr, 3, 3, sh - 3, sw -3)

    # snake variable
    snake = [
        [sh // 2, sw // 2 + 1],
        [sh // 2, sw // 2],
        [sh // 2, sw // 2 - 1],
    ]
    snake_ch = chr(9608)

    # 9608
    for unit in snake:
        stdscr.addstr(unit[0], unit[1], snake_ch)


    while True:
        stdscr.getch()

        head = snake[0]
        # calculate the new head
        new_head = [head[0], head[1] + 1]
        stdscr.addstr(new_head[0], new_head[1], snake_ch)
        # store the new head.
        snake.insert(0, new_head)
        # erase the tail by paint white space.
        stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
        snake.pop()

    stdscr.getch()

curses.wrapper(snake)