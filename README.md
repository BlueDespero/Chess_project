# Chess_project

1. Description

    This repository contains everything you need to play a game of chess with a friend. Sit comfortably with someone you like and enjoy the game of kings.

    Presented simulation of the game includes special moves like promotion, castling and En Passant. When you select a figure you will be presented with all the  moves it  can perform in current game state. If a checkmate occurs game will let you know with a pop-up window informing who has won. Case of pat is also taken into account (will cause a pop-up). 

2. Running

    To start a game you can use a command:

        python chess.py

    Or you can use a docker container based on a provided Dockerfile. Going with the latter is more reliable because it will ensure you have all the required python libraries. Start by building an image with command:

        sudo docker build -t chess_docker .

    When build is completed you can start your container with:

        sudo sh start.sh

    And that is all!

3. Goals

    + Adding the option of playing online
    + Adding settings for custom games (like time limits or starting from different arrangements)
    + Creating a single player mode where user will compete with computer
