import random

def generate_food(tly, tlx, bry, brx):

    c = [
        random.randint(tly, bry), 
        random.randint(tlx, brx)
    ]

    food_ch = "*"
    
    stdscr.addstr()
    print(c)

generate_food(3, 3, 20, 50)