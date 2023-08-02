# project_18_turtle_crossing
The provided code is a simplified implementation of the classic game Frogger. It consists of three classes:

1. CarManager class: Manages the cars moving across the screen. It creates cars randomly, moves them horizontally from right to left, and increases their speed as the game progresses.

2. Player class: Represents the player-controlled turtle character. It allows the player to move the turtle up and down, resets the turtle to the starting position, and checks if the turtle has reached the finish line.

3. Scoreboard class: Displays the current level of the game on the screen. It updates the level whenever the player successfully crosses the road and displays "Game Over" when the player collides with a car.

In the main code section, a Screen object is created to set up the game screen. An instance of the Player class is created, which responds to user input to move the turtle up and down. An instance of the CarManager class is also created, which generates cars and moves them horizontally. Additionally, a Scoreboard object is created to display the level.

The game loop runs continuously until the player collides with a car. Within the loop, the cars are created, moved, and their collisions with the player are detected. If the player successfully reaches the finish line, the level is incremented, and the car speed is increased. When the game ends, the "Game Over" message is displayed.

The game is controlled by user input and exits when the screen is clicked.

In summary, this code implements a simplified version of the Frogger game. The player controls a turtle character and tries to cross the road while avoiding moving cars. The game keeps track of the level, increases the car speed, and displays the level and "Game Over" message on the screen.
