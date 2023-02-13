#!/bin/bash

current_layout=$(setxkbmap -query | grep layout | awk '{print $2}')

if [ "$current_layout" == "us" ]; then
    setxkbmap -layout ua
elif [ "$current_layout" == "ua" ]; then
    setxkbmap -layout ru
elif [ "$current_layout" == "ru" ]; then
    setxkbmap -layout us
#else
#    setxkbmap -layout us
fi

pkill -RTMIN+1 i3blocks

