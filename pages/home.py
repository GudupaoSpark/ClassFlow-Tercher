import flet as ft
import os
import json
from const import *
from . import login

def get_user_info():
    if data_dir and os.path.exists(os.path.join(data_dir, "user.json")):
        with open(os.path.join(data_dir, "user.json"), "r") as f:
            user_data = json.load(f)
            return {
                "username": user_data.get("username"),
                "base_url": user_data.get("base_url")
            }
    return {"username": None, "base_url": None}

def get_home_content(ui):
    global ui_ref
    ui_ref = ui
    user_info = get_user_info()
    
    def logout(e):
        if data_dir and os.path.exists(os.path.join(data_dir, "user.json")):
            os.remove(os.path.join(data_dir, "user.json"))
            np = ui.pages
            np[0] = login.page
            ui.update_pages(np)

    header = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Text("仪表盘", size=24, weight=ft.FontWeight.BOLD),
                padding=ft.padding.only(bottom=20)
            ),
            ft.Row([
                ft.Container(
                    content=ft.Stack(
                        controls=[
                            ft.Text("用户信息", size=14, top=0, left=10),
                            ft.Container(
                            content=ft.Row([
                                ft.Column([
                                    ft.Text(f"{user_info['base_url'] if user_info['base_url'] else '未设置'}",
                                           size=20, weight=ft.FontWeight.BOLD),
                                    ft.Text("BASE_URL", size=14)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                ft.VerticalDivider(width=1, color=theme_colors["border"]),
                                ft.Column([
                                    ft.Text(f"{user_info['username'] if user_info['username'] else '访客'}",
                                           size=20, weight=ft.FontWeight.BOLD),
                                    ft.Text("当前用户", size=14)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                            ],
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER),
                            alignment=ft.alignment.center,
                            height=120,
                            padding=ft.padding.only(top=10)
                        )
                    ]),
                    padding=20,
                    bgcolor=theme_colors["surface"],
                    border_radius=10,
                    expand=True,
                    height=120
                ),
                ft.Container(
                    content=ft.Button(
                        content=ft.Column([
                            ft.Icon(ft.Icons.LOGOUT, size=20),
                            ft.Text("登出", size=12)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=3),
                        on_click=logout,
                        height=60,
                        width=80,
                        style=ft.ButtonStyle(
                            padding=ft.padding.symmetric(horizontal=10, vertical=5),
                            color=ft.Colors.RED_900
                        )
                    ),
                    padding=10,
                    bgcolor=theme_colors["surface"],
                    border_radius=10,
                    height=120
                )
            ], spacing=10)
        ])
    )
    
    stats_row = ft.Row([
        ft.Container(
            content=ft.Stack([
                ft.Text("班级数量", size=14, top=10, left=10),
                ft.Container(
                    content=ft.Column([
                        ft.Text("8", size=28, weight=ft.FontWeight.BOLD),
                        ft.Container(height=16)  # 占位符保持高度一致
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    alignment=ft.alignment.center,
                    height=120,
                    padding=ft.padding.only(top=20)
                )
            ]),
            padding=20,
            bgcolor=theme_colors["surface"],
            border_radius=10,
            expand=True,
            height=120
        ),
        ft.Container(
            content=ft.Stack([
                ft.Text("最近更新", size=14, top=10, left=10),
                ft.Container(
                    content=ft.Column([
                        ft.Text("2025-01-17", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("23:45", size=16)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    alignment=ft.alignment.center,
                    height=120,
                    padding=ft.padding.only(top=20)
                )
            ]),
            padding=20,
            bgcolor=theme_colors["surface"],
            border_radius=10,
            expand=True,
            height=120
        )
    ], spacing=10)
    
    recent_activity = ft.Container(
        content=ft.Column([
            ft.Text("最近活动", size=18, weight=ft.FontWeight.BOLD),
            ft.ListView([
                ft.ListTile(
                    title=ft.Text("完成作业1"),
                    subtitle=ft.Text("2小时前"),
                    leading=ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINE)
                ),
                ft.ListTile(
                    title=ft.Text("收到新消息"),
                    subtitle=ft.Text("4小时前"),
                    leading=ft.Icon(ft.Icons.MESSAGE_OUTLINED)
                )
            ], spacing=5)
        ]),
        padding=20,
        bgcolor=theme_colors["surface"],
        border_radius=10
    )
    
    return ft.Column(
        controls=[header, stats_row, recent_activity],
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

page = {
        "icon": ft.Icons.HOME_ROUNDED,
        "selected_icon": ft.Icons.HOME_OUTLINED,
        "label": "主页",
        "func": get_home_content,
    }
