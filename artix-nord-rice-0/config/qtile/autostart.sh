#!/usr/bin/bash

picom &
wired &
nitrogen --restore &
udiskie &
blueman-applet &
nm-applet &
lxsession &
eww daemon
#eww --config /home/lnn0q/.config/eww/ open dashboard
#volumeicon &

eval ssh-agent $SHELL &
ssh-add ~/.ssh/id_rsa-git
ssh-add -l
