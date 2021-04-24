import curses

#def init_play():
def simple(stdscr):

    stdscr.nodelay(True)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()

    body_ch = chr(9608)
    body = [
       sh // 2,
       sw // 2
    ]

    stdscr.addstr(body[0], body[1], body_ch)

    border_x = sw // 2 + 10
    # paint the border.
    for y in range(5, sh - 5):
        stdscr.addstr(y, border_x, chr(9474))

    # game loop
    while True:
        # play loop
        while True:
            key = stdscr.getch()
    
            new_body = [body[0], body[1] + 1]
            stdscr.addstr(new_body[0], new_body[1], body_ch)
            # erase the existing body.
            stdscr.addstr(body[0], body[1], " ")
            # update the body.
            body = new_body
    
            # check if game over, body touch border.
            if body[1] == border_x:
               # turn off no delay mode.
               stdscr.nodelay(False)
               stdscr.timeout(-1)
               # paint message.
               stdscr.addstr(3, 20, "GAME OVER!")
               stdscr.addstr(4, 20, "Press 'r' to restart, Press any other key to exit!")
               # break the play loop
               break

        key = stdscr.getch()
        if key == ord('r'):
            # restart game! 
            # clear screen.
            stdscr.addstr(3, 20, " " * 10)
            stdscr.addstr(4, 20, " " * 50)
            # initialize game.
            body = [
                sh // 2,
                sw // 2
            ]
            stdscr.nodelay(True)
            stdscr.timeout(100)
        else:
            # break the game loop!
            break;

curses.wrapper(simple)