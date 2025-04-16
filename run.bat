@echo off 
call venv\Scripts\activate 
python -c "import nltk; try: nltk.data.find('tokenizers/punkt'); except LookupError: nltk.download('punkt')" 
streamlit run app.py 
pause 
