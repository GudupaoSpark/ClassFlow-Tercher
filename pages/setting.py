import flet as ft
from const import *
import os
import json


def test(e):
    return ft.Column(
        controls=[
            ft.Text("测试"),
            ft.Text(os.getcwd(), color=theme_colors["text"], size=30),
            ft.Text(os.path.abspath(f"{assets_dir}/icon.png"), color=theme_colors["text"], size=30),
        ]
    )


def get_settings_content(ui):
    switch = ft.Switch(
        label="显示测试页面", value="测试" in [page["label"] for page in ui.pages]
    )

    # 读取保存的base_url
    config_path = os.path.join(data_dir, "config.json")
    config = {}
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = json.load(f)

    base_url = ft.TextField(
        label="BASE_URL",
        width=600,
        hint_text="请包括协议头",
        value=config.get("base_url", "")
    )

    def toggle_test_page(e):
        new_pages = [page for page in ui.pages if page["label"] != "测试"]
        if switch.value:
            new_pages.append(
                {
                    "icon": ft.Icons.BUG_REPORT_ROUNDED,
                    "selected_icon": ft.Icons.BUG_REPORT_OUTLINED,
                    "label": "测试",
                    "func": test,
                }
            )

        ui.update_pages(new_pages)

    def save_base_url(e):
        config["base_url"] = base_url.value
        with open(config_path, "w") as f:
            json.dump(config, f)

    switch.on_change = toggle_test_page
    base_url.on_change = save_base_url

    return ft.Column(
        controls=[
            ft.Text("设置", color=theme_colors["text"], size=20),
            switch,
            base_url
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )


page = {
    "icon": ft.Icons.SETTINGS_ROUNDED,
    "selected_icon": ft.Icons.SETTINGS_OUTLINED,
    "label": "设置",
    "func": get_settings_content,
}
