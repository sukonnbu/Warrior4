@echo off


if not exist "%appdata%\.warrior4\warrior4.db" goto pass

del %appdata%\.warrior4\warrior4.db
echo Data Removed

:pass

pause