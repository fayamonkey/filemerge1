@echo off
echo ===================================
echo  FileMerger App - Complete Fix Tool
echo ===================================
echo.
echo This script will:
echo 1. Fix NLTK data issues
echo 2. Modify app.py to use a more robust tokenization approach
echo.
echo A backup of app.py will be created before any changes.
echo.
pause

if exist venv\Scripts\activate (
    echo Activating virtual environment...
    call venv\Scripts\activate
) else (
    echo Virtual environment not found, using system Python.
)

echo.
echo Step 1: Running NLTK data fix...
echo ===============================
python fix_nltk.py

echo.
echo Step 2: Modifying app.py...
echo ========================
python modify_app.py

echo.
echo Fix complete! You can now run the app using run.bat
echo.
pause 