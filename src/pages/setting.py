import flet as ft
from const import *

def get_settings_content(ui):
    switch = ft.Switch(
        label="显示测试页面",
        value="测试" in [page["label"] for page in ui.pages]
    )

    def toggle_test_page(e):
        new_pages = [page for page in ui.pages if page["label"] != "测试"]
        if switch.value:
            new_pages.append({
                "icon": ft.Icons.BUG_REPORT_ROUNDED,
                "selected_icon": ft.Icons.BUG_REPORT_OUTLINED,
                "label": "测试",
                "func": lambda x: ft.Text("测试页面", color=theme_colors["text"], size=30),
            })
        
        ui.update_pages(new_pages)

    switch.on_change = toggle_test_page

    return ft.Column(
        controls=[
            ft.Text("设置", color=theme_colors["text"], size=20),
            switch
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START
    )

page = {
        "icon": ft.Icons.SETTINGS_ROUNDED,
        "selected_icon": ft.Icons.SETTINGS_OUTLINED,
        "label": "设置",
        "func": get_settings_content,
    }