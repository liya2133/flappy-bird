# Gesture Controlled Flappy Bird

## Overview

Gesture Controlled Flappy Bird is a computer vision-based game developed using Python, Pygame, and MediaPipe. Instead of using a keyboard or mouse, the player controls the bird using hand gestures detected through a webcam. The project demonstrates the integration of real-time hand tracking with a classic arcade game.

## Features

* Real-time hand gesture recognition using MediaPipe.
* Control the bird without touching the keyboard.
* Smooth gameplay built with Pygame.
* Obstacle generation with moving pipes.
* Collision detection and score tracking.
* Beginner-friendly and lightweight implementation.

## Technologies Used

* Python
* Pygame
* MediaPipe
* OpenCV

## Project Structure

```
Gesture-Controlled-Flappy-Bird/
│
├── assets/
│   ├── background.png
│   ├── bird.png
│   ├── pipe.png
│   └── ...
│
├── main.py
├── bird.py
├── pipe.py
├── hand_tracking.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Gesture-Controlled-Flappy-Bird.git
```

2. Navigate to the project folder:

```bash
cd Gesture-Controlled-Flappy-Bird
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python main.py
```

## How to Play

1. Ensure your webcam is connected.
2. Launch the game.
3. Keep your hand visible to the camera.
4. Raise or lower your hand to control the bird's movement.
5. Avoid hitting the pipes and try to achieve the highest score.

## Requirements

* Python 3.10 or later
* Webcam
* Pygame
* OpenCV
* MediaPipe

## Future Enhancements

* Multiple difficulty levels.
* Sound effects and background music.
* Pause and restart functionality.
* High-score leaderboard.
* Improved gesture recognition and smoother gameplay.

## Author

**Liya Sebastian**

MCA Student | Federal Institute of Science and Technology (FISAT)

## License

This project is created for educational and learning purposes.
