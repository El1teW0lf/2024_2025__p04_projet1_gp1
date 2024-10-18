import random
import time
import sys
import os

# List of emojis (Unicode)
emojis = ["😀", "😎", "😂", "😜", "😍", "🤖", "👽", "🐱", "🐶", "🍕", "🎉", "🚀", "⚽"]

# Function to generate a random ANSI color code
def random_color():
    return f"\033[38;5;{random.randint(0, 255)}m"

# Function to move the cursor to a specific position
def move_cursor(x, y):
    # ANSI escape sequence for cursor movement
    print(f"\033[{y};{x}H", end='')

# Function to hide/show the cursor
def hide_cursor(hide=True):
    print("\033[?25l" if hide else "\033[?25h", end='')

# Function to reset ANSI colors and cursor visibility
def reset_terminal():
    print("\033[0m", end='')  # Reset color
    hide_cursor(False)  # Show cursor again

# Function to print emojis at random positions
def print_emojis():
    # Get the terminal size
    rows, cols = os.get_terminal_size()

    for _ in range(200):  # Number of emojis to print
        # Choose random coordinates within terminal size
        x = random.randint(1, cols )  # Leave some margin
        y = random.randint(1, rows )
        
        # Choose a random emoji and color
        emoji = random.choice(emojis)
        color = random_color()

        # Move cursor and print emoji at the random position
        move_cursor(x, y)
        print(f"{color}{emoji}", end='')

# Main loop
try:
    # Hide the cursor
    hide_cursor(True)

    while True:
        # Print random emojis at random locations
        print_emojis()

        # Wait for 1/20th of a second to maintain 20 FPS
        time.sleep(1/20)

except KeyboardInterrupt:
    # Reset terminal settings on exit
    reset_terminal()
    sys.exit(0)
