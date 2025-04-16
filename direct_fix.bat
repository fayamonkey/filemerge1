@echo off
echo =================================
echo  FileMerger App - Direct Fix Tool
echo =================================
echo.
echo This script will directly create the missing NLTK punkt_tab files
echo and patch app.py to handle future issues gracefully.
echo.
echo This is a more direct approach that should resolve the punkt_tab issues.
echo.
pause

if exist venv\Scripts\activate (
    echo Activating virtual environment...
    call venv\Scripts\activate
) else (
    echo Virtual environment not found, using system Python.
)

echo.
echo Running direct fix...
echo ====================
python direct_fix.py

echo.
echo Direct fix complete! You can now run the app using run.bat
echo.
pause 