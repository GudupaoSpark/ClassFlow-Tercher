import flet as ft
import os
import sys



def DEFUI(pages, theme_colors = {
            "primary": "#60CDFF",
            "secondary": "#2B2B2B",
            "surface": "#202020",
            "background": "#1F1F1F",
            "text": "#FFFFFF",
            "text_secondary": "#9D9D9D",
            "border": "#404040",
            "hover": "#2D2D2D",
            "selected": "#3B3B3B",
        }):
    def f(page: ft.Page):
        nonlocal pages,theme_colors
        

        # 窗口设置
        page.title = "ClassFlow"
        page.window.title_bar_hidden = True
        page.window.title_bar_buttons_hidden = True
        page.window.bgcolor = ft.Colors.BLUE_GREY_900
        page.padding = 0

        # 窗口控制函数
        def window_close(e):
            page.window.close()
            
        def window_minimize(e):
            page.window.minimized = True
            page.update()
            
        def window_maximize(e):
            # 如果当前是全屏状态，先退出全屏
            if page.window.full_screen:
                page.window.full_screen = False
            
            # 切换最大化状态
            page.window.maximized = not page.window.maximized
            page.update()

        def window_fullscreen(e):
            # 切换全屏状态
            is_fullscreen = not page.window.full_screen
            page.window.full_screen = is_fullscreen
            
            # 更新按钮状态
            e.control.selected = is_fullscreen
            page.update()

        # 页面切换处理
        def change_page_content(e):
            index = int(e.control.selected_index)
            content_area.content = pages[index]["func"]()
            content_area.update()
        



        # 创建标题栏
        title_bar = ft.Container(
            content=ft.Row(
                controls=[
                    ft.WindowDragArea(
                        content=ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image(
                                        "src\\assets\\icon.png"
                                    ),
                                    ft.Text(
                                        page.title,
                                        size=13,
                                        color=theme_colors["text"],
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ],
                                spacing=8,
                            ),
                            padding=ft.padding.only(left=12, top=8, bottom=8),
                        ),
                        expand=True,
                    ),
                    ft.Row(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.PUSH_PIN_OUTLINED,
                                        selected_icon=ft.Icons.PUSH_PIN_ROUNDED,
                                        icon_size=16,
                                        icon_color=theme_colors["text"],
                                        selected=False,
                                        on_click=lambda e: (
                                            setattr(page.window, 'always_on_top', not page.window.always_on_top),
                                            setattr(e.control, 'selected', page.window.always_on_top),
                                            page.update()
                                        ),
                                        style=ft.ButtonStyle(
                                            padding=12,
                                            shape=ft.RoundedRectangleBorder(radius=0),
                                            bgcolor={
                                                "": theme_colors["surface"],
                                                "hovered": theme_colors["hover"],
                                            },
                                        ),
                                        tooltip="置顶窗口",
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.FULLSCREEN_ROUNDED,
                                        selected_icon=ft.Icons.FULLSCREEN_EXIT_ROUNDED,
                                        icon_size=16,
                                        icon_color=theme_colors["text"],
                                        selected=False,
                                        on_click=window_fullscreen,
                                        style=ft.ButtonStyle(
                                            padding=12,
                                            shape=ft.RoundedRectangleBorder(radius=0),
                                            bgcolor={
                                                "": theme_colors["surface"],
                                                "hovered": theme_colors["hover"],
                                            },
                                        ),
                                        tooltip="全屏",
                                    ),
                                ],
                                spacing=0
                            ),
                            ft.IconButton(
                                icon=ft.Icons.REMOVE_ROUNDED,
                                icon_size=16,
                                icon_color=theme_colors["text"],
                                on_click=window_minimize,
                                style=ft.ButtonStyle(
                                    padding=12,
                                    shape=ft.RoundedRectangleBorder(radius=0),
                                    bgcolor={
                                        "": theme_colors["surface"],
                                        "hovered": theme_colors["hover"],
                                    },
                                ),
                                tooltip="最小化",
                            ),
                            ft.IconButton(
                                icon=ft.Icons.CROP_SQUARE_ROUNDED,
                                icon_size=16,
                                icon_color=theme_colors["text"],
                                on_click=window_maximize,
                                style=ft.ButtonStyle(
                                    padding=12,
                                    shape=ft.RoundedRectangleBorder(radius=0),
                                    bgcolor={
                                        "": theme_colors["surface"],
                                        "hovered": theme_colors["hover"],
                                    },
                                ),
                                tooltip="最大化",
                            ),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE_ROUNDED,
                                icon_size=16,
                                icon_color=theme_colors["text"],
                                on_click=window_close,
                                style=ft.ButtonStyle(
                                    padding=12,
                                    shape=ft.RoundedRectangleBorder(radius=0),
                                    bgcolor={
                                        "": theme_colors["surface"],
                                        "hovered": "#C42B1C",
                                    },
                                ),
                                tooltip="关闭",
                            ),
                        ],
                        spacing=5,
                    ),
                ],
                spacing=0,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=theme_colors["surface"],
            height=40,
            border=ft.border.only(
                bottom=ft.BorderSide(1, theme_colors["border"])
            ),
        )

        # 内容区域
        content_area = ft.Container(
            content=ft.Text("主页内容", color=theme_colors["text"]),
            expand=True,
            padding=20
        )

        # 创建导航栏
        navigation_rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=200,
            extended=True,
            bgcolor=theme_colors["surface"],
            indicator_color=theme_colors["primary"],
            destinations=[
                ft.NavigationRailDestination(
                    icon=page["icon"],
                    selected_icon=page["selected_icon"],
                    label=page["label"]
                ) for page in pages
            ],
            on_change=change_page_content
        )
        
        # 创建主内容区域
        main_content = ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        title_bar,
                        ft.Row(
                            controls=[
                                navigation_rail,
                                ft.VerticalDivider(width=1),
                                content_area
                            ],
                            spacing=0,
                            expand=True
                        )
                    ],
                    spacing=0,
                    expand=True
                )
            ],
            spacing=0,
            expand=True
        )

        # 设置默认页面
        content_area.content = pages[0]["func"]()
        
        # 添加内容到页面
        page.add(main_content)
    return f
