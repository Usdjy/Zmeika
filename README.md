# Zmeika
For Players:
This the famous game "Snake".
It's launched by python game.py
The menu allows user to choose between 3 levels, that are ranked according to their complexity. To scroll up and down use keys with arrows.
To choose the level press space.
The game map is a closed subset of R^2, at the size of 60x40 snake blocks (600x400 pixels). To start the game press any of the keys WASD, that will be used for 
control. Initially, snake is at the center of the screen with the speed 5 on level 0, 10 on level 1 and 15 on level 2.
On each level, there are rocks. Player should not touch rocks with the head of the snake, otherwise it dies.
During the game player should eat the food (green apples) to achieve points.
The food spawns at random spot on the map (cannot spawn on the rock, it'd be unfair). After the food is eaten, it spawns again, player gets one point and the snake
gets one block longer. 
Reminder of the classic rules:
  Snake dies if it touches itself.
  Snake dies if it touches the border of the map.
When the game is finished (snake is dead), user can restart the game (press C) or quit to the menu (press Q).

For developers:
In this project we use 4 classes(Button, Snake, Rock, Food)

Food:
     This class represents the food that is eaten by the snake
     Attributes:
                   pts(int) - the amount of points that is given for eating this type of food
                   x(int) - x coordinate of food's position
                   y(int) - y coordinate of food's position
                   eaten(bool) - variable that is True if the piece is eaten, False otherwise
    
Rock:
     This class represents rocks, that serve as obstacles on snake's way
     Attributes:   x(int) - x coordinate of rock's position
                   y(int) - y coordinate of rock's position  
    
Snake:
     Class that represents the snake, which is the main object of the game
     Attributes:   Head([int, int]) - list with x and y coordinates of snake's head position
                   parts(list) - 2D list of the coordinates of each piece of the snake
                   x(int) - x coordinate of new head's position
                   y(int) - y coordinate of new head's position
                   dx(int) - "x component of snake's velocity": negative when it's moving to the left,
                                                                positive when it's moving to the right,
                                                                0 when it's moving vertically
                   dy(int) - same as dx, but for y-axis
                   len(int) - the current length of the snake
                   alive(bool) - variable that is False when the snake is dead, True otherwise
                   speed(int) - the speed of the snake. Rises when the snake eats food (obviously, it gains energy);
                                the base speed depends on the chosen level
    
Button:
     This class represents the buttons, that are used as a form of interactive interaction with the user
     Attributes:   name(str) - "name" of the button - the phrase which is written on it
                   chosen(bool) - the variable that is True when the button is "active" (it is lit), False otherwise
                   x(int) - x coordinate of the top left corner of the button
                   y(int) - y coordinate of the top left corner of the button    
