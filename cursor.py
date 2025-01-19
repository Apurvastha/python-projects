import pyautogui
import time
import random
import sys
from datetime import datetime

def move_mouse():
    """
    Moves the mouse cursor slightly in random directions at regular intervals
    to prevent system from locking.
    """
    try:
        # Get screen size
        screen_width, screen_height = pyautogui.size()
        
        print("Mouse movement started. Press Ctrl+C to stop.")
        print(f"Screen resolution: {screen_width}x{screen_height}")
        
        while True:
            # Get current mouse position
            current_x, current_y = pyautogui.position()
            
            # Generate random movement between -10 and 10 pixels
            move_x = random.randint(-10, 10)
            move_y = random.randint(-10, 10)
            
            # Ensure new position stays within screen bounds
            new_x = max(0, min(current_x + move_x, screen_width))
            new_y = max(0, min(current_y + move_y, screen_height))
            
            # Move mouse smoothly to new position
            pyautogui.moveTo(new_x, new_y, duration=0.5)
            
            # Log movement
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"[{current_time}] Moved mouse to ({new_x}, {new_y})")
            
            # Wait for 30 seconds before next movement
            time.sleep(10)
             
    except KeyboardInterrupt:
        print("\nMouse movement stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    move_mouse()