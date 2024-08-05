import random
import os
import time

# Set up the game grid
grid_size = 10
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# Player position
player_position = [grid_size // 2, grid_size - 1]

# Alien position
alien_position = [random.randint(0, grid_size - 1), 0]

# Game loop
while True:
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Update player and alien positions
    grid[player_position[1]][player_position[0]] = 'P'
    grid[alien_position[1]][alien_position[0]] = 'A'

    # Display the grid
    for row in grid:
        print(' '.join(row))

    # Get user input
    move = input("Move left (L) or right (R)? Press 'Q' to quit: ").upper()

    # Quit the game
    if move == 'Q':
        break

    # Move player
    grid[player_position[1]][player_position[0]] = ' '
    if move == 'L' and player_position[0] > 0:
        player_position[0] -= 1
    elif move == 'R' and player_position[0] < grid_size - 1:
        player_position[0] += 1

    # Move alien
    grid[alien_position[1]][alien_position[0]] = ' '
    alien_position[1] += 1

    # Check for collision
    if player_position == alien_position:
        print("Game Over! Alien ship reached the player.")
        break

    # Check if the player shot down the alien
    if alien_position[1] == grid_size - 1:
        print("You shot down the alien ship! You win!")
        break

    # Introduce some delay to make the game playable
    time.sleep(0.1)

