# Zmeika
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
