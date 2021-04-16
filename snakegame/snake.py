import curses
from curses import textpad
import random

def snake(stdscr):

    # hide the default cursor.
    curses.curs_set(False)

    stdscr.nodelay(True)
    interval = 200
    stdscr.timeout(interval)

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

    # set the default direction
    direction = curses.KEY_RIGHT

    # place the initial food.
    food_ch = "*"
    food = [
        random.randint(4, sh - 4),
        random.randint(4, sw - 4)
    ]
    stdscr.addstr(food[0], food[1], food_ch)

    while True:

        userkey = stdscr.getch()
        
        if userkey in [27, ord('q')]:
            break;

        if userkey in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = userkey

        head = snake[0]
        # calculate the new head toward right side one unit
        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]

        # paint the new head.
        stdscr.addstr(new_head[0], new_head[1], snake_ch)
        # store the new head.
        snake.insert(0, new_head)
        # check if the snake ate the food.
        if new_head != food:
            # what is length of the snake variable?
            # erase the tail by paint white space.
            stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()
        else:
            # place a new food
            food = [
                random.randint(4, sh - 4),
                random.randint(4, sw - 4)
            ]
            stdscr.addstr(food[0], food[1], food_ch)
            # make it faster by reduce the timeout interval
            interval = interval - 10
            stdscr.timeout(interval)

    stdscr.getch()

curses.wrapper(snake)