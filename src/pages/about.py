import flet as ft
import webbrowser

def get_about_content(ui):
    co = ft.Column(
        controls=[
            ft.Image(
                src="src/assets/icon.png",
                width=256,
                height=256,
            ),
            ft.Text("ClassFlow", size=50),
            ft.Text("更好的同步课表", size=20),
            ft.Text("By Gudupao", size=15),
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

page = {
        "icon": ft.Icons.INFO_ROUNDED,
        "selected_icon": ft.Icons.INFO_OUTLINED,
        "label": "关于",
        "func": get_about_content,
    }