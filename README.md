# robot
## Robot Face
This script creates a graphical interface using Pygame to display a robot face that responds to text input by speaking and animating its mouth. The robot face's eyes also follow the mouse cursor.

## Features
Robot Face Animation: The robot face has blue pixelated eyes that follow the mouse cursor and a mouth that animates when the robot is speaking.
Text-to-Speech (TTS): The robot converts text from a file to speech using the pyttsx3 library.
File Monitoring: The script monitors a text file for changes and updates the robot's speech accordingly.

## Requirements
Python 3.x
Pygame
pyttsx3
threading

## Installation
Install Pygame:
``
pip install pygame
``

## Install pyttsx3:

``
pip install pyttsx3
``

## Usage
### Run the Script:

`` 
python robot_face.py
``

### Interact with the Robot Face:

The robot face will follow your mouse cursor with its eyes.
To test the text-to-speech functionality, create or update the input/text.txt file with the text you want the robot to speak. The robot will read and speak the new text automatically.
Click the mouse to make the robot say "Hello world."

## Script Overview

### Initialization:

Initializes Pygame and sets up the display window.
Defines colors and screen dimensions.

### Functions:

draw_eyes(surface, eye_x, eye_y, eye_width, eye_height): Draws the robot's eyes.
draw_mouth(surface, is_speaking, mouth_frame): Draws the robot's mouth, which animates when speaking.
tts(text, filename): Converts text to speech and saves it as an audio file.
speak(filename): Plays the saved audio file in a separate thread.
check_file(filename): Monitors the text file for changes and triggers TTS and speaking functions.

### Main Loop:

Handles events such as window resizing and mouse clicks.
Updates the robot face's eye positions based on the mouse cursor.
Calls functions to draw the eyes and mouth.
Monitors the text file and updates speech accordingly.


## Notes
Ensure the input/text.txt file exists and is accessible.
Audio files are saved in the audio/ directory. Make sure this directory exists or modify the paths in the script as needed.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Andrew Ziadeh
