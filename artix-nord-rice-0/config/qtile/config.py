from libqtile import bar, layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from libqtile import widget as owidget
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration

import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

mod = "mod4"
terminal = "kitty"
file_manager = "thunar"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "control"], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
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
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc='brightness Down'),
    Key([mod], "XF86MonBrightnessUp", lazy.spawn("redshift -O 4500K"), desc='Heat UP'),
    Key([mod], "XF86MonBrightnessDown", lazy.spawn("redshift -x"), desc='Heat Down'),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
    Key([mod], "e", lazy.spawn("/home/lnn0q/.config/qtile/current_display.sh 1"), desc="ExtDisplay"),
    Key([mod], "i", lazy.spawn("/home/lnn0q/.config/qtile/current_display.sh 2"), desc="BuiltInDisplay"),
    Key([mod], "l", lazy.spawn("/home/lnn0q/.config/qtile/current_display.sh 3"), desc="DualDisplay"),
    Key([mod], "d", lazy.spawn("/home/lnn0q/.config/qtile/control_widgets.sh"), desc="WidgetControl"),
]



groups = [Group(f"{i+1}",label="") for i in range(7)]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

groups.append(ScratchPad('scratchpad', [
    DropDown('foliate', 'foliate', width=0.48, height=0.81,x=0.33, y=0.08, on_focus_lost_hide=False, warp_pointer=False),
    DropDown('cava', [terminal, 'cava'], width=0.217, height=0.143, x=0.059, y=0.596, on_focus_lost_hide=False, warp_pointer=False),
    DropDown('spotify', 'spotify', width=0.65, height=0.65, x=0.3, y=0.16, on_focus_lost_hide=False, warp_pointer=False),
    DropDown('mocp', [terminal, 'mocp'], width=0.5, height=0.3, x=0.3, y=0.198 , on_focus_lost_hide=False, warp_pointer=False),
    DropDown('thunar', 'thunar', width=0.65, height=0.65, x=0.3, y=0.16, on_focus_lost_hide=False, warp_pointer=False),
    DropDown('telegram', 'telegram-desktop', width=0.65, height=0.65, x=0.3, y=0.16, on_focus_lost_hide=False, warp_pointer=False),
    DropDown('kitty', 'kitty', width=0.3, height=0.3, x=0.3, y=0.198 , on_focus_lost_hide=False, warp_pointer=False),
    DropDown('blueman-manager', 'blueman-manager', width=0.3, height=0.45, x=0.29, y=0.25, on_focus_lost_hide=False, warp_pointer=False),
    DropDown('pavucontrol', 'pavucontrol', width=0.32, height=0.45, x=0.672, y=0.25, on_focus_lost_hide=False, warp_pointer=False),
]))

keys.extend([
    Key([mod, 'control'], "1", lazy.group['scratchpad'].dropdown_toggle('foliate')),
    Key([mod, 'control'], "2", lazy.group['scratchpad'].dropdown_toggle('cava')),
    Key([mod, 'control'], "3", lazy.group['scratchpad'].dropdown_toggle('spotify')),
    Key([mod, 'control'], "4", lazy.group['scratchpad'].dropdown_toggle('mocp')),
    Key([mod, 'control'], "5", lazy.group['scratchpad'].dropdown_toggle('thunar')),
    Key([mod, 'control'], "6", lazy.group['scratchpad'].dropdown_toggle('telegram')),
    Key([mod, 'control'], "7", lazy.group['scratchpad'].dropdown_toggle('blueman-manager')),
    Key([mod, 'control'], "8", lazy.group['scratchpad'].dropdown_toggle('pavucontrol')),
    Key([mod], "A", lazy.group['scratchpad'].dropdown_toggle('kitty')),
])
# groups = [
#     ScratchPad('8', [
#         DropDown(
#             'foliate',
#             ['/usr/bin/foliate'],
#             height = 0.8,
#             width = 0.8,
#             x = 0.1,
#             y = 0.0,
#             on_focus_lost_hide = False,
#             warp_pointer = False,
#         ),
#     ]),
# ]


mainColor = '#2e3440'
secondaryColor = '#3b4252'

#mainColor = '#468'
#secondaryColor = '#334d66'

borderNormal = mainColor
borderFocused = secondaryColor

#default = 4
borderWidth = 0  

layouts = [
    layout.Columns(border_width=borderWidth, margin=6, border_normal=borderNormal, border_focus=borderFocused, border_normal_stack=borderNormal, border_focus_stack=borderFocused),
    layout.Max(border_width=borderWidth, margin=6, border_normal=borderNormal,border_focus=borderFocused),
]

decoration_group = {
    "decorations": [
        RectDecoration(colour=mainColor, radius=12, filled=True, padding_y=3, group=True)
    ],
    "padding": 5,
}

widget_defaults = dict(
    font="JetBrains Mono Bold",
    fontsize=14,
    # padding=5,
)
# extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [  
                # widget.Spacer(
                #     length=14,
                #     **decoration_group
                # ),
                widget.GroupBox(
                    highlight_method="text",
                    #this_current_screen_border="#ffaf00",
                    this_current_screen_border="#EBCB8B",
                    #active="#2c9",
                    active="#91d7e3",
                    inactive=secondaryColor,
                    # padding=5,
                    fontsize=15,
                    borderwidth=0,
                    disable_drag=True,
                    **decoration_group
                ),
                # widget.Spacer(
                    # length=820,
                # ),
                widget.WindowName(
                    foreground="#cad3f5",
                    font="JetBrains Mono Bold",
                ),
                owidget.Systray(),
                # widget.Spacer(
                #      length=5,
                # ),
                # widget.TextBox(
                #     foreground=secondaryColor,
                #     text="[",
                #     fontsize=18,
                # ),
                widget.Spacer(
                    length=5,
                ),
                widget.TextBox(
                    foreground="#a6da95",
                    text="",
                    font="JetBrains Mono",
                    fontsize=18,
                    **decoration_group
                ),
                # widget.Spacer(
                #     length=2,
                # ),
                widget.KeyboardLayout(
                    configured_keyboards=['us', 'ua', 'ru'],
                    foreground="#a6da95",
                    font="JetBrains Mono ExtraBold",
                    **decoration_group
                ),
                widget.Spacer(
                    length=5,
                ),
                # widget.TextBox(
                #     foreground=secondaryColor,
                #     text="]",
                #     fontsize=18,
                # ),
                # widget.TextBox(
                #     foreground=secondaryColor,
                #     text="[",
                #     fontsize=18,
                #     padding=0,
                # ),
                widget.TextBox(
                    foreground="#91d7e3",
                    text="",
                    font="JetBrains Mono",
                    fontsize=14,
                    # padding=0,
                    **decoration_group
                ),
                # widget.Spacer(
                #     length=4,
                # ),
                widget.Battery(
                    foreground="#91d7e3",
                    format="{percent:2.0%}{char}",
                    charge_char='^',
                    discharge_char='',
                    font="JetBrains Mono ExtraBold",
                    fontsize=14,
                    update_interval=5,
                    **decoration_group
                ),
                # widget.TextBox(
                #     foreground=secondaryColor,
                #     text="]",
                #     fontsize=18,
                #     padding=0,
                # ),
                widget.Spacer(
                    length=5,
                ),
                # widget.TextBox(
                #     foreground=secondaryColor,
                #     text="[",
                #     fontsize=18,
                #     padding=0,
                # ),
                widget.TextBox(
                    foreground="#b7bdf8",
                    text="",
                    font="Font Awesome 6 Free Solid",
                    fontsize=15,
                    mouse_callbacks={
                        "Button1": lazy.spawn("pulsemixer --toggle-mute"),
                    },
                    **decoration_group
                ),
                # widget.Spacer(
                #     length = 3,
                # ),
                widget.Volume(
                    foreground="#b7bdf8",
                    font='JetBrains Mono ExtraBold',
                    fontsize=14,
                    **decoration_group
                ),
                # widget.TextBox(
                #     foreground=secondaryColor,
                #     text="]",
                #     fontsize=18,
                # ),
                # widget.TextBox(
                #     foreground=secondaryColor,
                #     text="[",
                #     fontsize=18,
                # ),
                widget.Spacer(
                    length=5,
                ),
                widget.TextBox(
                   foreground="#f5bde6",
		           text=" ",
                   **decoration_group
		        ),
                widget.Clock(
                    foreground="#f5bde6",
                    format="%H:%M",
                    font="JetBrains Mono Bold",
                    rounded=True,
                    **decoration_group
                ),
                # widget.Spacer(
                #     length=4,
                # ),
                # widget.TextBox(
                #     foreground=secondaryColor,
                #     text="]",
                #     fontsize=18,
                #     padding=0,
                # ),
                # widget.TextBox(
                #     foreground=secondaryColor,
                #     text="[",
                #     fontsize=18,
                #     padding=0,
                # ),
                # widget.Spacer(
                #     length=4,
                # ),
                widget.Spacer(
                    length=5,
                ),
                widget.TextBox(
                   foreground="#f0c6c6",
		           text=" ",
                   fontsize=14,
                   **decoration_group
		        ),
                # widget.Spacer(
                #     length = 3,
                # ),
                widget.Clock(
                    foreground="#f0c6c6",
                    format="%d/%m/%y",
                    font="JetBrains Mono Bold",
                    **decoration_group
                ),
                # widget.TextBox(
                #     foreground=secondaryColor,
                #     text="]",
                #     fontsize=18,
                # ),
                widget.Spacer(
                    length=12,
                ),
                # widget.TextBox(
                #     foreground="#f5a97f",
                #     text="[",
                #     fontsize=18,
                # ),
                widget.TextBox(
                    text=" \uf011 ",
                    #foreground="#ff6361",
                    foreground="#f5a97f",
                    fontsize=15,
                    mouse_callbacks={
                        "Button1": lazy.shutdown(),
                    },
                    **decoration_group
                ),
                # widget.TextBox(
                #     foreground="#f5a97f",
                #     text="]",
                #     fontsize=18,
                # ),
                # widget.Spacer(
                #     length=18,
                # ),
            ],
            30,
            # background = mainColor,
            background = "#ff0000.0",
            margin = [6,6,0,6],  
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod, "control"], "Button1", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
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
# wmname = "astro"
