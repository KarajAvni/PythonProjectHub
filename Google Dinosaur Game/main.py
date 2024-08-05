import time
import pyautogui

# Function to press the space key
def jump():
    pyautogui.press('space')

# Main loop to play the game
def play_dinosaur_game():
    print("Get ready to play the Google Dinosaur Game!")
    time.sleep(2)  # Give some time to focus on the game

    while True:
        # Press space to make the dinosaur jump
        jump()

        # Adjust the sleep time based on the game's speed
        time.sleep(0.1)

# Run the game
if __name__ == "__main__":
    play_dinosaur_game()

