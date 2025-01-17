import flet as ft
import os
import json
from . import home

def get_login_content(ui):

    def on_login_click(e):
        print(f"Username: {username.value}, Password: {password.value}")
        
        # 保存用户信息
        data_dir = os.getenv("FLET_APP_STORAGE_DATA")
        if data_dir:
            user_data = {
                "username": username.value,
                "password": password.value
            }
            with open(os.path.join(data_dir, "user.json"), "w") as f:
                json.dump(user_data, f)
        
        np = ui.pages
        np[0] = home.page
        ui.update_pages(np)

    username = ft.TextField(label="用户名", width=300)
    password = ft.TextField(label="密码", password=True, width=300)
    
    co = ft.Column(
        controls=[
            ft.Text("登录 ClassFlow", size=30),
            username,
            password,
            ft.Row(
                [
                    ft.Button(
                        "登录",
                        on_click=on_login_click
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        spacing=15,
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

page = {
            "icon": ft.Icons.LOGIN_ROUNDED,
            "selected_icon": ft.Icons.LOGIN_OUTLINED,
            "label": "登录",
            "func": get_login_content,
        }