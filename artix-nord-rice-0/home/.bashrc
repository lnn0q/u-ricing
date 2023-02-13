#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias cb='cbonsai -l -t 3 -m "read-sleep ^repeat"'
export PATH="$PATH:$HOME/.local/bin"
# alias ls='ls --color=auto'
# PS1='[\u@\h \W]\$ '
export PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/home/lnn0q/.local/bin

export PATH="~/Scripts/:$PATH"

eval "$(starship init bash)"
