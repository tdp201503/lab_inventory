@echo off
for /R "%~dp0" %%# in (*.ui) do pyuic4 %%~n#.ui -o %%~n#.py