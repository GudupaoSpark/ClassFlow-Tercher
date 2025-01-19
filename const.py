import os

theme_colors = {
    "primary": "#60CDFF",
    "secondary": "#2B2B2B",
    "surface": "#202020",
    "background": "#1F1F1F",
    "text": "#FFFFFF",
    "text_secondary": "#9D9D9D",
    "border": "#404040",
    "hover": "#2D2D2D",
    "selected": "#3B3B3B",
}

if os.name == "nt":
    data_dir = os.getenv("appdata")+"/ClassFlow/Tercher"
else:
    data_dir = os.getenv("HOME")+"/.ClassFlow/Tercher"

if not os.path.exists(data_dir):
    os.makedirs(data_dir)