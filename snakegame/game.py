import curses
from curses import textpad
import random

def gen_food(stdscr):

    sh, sw = stdscr.getmaxyx()

    food = [
        random.randint(4, sh - 4),
        random.randint(4, sw - 4) 
    ]

    return food

def game(stdscr):

    # turn off the default cursor
    curses.curs_set(False)

    stdscr.nodelay(True)
    # million seconds
    stdscr.timeout(1000)

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

    # set the default moving direction for snake.
    direction = curses.KEY_RIGHT

    food_ch = "*"
    food = gen_food(stdscr)
    stdscr.addstr(food[0], food[1], food_ch)

    while True:

        # holde the screen the see the snake.
        # userkey will be -1 if timeout in nodelay mode.
        userkey = stdscr.getch()

        if userkey in [ ord('q') ]:
            break
        elif userkey in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        # move the snake one unit right.
            direction = userkey 

        # get the current head
        head = snake[0]
        # calc the new head coordinates based on the direction.
        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
        # paint the new head
        stdscr.addstr(new_head[0], new_head[1], snake_ch)
        # add new head to the snake variable.
        snake.insert(0, new_head)
        # erease the tail unit.
        stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
        snake.pop()

    stdscr.getch()

curses.wrapper(game)