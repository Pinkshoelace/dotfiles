# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from os import path
import subprocess

# Autostart

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')])




mod = "mod4"
terminal = guess_terminal()

keys = [

    # TILES

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Spawn Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Volume Keys
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    #Spawn Programs
    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    Key([mod], "b", lazy.spawn("firefox")),

    # Screenshot saved in .
    Key([mod], "s", lazy.spawn("scrot")),

    # Open file explorer
    Key([mod], "n", lazy.spawn("thunar")),
]

groups = [Group(i) for i in ["  WWW  ","  DEV  ","  TERM  ","  MISC  "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


# Color & space between layout
layout_conf= {
    'border_focus': '#a151d3',
    'border_width': 1,
    'margin': 4

}


layouts = [
    # layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(**layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_conf),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    #HDMI
    Screen(
        top=bar.Bar(
            [   
                widget.TextBox(
                    background=["#0f101a", "#0f101a"],
                    foreground=["#6a359c", "#6a359c"], 
                    text=' ',
                    fontsize='20'
                ),
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font',
                    fontsize=16,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    # urgent_alert_method='block',
                    # urgent_border=["#F07178", "#F07178"],
                    this_current_screen_border=["#a151d3", "#a151d3"],
                    this_screen_border=["#353c4a", "#353c4a"],
                    other_current_screen_border=["#0f101a", "#0f101a"],
                    other_screen_border=["#0f101a", "#0f101a"],
                    disable_drag=True
                ),
                widget.WindowName(
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0f101a", "#0f101a"],
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold'
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'purple', 'last.png'),
                ),
                widget.Sep(
                    background=["#b589d6", "#b589d6"],
                    linewidth=0,
                    padding=5
                ),
                widget.Sep(
                    background=["#b589d6", "#b589d6"],
                    linewidth=0,
                    padding=5
                ),
                widget.Systray(
                    background=["#b589d6", "#b589d6"]
                ),
                widget.Sep(
                    background=["#b589d6", "#b589d6"],
                    linewidth=0,
                    padding=5
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'purple', 'middle.png'),
                ),
                widget.CurrentLayoutIcon(
                    background=["#804fb3", "#804fb3"],
                    foreground=["#0f101a", "#0f101a"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    background=["#804fb3", "#804fb3"],
                    foreground=["#f1ffff", "#f1ffff"],
                ),
                widget.Sep(
                    background=["#804fb3", "#804fb3" ],
                    linewidth=0,
                    padding=5
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'purple', 'first.png'),
                ),
                widget.TextBox(
                    background=["#6a359c", "#6a359c"],
                    foreground=["#f1ffff", "#f1ffff"], 
                    text=' ' 
                ),
                widget.Clock(
                    background=["#6a359c", "#6a359c"],
                    foreground=["#f1ffff", "#f1ffff"], 
                    format='%d/%m/%Y - %H:%M '
                ),
            ],
            24,
            opacity=0.95
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font',
                    fontsize=16,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    # urgent_alert_method='block',
                    # urgent_border=["#F07178", "#F07178"],
                    this_current_screen_border=["#a151d3", "#a151d3"],
                    this_screen_border=["#353c4a", "#353c4a"],
                    other_current_screen_border=["#0f101a", "#0f101a"],
                    other_screen_border=["#0f101a", "#0f101a"],
                    disable_drag=True
                ),
                widget.WindowName(
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0f101a", "#0f101a"],
                    fontsize=14,
                    font='UbuntuMono Nerd Font Bold'
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'purple', 'last.png'),
                ),
                widget.CurrentLayoutIcon(
                    background=["#b589d6", "#b589d6"],
                    foreground=["#0f101a", "#0f101a"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    background=["#b589d6", "#b589d6"],
                    foreground=["#f1ffff", "#f1ffff"],
                ),
                widget.Sep(
                    background=["#b589d6", "#b589d6" ],
                    linewidth=0,
                    padding=5
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'purple', 'middle.png'),
                ),
                widget.TextBox(
                    background=["#804fb3", "#804fb3"],
                    foreground=["#f1ffff", "#f1ffff"], 
                    text=' ' 
                ),
                widget.Clock(
                    background=["#804fb3", "#804fb3"],
                    foreground=["#f1ffff", "#f1ffff"], 
                    format='%d/%m/%Y - %H:%M '
                ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], border_focus='#a151d3')
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# Fix Java
wmname = "LG3D"
