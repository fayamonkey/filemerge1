"""
Fix NLTK Data Issues

This script downloads all necessary NLTK data packages for the FileMerger App.
Run this script if you encounter NLTK-related errors.
"""

import nltk
import sys
import os
import shutil
from pathlib import Path

print("Fixing NLTK Data Issues...")

# Find all possible NLTK data directories
nltk_data_dirs = nltk.data.path

# Create a new directory if none exists
if not nltk_data_dirs or not any(os.path.exists(d) for d in nltk_data_dirs):
    user_dir = os.path.expanduser("~/nltk_data")
    os.makedirs(user_dir, exist_ok=True)
    print(f"Created NLTK data directory: {user_dir}")
    nltk_data_dirs = [user_dir]

# Choose the first writable directory
nltk_data_dir = None
for d in nltk_data_dirs:
    if os.path.exists(d) and os.access(d, os.W_OK):
        nltk_data_dir = d
        break

if not nltk_data_dir:
    user_dir = os.path.expanduser("~/nltk_data")
    os.makedirs(user_dir, exist_ok=True)
    nltk_data_dir = user_dir
    
print(f"Using NLTK data directory: {nltk_data_dir}")

# Download all required packages
print("Downloading NLTK data packages...")

# Essential packages for the application
packages = [
    'punkt',
    'stopwords',
    'averaged_perceptron_tagger',
    'wordnet',
    'omw-1.4'
]

# Download each package
for package in packages:
    print(f"Downloading {package}...")
    nltk.download(package, download_dir=nltk_data_dir, quiet=False)

# Download all popular packages to ensure punkt_tab is included
print("Downloading popular packages (includes punkt_tab)...")
nltk.download('popular', download_dir=nltk_data_dir, quiet=False)

# Handle punkt_tab specifically
punkt_tab_dir = os.path.join(nltk_data_dir, 'tokenizers', 'punkt_tab')
punkt_dir = os.path.join(nltk_data_dir, 'tokenizers', 'punkt')

# If punkt_tab doesn't exist but punkt does, try to create a symlink or copy
if not os.path.exists(punkt_tab_dir) and os.path.exists(punkt_dir):
    print("Creating punkt_tab from punkt...")
    try:
        os.makedirs(os.path.join(nltk_data_dir, 'tokenizers', 'punkt_tab'), exist_ok=True)
        english_dir = os.path.join(punkt_tab_dir, 'english')
        os.makedirs(english_dir, exist_ok=True)
        
        # Copy PY files from punkt to punkt_tab
        punkt_files = [f for f in os.listdir(punkt_dir) if f.endswith('.pickle')]
        for file in punkt_files:
            source = os.path.join(punkt_dir, file)
            dest = os.path.join(english_dir, file)
            shutil.copy2(source, dest)
            print(f"Copied {source} to {dest}")
        
        # Create a simple README file to document the fix
        with open(os.path.join(punkt_tab_dir, 'README.txt'), 'w') as f:
            f.write("This directory was created by the FileMerger App fix_nltk.py script to handle punkt_tab requirements.")
        
        print("Successfully created punkt_tab directory and copied necessary files")
    except Exception as e:
        print(f"Error setting up punkt_tab: {str(e)}")

# Fix punkt_tab English directory specifically
try:
    english_dir = os.path.join(punkt_tab_dir, 'english')
    os.makedirs(english_dir, exist_ok=True)
    
    # Create a minimal PunktToken model file if it doesn't exist
    model_file = os.path.join(english_dir, 'punkt.pickle')
    if not os.path.exists(model_file):
        source_file = os.path.join(punkt_dir, 'english.pickle')
        if os.path.exists(source_file):
            shutil.copy2(source_file, model_file)
            print(f"Copied punkt model from {source_file} to {model_file}")
except Exception as e:
    print(f"Error setting up punkt_tab English directory: {str(e)}")

# Create a modified version of sent_tokenize that doesn't require punkt_tab
print("Creating a modified tokenize function...")

modified_code = """
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
"""

custom_tokenize_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "custom_tokenize.py")
with open(custom_tokenize_path, 'w') as f:
    f.write(modified_code)

print(f"Created custom tokenize module at {custom_tokenize_path}")

# Verify everything is working
print("\nVerifying NLTK installations...")
try:
    from nltk.tokenize import sent_tokenize
    test_text = "This is a test sentence. This is another one."
    sentences = sent_tokenize(test_text)
    print(f"Tokenization working! Result: {sentences}")
except Exception as e:
    print(f"Error with tokenization: {str(e)}")
    print("You may need to modify app.py to use the custom tokenization module.")

print("\nAll NLTK data fixes have been applied.")
print("If you still encounter issues, try running the app with this code at the top of your script:")
print("\nimport sys")
print("sys.path.insert(0, '.') # Add current directory to path")
print("import custom_tokenize # Import the custom tokenization module")
print("\nYou can now run the FileMerger App.") 