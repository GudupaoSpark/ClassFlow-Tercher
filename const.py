import os
import darkdetect

theme_colors_dark = {
    "primary": "#60CDFF",
    "secondary": "#2B2B2B",
    "surface": "#202020",
    "background": "#1F1F1F",
    "text": "#FFFFFF",
    "text_secondary": "#9D9D9D",
    "border": "#404040",
    "hover": "#2D2D2D",
    "selected": "#3B3B3B",
    "bgcolor": "#101010",
}

theme_colors_light = {
    "primary": "#42A5F5",
    "secondary": "#F5F5F5",
    "surface": "#FFFFFF",
    "background": "#ECEFF1",
    "text": "#000000",
    "text_secondary": "#757575",
    "border": "#BDBDBD",
    "hover": "#E0E0E0",
    "selected": "#BBDEFB",
    "bgcolor": "#FAFAFA",
}

if os.name == "nt":
    data_dir = os.getenv("appdata")+"/ClassFlow/Tercher"
else:
    data_dir = os.getenv("HOME")+"/.ClassFlow/Tercher"

assets_dir = os.path.abspath(".")+"/assets"

theme_colors = theme_colors_light if darkdetect.theme() == "Light" else theme_colors_dark

if not os.path.exists(data_dir):
    os.makedirs(data_dir)
