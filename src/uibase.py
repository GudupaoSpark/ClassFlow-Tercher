import flet as ft
import os
import sys
from rich import print


class UIBase:
    def __init__(self, pages, theme_colors=None):
        self.pages = pages
        self.theme_colors = theme_colors or {
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
        self.the_page = None
        self.current_index = 0
        self.main_content = None

    def setup_window(self, page: ft.Page):
        """初始化窗口设置"""
        page.title = "ClassFlow"
        page.window.title_bar_hidden = True
        page.window.title_bar_buttons_hidden = True
        page.window.bgcolor = ft.Colors.BLUE_GREY_900
        page.padding = 0

    def create_window_controls(self):
        """创建窗口控制按钮"""
        self.top = ft.IconButton(
            icon=ft.Icons.PUSH_PIN_OUTLINED,
            selected_icon=ft.Icons.PUSH_PIN_ROUNDED,
            icon_size=16,
            icon_color=self.theme_colors["text"],
            selected=False,
            on_click=self.toggle_always_on_top,
            style=self.get_button_style(),
            tooltip="置顶窗口",
        )
        self.full = ft.IconButton(
            icon=ft.Icons.FULLSCREEN_ROUNDED,
            selected_icon=ft.Icons.FULLSCREEN_EXIT_ROUNDED,
            icon_size=16,
            icon_color=self.theme_colors["text"],
            selected=False,
            on_click=self.toggle_fullscreen,
            style=self.get_button_style(),
            tooltip="全屏",
        )
        self.min = ft.IconButton(
            icon=ft.Icons.REMOVE_ROUNDED,
            icon_size=16,
            icon_color=self.theme_colors["text"],
            on_click=self.minimize_window,
            style=self.get_button_style(),
            tooltip="最小化",
        )
        self.max = ft.IconButton(
            icon=ft.Icons.CROP_SQUARE_ROUNDED,
            icon_size=16,
            icon_color=self.theme_colors["text"],
            on_click=self.toggle_maximize,
            style=self.get_button_style(),
            tooltip="最大化",
        )
        self.close = ft.IconButton(
            icon=ft.Icons.CLOSE_ROUNDED,
            icon_size=16,
            icon_color=self.theme_colors["text"],
            on_click=self.close_window,
            style=self.get_button_style(hover_color="#C42B1C"),
            tooltip="关闭",
        )
        return ft.Row(
            controls=[
                self.top,
                self.full,
                self.min,
                self.max,
                self.close,
            ],
            spacing=5,
        )

    def get_button_style(self, hover_color=None):
        """获取按钮样式"""
        return ft.ButtonStyle(
            padding=12,
            shape=ft.RoundedRectangleBorder(radius=0),
            bgcolor={
                "": self.theme_colors["surface"],
                "hovered": hover_color or self.theme_colors["hover"],
            },
        )

    def create_title_bar(self, page: ft.Page):
        """创建标题栏"""
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.WindowDragArea(
                        content=ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image("src\\assets\\icon.png"),
                                    ft.Text(
                                        page.title,
                                        size=13,
                                        color=self.theme_colors["text"],
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ],
                                spacing=8,
                            ),
                            padding=ft.padding.only(left=12, top=8, bottom=8),
                        ),
                        expand=True,
                    ),
                    self.create_window_controls(),
                ],
                spacing=0,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=self.theme_colors["surface"],
            height=40,
            border=ft.border.only(bottom=ft.BorderSide(1, self.theme_colors["border"])),
        )

    def create_navigation_rail(self, change_page_handler):
        """创建导航栏"""
        return ft.NavigationRail(
            selected_index=self.current_index,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=200,
            extended=True,
            bgcolor=self.theme_colors["surface"],
            indicator_color=self.theme_colors["primary"],
            destinations=[
                ft.NavigationRailDestination(
                    icon=page.get("icon", ft.Icons.QUESTION_MARK),
                    selected_icon=page.get("selected_icon", ft.Icons.QUESTION_MARK),
                    label=page.get("label", "未命名"),
                )
                for page in self.pages
            ],
            on_change=change_page_handler,
        )

    def create_content_area(self):
        """创建内容区域"""
        return ft.Container(
            content=ft.Text("主页内容", color=self.theme_colors["text"]),
            expand=True,
            padding=20,
        )

    def create_main_layout(self, page: ft.Page):
        """创建主布局"""
        content_area = self.create_content_area()

        # 单页时不显示侧边栏
        if len(self.pages) <= 1:
            return ft.Column(
                controls=[self.create_title_bar(page), content_area],
                spacing=0,
                expand=True,
            )
        else:
            navigation_rail = self.create_navigation_rail(self.change_page_content)
            return ft.Column(
                controls=[
                    self.create_title_bar(page),
                    ft.Row(
                        controls=[
                            navigation_rail,
                            ft.VerticalDivider(width=1),
                            content_area,
                        ],
                        spacing=0,
                        expand=True,
                    ),
                ],
                spacing=0,
                expand=True,
            )

    def change_page_content(self, e):
        """处理页面切换"""
        self.current_index = int(e.control.selected_index)
        self.content_area.content = self.pages[self.current_index]["func"](self)
        self.content_area.update()

    def toggle_always_on_top(self, e):
        """切换窗口置顶状态"""
        e.control.page.window.always_on_top = not e.control.page.window.always_on_top
        e.control.selected = e.control.page.window.always_on_top
        e.control.page.update()

    def minimize_window(self, e):
        """最小化窗口"""
        e.control.page.window.minimized = True
        e.control.page.update()

    def toggle_maximize(self, e):
        """切换最大化状态"""
        if e.control.page.window.full_screen:
            self.toggle_fullscreen(e)
        else:
            e.control.page.window.maximized = not e.control.page.window.maximized
            e.control.page.update()

    def toggle_fullscreen(self, e):
        """切换全屏状态"""
        is_fullscreen = not e.control.page.window.full_screen
        e.control.page.window.full_screen = is_fullscreen
        self.full.selected = is_fullscreen
        e.control.page.update()

    def close_window(self, e):
        """关闭窗口"""
        e.control.page.window.close()

    def update_pages(self, new_pages):
        """更新页面配置"""
        # 记住当前选中的页面
        current_label = self.pages[self.current_index]["label"] if self.pages else None

        self.pages = new_pages

        if self.the_page:
            # 清除当前页面内容
            self.the_page.controls.clear()

            # 创建新的布局
            self.main_content = self.create_main_layout(self.the_page)

            # 获取内容区域
            if len(self.pages) <= 1:
                self.content_area = self.main_content.controls[1]
            else:
                self.content_area = self.main_content.controls[1].controls[2]

            # 恢复之前的选中状态
            if current_label:
                for i, page in enumerate(self.pages):
                    if page["label"] == current_label:
                        self.current_index = i
                        break

            # 更新当前显示的内容
            self.content_area.content = self.pages[self.current_index]["func"](self)
            self.the_page.add(self.main_content)
            self.the_page.update()

    def get_ui(self):
        """获取UI函数"""

        def f(page: ft.Page):
            self.the_page = page
            self.setup_window(page)
            self.main_content = self.create_main_layout(page)

            # 获取内容区域
            if len(self.pages) <= 1:
                self.content_area = self.main_content.controls[1]
            else:
                self.content_area = self.main_content.controls[1].controls[2]

            self.content_area.content = self.pages[self.current_index]["func"](self)
            page.add(self.main_content)

        return f
