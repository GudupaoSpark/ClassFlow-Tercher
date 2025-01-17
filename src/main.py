import flet as ft
from uibase import DEFUI
import webbrowser

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


def get_about_content():
    co = ft.Column(
        controls=[
            ft.Text("ClassFlow", size=50),
            ft.Text("更好的同步课表", size=20),
            ft.Text("", size=10),
            ft.Row(
                [
                    ft.Button(
                        "Website",
                        on_click=lambda _: webbrowser.open(
                            "https://gudupao.top"
                        ),
                    ),ft.Button(
                        "Github Repo",
                        on_click=lambda _: webbrowser.open(
                            "https://github.com/GudupaoSpark/ClassFlow"
                        ),
                    )
                ],
        alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],spacing=15,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return ft.SafeArea(
        ft.Container(
            co,
            alignment=ft.alignment.center,
        ),
        expand=True,
    )


def get_settings_content():
    return ft.Text("设置页面", color=theme_colors["text"])


def get_home_content():
    return ft.Text("主页", color=theme_colors["text"])


ps = [
    {
        "icon": ft.Icons.HOME_ROUNDED,
        "selected_icon": ft.Icons.HOME_OUTLINED,
        "label": "主页",
        "func": get_home_content,
    },
    {
        "icon": ft.Icons.SETTINGS_ROUNDED,
        "selected_icon": ft.Icons.SETTINGS_OUTLINED,
        "label": "设置",
        "func": get_settings_content,
    },
    {
        "icon": ft.Icons.INFO_ROUNDED,
        "selected_icon": ft.Icons.INFO_OUTLINED,
        "label": "关于",
        "func": get_about_content,
    },
]

ft.app(DEFUI(ps, theme_colors))
