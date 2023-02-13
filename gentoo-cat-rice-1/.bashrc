# /etc/skel/.bashrc
#
# This file is sourced by all *interactive* bash shells on startup,
# including some apparently interactive shells such as scp and rcp
# that can't tolerate any output.  So make sure this doesn't display
# anything or bad things will happen !


# Test for an interactive shell.  There is no need to set anything
# past this point for scp and rcp, and it's important to refrain from
# outputting anything in those cases.
if [[ $- != *i* ]] ; then
	# Shell is non-interactive.  Be done now!
	return
fi


# Put your fun stuff here.

if [ "$(tty)" == "/dev/tty1" ]; then
	exec ~/.autowm_s.sh
fi

#eval "$(starship init bash)"

. /home/lnn0q/.nix-profile/etc/profile.d/nix.sh

alias nf='printf "\n\n\n\n\n" && nitch && printf "\n\n\n"'

export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/Scripts:$PATH"
