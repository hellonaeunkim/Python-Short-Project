# project_22_us_states_game

This code is a U.S. States guessing game using the turtle graphics module and pandas library:

1. It imports the required modules and sets up the turtle graphics window.
2. The image of the U.S. map is loaded and set as the shape of the turtle.
3. The States class is defined, which is responsible for writing the guessed states on the map.
4. The data from the "50_states.csv" file is loaded using pandas, and a list of all the states is created.
5. The game loop starts, prompting the user to enter the name of a state.
6. If the entered state is correct, it is added to the guessed_states list, and its coordinates are obtained from the data to be written on the map.
7. If the user enters "Exit," the loop breaks, and the missing states are identified by comparing the guessed states with all the states. The missing states are then saved to a new CSV file named "states_to_learn.csv."
8. The write_state method in the States class is used to write the guessed states on the turtle graphics window.

Overall, the code allows users to guess the names of U.S. states and displays them on a map using the turtle graphics module.
