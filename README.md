#Simple "Game of Life" in Python

This simple python program is an implementation of Conway's Game of Life ([Wikipedia](https://en.wikipedia.org/wiki/Conway's_Game_of_Life)).  
It provides a command line interface with a few known patterns and you have the ability to enter your own patterns and fields.

Here you can see a pulsar ([ttyrec](http://0xcc.net/ttyrec/index.html.en) and [ttygif](https://github.com/icholy/ttygif) made it seem a bit slow, but it's actually very smooth):  

![](tty.gif)

##Patterns
* Blinker
* Toad
* Beacon
* Pulsar
* Glider
* Lightweight spaceship
* Glider gun

##Custom mode
For the custom mode of the game, you first will be asked to give the dimensions of the field (height and width).  
After that, the field has to be entered, with 0s for dead cells and 1s for living cell. These are separated by spaces.  
At the end you can define the iterations and the speed (in seconds) with which the particular states should change.  
###Example:
```
Height: 5
Width: 3
0 0 0
0 0 0
1 1 1
0 0 0
0 0 0
Iterations: 10
Speed in seconds (for example 0.5): 1
```
