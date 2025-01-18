import flet as ft
import os
from uibase import UIBase
from pages import about, setting, home, login
from const import *


def get_pages():
    data_dir = os.getenv("FLET_APP_STORAGE_DATA")
    user_exists = data_dir and os.path.exists(os.path.join(data_dir, "user.json"))

    pages = [
        home.page,
        setting.page,
        about.page,
    ]

    if not user_exists:
        pages[0] = login.page

    return pages


def main(page: ft.Page):
    global ui
    pages = get_pages()
    ui = UIBase(pages, theme_colors)
    
    ui.get_ui()(page)


ft.app(main)
