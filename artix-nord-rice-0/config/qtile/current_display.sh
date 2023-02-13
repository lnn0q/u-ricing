#!/usr/bin/bash
nitrogen --restore &
killall dunst &
if [[ $1 -eq 1 ]]
then
    xrandr --output DP1 --mode 2560x1440 --rate 144 --output eDP1 --off
    notify-send Display=DP1 &
elif [[ $1 -eq 2 ]]
then
    xrandr --output eDP1 --mode 1536x1024 --rate 60 --output DP1 --off
    notify-send Display=eDP1 &
elif [[ $1 -eq 3 ]]
then
    #xrandr --output eDP1 --primary --mode 1536x1024 --rate 60 --output DP1 --mode 2560x1440 --rate 144 --right-of eDP1
    xrandr --output eDP1 --primary --mode 1536x1024 --pos 512x1440 --rotate normal --output DP1 --mode 2560x1440 --pos 0x0 --rotate normal
    notify-send Display=DualDisp &
fi
