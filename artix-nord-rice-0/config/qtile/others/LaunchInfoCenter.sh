#!/bin/bash

# Author 	 -  z0mbi3
# Source 	 -  https://github.com/gh0stzk/dotfiles
# Maintainer -  z0mbi3.zk@protonmail.com
#
FILE="/home/lnn0q/.cache/eww_m.dashboard"
ewwcfg="/home/lnn0q/.config/eww/"
EWW=`which eww`

if [[ ! `pidof eww` ]]; then
	${EWW} -c /home/lnn0q/.config/eww/ daemon &
	sleep 1
fi

launch_eww() {
	${EWW} --config "$ewwcfg" open dashboard
}


## Launch or close widgets accordingly
if [[ ! -f "$FILE" ]]; then
	touch "$FILE"
	launch_eww
else
	${EWW} --config "$ewwcfg" close dashboard
	rm "$FILE"
fi
