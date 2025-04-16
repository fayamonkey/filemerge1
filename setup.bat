@echo off
echo Setting up FileMerger App...

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Ensuring scikit-learn is properly installed...
pip install --upgrade scikit-learn

echo Downloading NLTK data...
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('popular')"

echo Creating run.bat file...
echo @echo off > run.bat
echo call venv\Scripts\activate >> run.bat
echo streamlit run app.py >> run.bat
echo pause >> run.bat

echo Running direct fix for NLTK issues...
python direct_fix.py

echo Setup complete! You can now run the app using run.bat
echo.
pause 