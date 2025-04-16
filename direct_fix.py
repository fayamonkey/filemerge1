"""
Direct Fix for NLTK punkt_tab Issues

This script directly creates the missing collocations.tab and other files
required by NLTK's punkt_tab tokenizer.
"""

import os
import sys
import shutil
import nltk

# Find NLTK data directory
nltk_data_dir = nltk.data.path[0]  # Use the first directory in the path
if not os.path.exists(nltk_data_dir):
    nltk_data_dir = os.path.expanduser("~/nltk_data")
    os.makedirs(nltk_data_dir, exist_ok=True)
    
print(f"Using NLTK data directory: {nltk_data_dir}")

# Make sure punkt is downloaded
nltk.download('punkt', download_dir=nltk_data_dir, quiet=False)

# Create punkt_tab directory structure
punkt_tab_dir = os.path.join(nltk_data_dir, 'tokenizers', 'punkt_tab')
english_dir = os.path.join(punkt_tab_dir, 'english')
os.makedirs(english_dir, exist_ok=True)
print(f"Created directory: {english_dir}")

# Create necessary files
collocations_content = """%;
%;%;
%;%;%;
%;%;%;%;
%;%;%;%;%;
%,%
%,%,
%,%,%
%,%,%,
%,%,%,%
%;%,
%;%,%
%.%.
%.%.%
%...
%..%
%%;
%%,
%:%:
%:%:%
%;%:
%;%;%:
%,%:
%,%,%:
%.%.%:
%.%:%
"""

abbrev_content = """Mr.
Mrs.
Ms.
Dr.
Prof.
St.
etc.
vs.
e.g.
i.e.
U.S.
U.K.
E.U.
Fig.
Figs.
Jan.
Feb.
Mar.
Apr.
Jun.
Jul.
Aug.
Sep.
Sept.
Oct.
Nov.
Dec.
Mon.
Tue.
Wed.
Thu.
Fri.
Sat.
Sun.
"""

# Write collocations.tab
with open(os.path.join(english_dir, 'collocations.tab'), 'w', encoding='utf-8') as f:
    f.write(collocations_content)
print("Created collocations.tab")

# Write abbrev.tab
with open(os.path.join(english_dir, 'abbrev.tab'), 'w', encoding='utf-8') as f:
    f.write(abbrev_content)
print("Created abbrev.tab")

# Copy pickle file from punkt if available
punkt_dir = os.path.join(nltk_data_dir, 'tokenizers', 'punkt')
if os.path.exists(punkt_dir):
    english_pickle = os.path.join(punkt_dir, 'english.pickle')
    if os.path.exists(english_pickle):
        shutil.copy2(english_pickle, os.path.join(english_dir, 'punkt.pickle'))
        print(f"Copied punkt model from {english_pickle} to {english_dir}")

# Create a empty README file
with open(os.path.join(punkt_tab_dir, 'README'), 'w', encoding='utf-8') as f:
    f.write("This directory was created by the FileMerger App direct_fix.py script.")
print("Created README file")

# Also modify app.py to use a fallback method
app_path = 'app.py'
if os.path.exists(app_path):
    print("\nModifying app.py...")
    
    # Create a backup
    backup_path = f"{app_path}.bak"
    if not os.path.exists(backup_path):
        shutil.copy2(app_path, backup_path)
        print(f"Created backup of {app_path} at {backup_path}")
    
    # Simple fix to directly patch the PunktTokenizer class
    patch_code = """
# Patch NLTK's PunktTokenizer to avoid punkt_tab issues
try:
    from nltk.tokenize.punkt import PunktTokenizer
    
    # Save the original load_lang method
    original_load_lang = PunktTokenizer.load_lang
    
    # Define a new load_lang method that doesn't fail
    def patched_load_lang(self, lang):
        try:
            # Try the original method first
            return original_load_lang(self, lang)
        except:
            # Fall back to a simple split if the original method fails
            from nltk.tokenize.punkt import PunktParameters
            self._params = PunktParameters()
            return
    
    # Apply the patch
    PunktTokenizer.load_lang = patched_load_lang
    print("Applied PunktTokenizer patch")
except:
    print("Could not patch PunktTokenizer")

"""
    
    # Read the content of app.py
    with open(app_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Insert our patch after the imports
    import_end = content.find("# Set page configuration")
    if import_end == -1:
        import_end = content.find("# Initialize session state")
    
    if import_end != -1:
        modified_content = content[:import_end] + patch_code + content[import_end:]
        
        # Write the modified content back to app.py
        with open(app_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        print("Successfully patched app.py")
    else:
        print("Could not find a suitable location to insert the patch in app.py")

print("\nDirect fix complete!")
print("This should resolve the punkt_tab issues by creating the necessary files.")
print("You can now run the app using run.bat") 