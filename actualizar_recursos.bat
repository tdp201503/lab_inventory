@echo off
for /R "%~dp0" %%# in (*.qrc) do pyrcc4 %%~n#.qrc -o %%~n#_rc.py