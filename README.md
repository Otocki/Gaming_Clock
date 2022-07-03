# Gaming_Clock 🎮⏱️

A python script that checks for how long were you playing a game.

## Instalation

To run this on your machine:
- ensure you have python installed
- download 'gaming_timer.py' file from this repository
- run 'gaming_timer.py' directly, from CLI or with any other prefered python interpreter
<p><br>*optionaly for Windows users:*</p>
- 'download 'uruchom_zegar.bat' script from this repository
- execute the .bat script


## Usage

Program will display a big digital clock in seperate window, showing current real time. Window will appear on the side of the screen, or on the secondary monitor.
This clock checks all of the running processes for stated games and calculates how long were they opened.

I wrote it to help both Me and my Mom, with controll over our gaming habits.
I realise this whole thing is still not perfect, and has a lot of problems.

## Internals

Script (to this date) consists of five functions:
**Window()**
whitch gives the timer window its size using tkinter module, and puts it on the top-right corner of the secondary screen,
**Clock_mechanism()**
that, with time module, updates the displayed time after every half a second,
**find_process()**
whitch uses psutil module to create a list of working processes that have a game title in their name,
**stoper()**
an addition to the clock, responsible for mesauring time spent on the game,
**fill_window()**
a series of tkinter lines that packs all of the above into readable lines inside the window.

## Issues

Main fixes and features that still need some work are:
+ games, or rather the names of their processes need to be inserted manually into the code
+ position of the window was calculated with screeninfo script, output numbers inserted into code manually
 it should be done automatically
+ kiling the timer for the game that is no longer running
+ checking for new processes on the spot
+ displaying separate timers for more than one active game
+ adjusting window geometry should be automatic.
+ timer final output could be logged for sake of statistics, and progress tracking
