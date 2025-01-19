import flet as ft
import os
import json
from . import home
from const import *

def get_login_content(ui):

    def on_login_click(e):
        # 验证输入
        has_error = False
        if not base_url.value:
            base_url.error_text = "请输入 BASE_URL"
            has_error = True
        else:
            base_url.error_text = None
            
        if not username.value:
            username.error_text = "请输入用户名"
            has_error = True
        else:
            username.error_text = None
            
        if not password.value:
            password.error_text = "请输入密码"
            has_error = True
        else:
            password.error_text = None
            
        if has_error:
            ui.the_page.update()
            return
            
        print(f"Username: {username.value}, Password: {password.value}")
        
        # 保存用户信息
        if data_dir:
            user_data = {
                "base_url": base_url.value,
                "username": username.value,
                "password": password.value
            }
            with open(os.path.join(data_dir, "user.json"), "w") as f:
                json.dump(user_data, f)
        
        np = ui.pages
        np[0] = home.page
        ui.update_pages(np)

    base_url = ft.TextField(
        label="BASE_URL",
        width=600,
        hint_text="请包括协议头"
    )
    username = ft.TextField(label="用户名", width=600)
    password = ft.TextField(label="密码", password=True, width=600)
    
    co = ft.Column(
        controls=[
            ft.Image(
                src=f"{assets_dir}/icon.png",
                width=150,
                height=150,
            ),
            ft.Text("ClassFlow", size=50),
            ft.Text("登录教师账号", size=30),
            base_url,
            username,
            password,
            ft.Row(
                [
                    ft.Button(
                        "登录",
                        icon=ft.Icons.LOGIN,
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
            ft.Column(
                [
                    ft.Container(
                        co,
                        alignment=ft.alignment.center,
                    )
                ],
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
            alignment=ft.alignment.center,
            expand=True,
        ),
        expand=True,
    )

page = {
            "icon": ft.Icons.LOGIN_ROUNDED,
            "selected_icon": ft.Icons.LOGIN_OUTLINED,
            "label": "登录",
            "func": get_login_content,
        }