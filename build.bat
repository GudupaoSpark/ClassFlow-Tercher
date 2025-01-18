@echo off

echo 删除 build 目录
rmdir /s /q build

echo 删除 dist 目录
rmdir /s /q dist

echo 运行 Flet 构建
flet pack --icon assets\icon.ico main.py -D

echo 复制资源目录
xcopy /s /e /y /q /i "assets" "dist\main\assets"