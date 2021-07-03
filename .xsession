# Image compositor
picom --no-fading-openclose &

# Keyboard Layout
setxkbmap gb &

# Wallpaper
feh --bg-scale ./Downloads/4kwallpaper.jpg &

# USB player
udiskie -t &

# Screen Display 
xrandr --output HDMI-1 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --output DVI-I-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off &

# Wifi icon
nm-applet &