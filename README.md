# Battleship

Battleship is a command-line game implemented in Python. The game allows players to load ship positions from a text file and play the classic game of Battleship by attempting to sink all enemy ships on the board.

## Features

- Load ship positions from a text file.
- Play the game by entering coordinates to shoot at.
- The game checks for hits, misses, and sunken ships.
- Display the game board after each move.

## Classes

### Ship

Represents a ship on the board. It has the following functionalities:
- Create a ship with a specific type and coordinates.
- Check if the ship is hit.
- Determine if the ship is sunk.

### Board

Represents the game board. It has the following functionalities:
- Create a 10x10 game board.
- Add ships to the board.
- Fire at a coordinate and check for hits or misses.
- Check if there are any ships left on the board.
- Convert coordinates from alphanumeric to numeric format.

### Game

Handles the game logic. It has the following functionalities:
- Load ship positions from a text file.
- Start the game loop and handle player input.
- Check for victory conditions.

## How to Play

1. Run the game by executing the `Battleship.py` file.
2. Enter the name of the file containing the ship positions.
3. Enter coordinates to shoot at (e.g., A5, B3, etc.).
4. The game will display the board and indicate hits, misses, and sunken ships.
5. Continue until all ships are sunk or you decide to quit by entering `q`.

## Example Ship File Format

The ship file should be a text file where each line represents a ship. The first item is the ship type, followed by its coordinates separated by semicolons. For example:

Battleship;A1;A2;A3;A4
Cruiser;B1;B2;B3
Destroyer;C1;C2
Submarine;D1

## Contact

For any questions or issues, please contact the author:

- Name: Eemil Soisalo
- Email: eemil.soisalo@tuni.fi
- Student ID: 150353416

Enjoy the game!
