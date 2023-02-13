# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

mod = "mod4"
terminal = "kitty"
file_manager = "nnn"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "control"], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

##CUSTOM
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
##Other stuff
#Key([mod], "c", lazy.spawn("roficlip"), desc='clipboard'),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
]



groups = [Group(f"{i+1}",label="\uf069") for i in range(7)]
#groups = [Group(i) for i in "123456789"]
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

#mainColor = '#2e3440'
mainColor = '#2e3440'
secondaryColor = '#3b4252'

#mainColor = '#468'
#secondaryColor = '#334d66'

borderNormal = mainColor
borderFocused = secondaryColor

#default = 4
borderWidth = 0

#add layoutDefault = dict()

layouts = [
    layout.Columns(border_width=borderWidth, margin=6, border_normal=borderNormal, border_focus=borderFocused, border_normal_stack=borderNormal, border_focus_stack=borderFocused),
    layout.Max(border_width=borderWidth, margin=6, border_normal=borderNormal,border_focus=borderFocused),
    #layout.Matrix(border_width=borderWidth, margin=6, border_normal=borderNormal,border_focus=borderFocused),
    #layout.MonadTall(border_width=borderWidth, margin=6, border_normal=borderNormal,border_focus=borderFocused),
    #layout.MonadWide(border_width=borderWidth, margin=6, border_normal=borderNormal,border_focus=borderFocused),
    #layout.Tile(border_width=borderWidth, margin=6, border_normal=borderNormal,border_focus=borderFocused),
    # Try more layouts by unleashing below layouts.
    # layout.Floating(border_width=borderWidth, border_normal=borderNormal,border_focus=borderFocused),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    #font="sans",
    font="JetBrains Mono Bold",
    fontsize=14,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [  
                widget.Spacer(
                    length=14,
                ),
                #widget.TextBox(
                #    text="\ue62e",
                #    #foreground="#ffaf00",
                #    foreground="#bffff9",
                #    fontsize=24,
                #),
                #widget.CurrentLayoutIcon(
                #    scale = 0.45,
                #),
                #widget.CurrentLayout(
                #    font= 'JetBrains Mono'
                #),
                widget.GroupBox(
                    highlight_method="text",
                    this_current_screen_border="#ffaf00",
                    active="#2c9",
                    inactive=secondaryColor,
                #2c9ac4
                    padding=2,
                    fontsize=15,
                    borderwidth=0,
                    disable_drag=True,
                ),
                widget.WindowName(
                    foreground="#cad3f5",
                    font="JetBrains Mono Bold",
                ),
                #widget.Spacer(
                #    length=735,
                #),
                widget.Systray(),
                #widget.Spacer(
                #    length=8,
                #),
                #widget.CurrentLayoutIcon(
                #    scale=0.45,
                #    padding=0,
                #),
                # widget.Memory(),
                widget.TextBox(
                    foreground=secondaryColor,
                    text="|",
                    fontsize=18,
                    padding=3,
                ),
                widget.TextBox(
                    foreground="#a6da95",
                    text="",
                    font="JetBrains Mono",
                    fontsize=18,
                    padding=0,
                ),
                widget.Spacer(
                    length=2,
                ),
                widget.KeyboardLayout(
                    configured_keyboards=['us', 'ua', 'ru'],
                    foreground="#a6da95",
                    font="JetBrains Mono ExtraBold",
                    padding=0,
                ),
                widget.Spacer(
                    length=4,
                ),
                widget.TextBox(
                    foreground=secondaryColor,
                    text="|",
                    fontsize=18,
                    padding=0,
                ),
                widget.TextBox(
                    foreground="#91d7e3",
                    text=" ",
                    font="JetBrains Mono",
                    fontsize=18,
                    padding=0,
                    ),
                widget.Battery(
                    foreground="#91d7e3",
                    format="{percent:2.0%}{char}",
                    charge_char='^',
                    discharge_char='',
                    font="JetBrains Mono ExtraBold",
                    fontsize=14,
                    padding=0,
                    update_interval=5,
                ),
                widget.Spacer(
                    length=5,
                ),
                #widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(), 
                widget.TextBox(
                    foreground="#b7bdf8",
                    text="",
                    font="Font Awesome 6 Free Solid",
                    fontsize=15,
                    padding=3,
                    mouse_callbacks={
                        "Button1": lazy.spawn("pulsemixer --toggle-mute"),
                    },
                ),
                widget.PulseVolume(
                    foreground="#b7bdf8",
                    font='JetBrains Mono ExtraBold',
                    fontsize=14,
                    padding=0,
                ),
                #widget.TextBox(
                #    foreground=secondaryColor,
                #    text="|",
                #    fontsize=18,
                #    padding=3,
                #),
                widget.Spacer(
                    length=10,
                ),
                #widget.Pomodoro(
                    #color_active="",
                    #color_break="#ff6361",
                    #color_inactive="#ffffff",
                    #color_inactive="#ed8796",
                    #prefix_inactive="pomodoro",
                    #prefix_paused="pause",
                    #prefix_break="b",
                #),
                #widget.Spacer(
                #   length=4,
                #),
                widget.TextBox(
                    foreground=secondaryColor,
                    text="|",
                    fontsize=18,
                    padding=0,
                ),
                widget.TextBox(
                   foreground="#f5bde6",
		           text=" ",
                   padding=3,
                   #background="#334d66",
		        ),
                widget.Clock(
                    foreground="#f5bde6",
                    #%I:%M %p
                    format="%H:%M",
                    font="JetBrains Mono Bold",
                    #background='#334d66',
                    rounded=True,
                    padding=0,
                ),
                widget.Spacer(
                    length=4,
                    #background="#334d66",
                ),
                widget.TextBox(
                    foreground=secondaryColor,
                    text="|",
                    fontsize=18,
                    padding=0,
                ),
                widget.Spacer(
                    length=4,
                    #background="#334d66",
                ),
                widget.TextBox(
                   foreground="#f0c6c6",
		           text=" ",
                   fontsize=14,
                   padding=3,
                   #background="#334d66",
		        ),
                widget.Clock(
                    foreground="#f0c6c6",
                    format="%d/%m/%y",
                    font="JetBrains Mono Bold",
                    padding=0,
                ),
                # widget.QuickExit(),
                widget.TextBox(
                    foreground=secondaryColor,
                    text="|",
                    fontsize=18,
                ),
                widget.Spacer(
                    length=6,
                ),
                widget.TextBox(
                    text="\uf011",
                    #foreground="#ff6361",
                    foreground="#f5a97f",
                    fontsize=15,
                    mouse_callbacks={
                        "Button1": lazy.shutdown(),
                    },
                ),
                # widget.QuickExit(
                #     default_text="\uf011",
                #     #foreground="#ff6361",
                #     foreground="#f5a97f",
                #     fontsize=15,
                #     # countdown_format='{}',
                # ),
                widget.Spacer(
                    length=18,
                ),
            ],
            30,
            background = mainColor,
            margin = [6,6,6,6],
            #border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod, "control"], "Button1", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# mouse = [
#     Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
#     Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
#     Click([mod], "Button2", lazy.window.bring_to_front()),
# ]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    
    # border_focus = '#FF632F',
    # border_normal = '#FF632F',
    border_width = 0
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
# wmname = "astrowm"
