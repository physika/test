import curses
import random

# Constants for the game dimensions
HEIGHT = 20
WIDTH = 40

# Directions mapped to coordinate deltas
DIRECTIONS = {
    curses.KEY_UP: (-1, 0),
    curses.KEY_DOWN: (1, 0),
    curses.KEY_LEFT: (0, -1),
    curses.KEY_RIGHT: (0, 1),
}

def main(stdscr):
    # Set up curses
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)

    # Initial snake position: center
    snake = [(HEIGHT // 2, WIDTH // 2)]
    direction = curses.KEY_RIGHT

    # Place the first food
    food = (random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2))

    while True:
        # Input handling
        key = stdscr.getch()
        if key in DIRECTIONS:
            direction = key
        elif key == ord('q'):
            break

        # Calculate new head position
        dy, dx = DIRECTIONS.get(direction, (0, 0))
        head_y, head_x = snake[0]
        new_head = (head_y + dy, head_x + dx)

        # Check collisions with wall or self
        if (
            new_head[0] in (0, HEIGHT - 1)
            or new_head[1] in (0, WIDTH - 1)
            or new_head in snake
        ):
            break

        # Add new head to the snake
        snake.insert(0, new_head)

        # Check for food consumption
        if new_head == food:
            food = (random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2))
        else:
            snake.pop()

        # Draw the board
        stdscr.clear()
        # Draw borders
        for x in range(WIDTH):
            stdscr.addch(0, x, '#')
            stdscr.addch(HEIGHT - 1, x, '#')
        for y in range(HEIGHT):
            stdscr.addch(y, 0, '#')
            stdscr.addch(y, WIDTH - 1, '#')

        # Draw food
        stdscr.addch(food[0], food[1], '*')

        # Draw snake
        for y, x in snake:
            stdscr.addch(y, x, 'o')

        stdscr.refresh()
        curses.napms(100)

if __name__ == '__main__':
    curses.wrapper(main)
