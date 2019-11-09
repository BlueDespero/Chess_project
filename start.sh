#!/bin/bash
sudo docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -it --rm chess_docker /workspace/run.sh