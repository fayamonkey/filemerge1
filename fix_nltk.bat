@echo off
echo Running NLTK data fix...

if exist venv\Scripts\activate (
    call venv\Scripts\activate
) else (
    echo Virtual environment not found, using system Python.
)

python fix_nltk.py
echo.
echo If there were no errors, you can now start the app using run.bat
pause 