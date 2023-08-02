# project_17_pong_game
The provided code is a Python implementation of the classic Pong game. It consists of three classes:

1. ScoreBoard class: Manages the score display on the screen. It keeps track of the left and right scores, updates the scoreboard, and displays the scores using a turtle.

2. Paddle class: Represents the paddles used by the players to hit the ball. It creates the paddles, moves them up or down in response to user input, and ensures they stay within the game screen boundaries.

3. Ball class: Represents the ball used in the game. It creates the ball, moves it across the screen, bounces it off walls and paddles, and adjusts its speed as the game progresses.

In the main code section, the Screen class from the turtle module is used to set up the game screen. Paddle objects are created for both the left and right players, and their movement is controlled by the corresponding keys. A ball object is also created, and its movement and collisions are handled within the game loop. The ScoreBoard object keeps track of the scores and updates them accordingly.

The game loop continues until the game is over. The ball's speed gradually increases with each paddle collision, and the scores are updated when the ball goes out of bounds. The game screen is continuously updated, and the game exits when the screen is clicked.

In summary, this code implements the classic Pong game where two players control paddles to hit a ball back and forth. The paddles and ball are represented by separate classes, and the score is displayed on the screen. The game loop handles movement, collisions, and score updates.
