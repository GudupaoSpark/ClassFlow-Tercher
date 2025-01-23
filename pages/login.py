import flet as ft
import os
import json
from . import home
from const import *
from encrypt import en_req

def get_login_content(ui):

    def on_login_click(e):
        # 读取配置
        config_path = os.path.join(data_dir, "config.json")
        if not os.path.exists(config_path):
            ui.base_url_error = "请先在设置中配置 BASE_URL"
            ui.the_page.update()
            return
            
        with open(config_path, "r") as f:
            config = json.load(f)
            
        # 验证输入
        has_error = False
        if not config.get("base_url"):
            ui.base_url_error = "请先在设置中配置 BASE_URL"
            has_error = True
        else:
            ui.base_url_error = None
            
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
            
        # 使用info模块发送登录请求
        from reqs import info
        if not info.send_login_request(username.value, password.value, ui):
            password.error_text = "登录失败，请检查用户名和密码"
            ui.the_page.update()
            return
        
        np = ui.pages
        np[0] = home.page
        ui.update_pages(np)

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