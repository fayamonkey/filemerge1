
# Modified sent_tokenize that doesn't rely on punkt_tab
from nltk.tokenize.punkt import PunktSentenceTokenizer
import re

def custom_sent_tokenize(text, language='english'):
    try:
        # Try the standard tokenizer first
        from nltk.tokenize import sent_tokenize as nltk_sent_tokenize
        return nltk_sent_tokenize(text, language)
    except LookupError:
        # Fall back to simple regex-based tokenization
        return re.split(r'(?<=[.!?])\s+', text)

# Install our custom function into NLTK
import nltk.tokenize
nltk.tokenize.sent_tokenize = custom_sent_tokenize
