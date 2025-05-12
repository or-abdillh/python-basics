import curses
from random import randint

# Setup window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)  # Create a window with height 20 and width 60
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# Snake and food
snake = [[4, 10], [4, 9], [4, 8]]  # Initial snake position
food = [10, 20]  # Initial food position
win.addch(food[0], food[1], '*')  # Display food

# Game logic
key = curses.KEY_RIGHT  # Initial direction
score = 0

while True:
    win.addstr(0, 2, f'Score: {score} ')  # Display score
    win.timeout(100 - (len(snake) // 5 + len(snake) // 10) % 10)  # Speed adjustment

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN, 27]:
        key = prev_key

    # Calculate the next position of the snake's head
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    # Insert new head
    snake.insert(0, [y, x])

    # Check if snake eats food
    if snake[0] == food:
        score += 1
        food = []
        while food == []:
            food = [randint(1, 18), randint(1, 58)]
            if food in snake:
                food = []
        win.addch(food[0], food[1], '*')
    else:
        # Remove snake's tail
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    # Check for collision
    if (snake[0][0] in [0, 19] or
        snake[0][1] in [0, 59] or
        snake[0] in snake[1:]):
        break

    # Render snake
    win.addch(snake[0][0], snake[0][1], '#')

curses.endwin()
print(f"Game Over! Your score is {score}")