import curses

"""
The function to calculate the next coordinates for the given tetriminos.
Prameters:
tetrimino the given tetrimino
type of the tetrimino
direction the moveing direction for this tetrimino
Return:
it will return a tuple:
(new_yxs, erase_yxs, new_mino)
"""
def calc_next_yxs(tetrimino, type, direction):

    return

def tetris(stdscr):

    curses.curs_set(False)

    stdscr.addstr(1, 20, 'Move Tetriminos...')
    stdscr.addstr(2, 20, 'Press "q" to exit! Any other key to move!')

    # define the character for each block of a tetrimino
    block_ch = chr(9609)
    # eraser character.
    eraser_ch = ' '

    # define the initial coordinates for a tetrimino
    mino = [
        [4,3], [4,5], [5,5], [5,3]
    ]

    # paint the tetrimino
    for unit in mino:
        stdscr.addstr(unit[0], unit[1], block_ch)

    # the moving loop...
    while True:
        key = stdscr.getch()

        if key == ord('q'):
            break

        # assume move to right
        # calculate the new (y, x).
        new_yxs = [
            [mino[1][0], mino[1][1] + 2],
            [mino[2][0], mino[2][1] + 2]
        ]
        # calculate the erase y,x
        erase_yxs = [
            [mino[0][0], mino[0][1]],
            [mino[3][0], mino[3][1]]
        ]
        # record the new coordinates for the tetriminos,
        # so we can move next loop!
        mino = [
           mino[1], new_yxs[0], new_yxs[1], mino[2]
        ]
        # paint the block characters and eraser characters to make the
        # tetrimino move.
        for unit in new_yxs:
            stdscr.addstr(unit[0], unit[1], block_ch)
        for unit in erase_yxs:
            stdscr.addstr(unit[0], unit[1], eraser_ch)

curses.wrapper(tetris)