import time
import sys
import os

texts = ["Hello, World!"]

def move_cursor(x, y):
    print(f"\033[{y};{x}H", end='')

def hide_cursor(hide=True):
    print("\033[?25l" if hide else "\033[?25h", end='')

def reset_terminal():
    hide_cursor(False)

def clear_line(y):
    move_cursor(0, y)  # Move to the start of the line
    print("\033[K", end='')  # ANSI escape code to clear the line

# Main loop to print moving text back and forth
def display_moving_text():
    # Get the terminal size
    cols, rows = os.get_terminal_size()

    text_index = 0  # Track which text from the list to display

    try:
        # Hide the cursor
        hide_cursor(True)

        x_position = 0  # Start from the left-most position
        direction = 1  # 1 for moving right, -1 for moving left
        text = texts[text_index]  # Get the current text
        y = rows // 2  # Center vertically

        while True:
            # Clear the current line before moving
            clear_line(y)

            # Move cursor to the current position and print the text
            move_cursor(x_position, y)
            print(f"{text}", end='', flush=True)

            # Update the horizontal position for the next frame
            x_position += direction

            # If the text reaches the right edge, change direction to left
            if x_position + len(text) >= cols:
                direction = -1  # Start moving left

            # If the text reaches the left edge, change direction to right
            if x_position <= 0:
                direction = 1  # Start moving right

            # Control the speed of the movement
            time.sleep(0.05)

    except KeyboardInterrupt:
        # Reset terminal settings on exit
        reset_terminal()
        sys.exit(0)

# Run the main display loop
if __name__ == "__main__":
    display_moving_text()
