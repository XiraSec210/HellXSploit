@echo off
title Installing...
pip install -r requirements.txt
cls
echo Installed succesfully!
echo.
echo Launching HellXSploit...
timeout /t 3>nul
start.bat