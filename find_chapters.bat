@echo off
setlocal enabledelayedexpansion

set "file=C:\Users\YUKI\Desktop\那一束月光\index.html"
set "lineNum=0"

for /f "delims=" %%a in ('type "%file%"') do (
    set /a lineNum+=1
    if "%%a"=="                }," (
        echo Line !lineNum!: %%a
    )
)
