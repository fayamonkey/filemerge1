"""
Modify app.py to use the custom tokenization function.
Run this script if you still encounter NLTK punkt_tab issues.
"""

import os
import sys
import re
import shutil

# Path to app.py
app_path = 'app.py'

# Check if app.py exists
if not os.path.exists(app_path):
    print(f"Error: {app_path} not found. Make sure you're running this script from the correct directory.")
    sys.exit(1)

# Create a backup
backup_path = f"{app_path}.bak"
try:
    shutil.copy2(app_path, backup_path)
    print(f"Created backup of {app_path} at {backup_path}")
except Exception as e:
    print(f"Warning: Could not create backup: {str(e)}")

# Read the content of app.py
try:
    with open(app_path, 'r', encoding='utf-8') as f:
        content = f.read()
except Exception as e:
    print(f"Error reading {app_path}: {str(e)}")
    sys.exit(1)

# Define the code to insert at the top
top_insert = """# Added by modify_app.py to fix NLTK issues
import sys
sys.path.insert(0, '.')  # Add current directory to path
try:
    import custom_tokenize  # Import custom tokenization module
except ImportError:
    print("Warning: custom_tokenize.py not found. Run fix_nltk.py first.")

"""

# Define the code to modify the chunk_by_tokens function
chunk_by_tokens_pattern = r"def chunk_by_tokens\(text, max_tokens=500\):.*?return chunks"
chunk_by_tokens_replacement = """def chunk_by_tokens(text, max_tokens=500):
    # Modified to use a more reliable sentence tokenization approach
    try:
        sentences = sent_tokenize(text)
    except Exception as e:
        # Last resort: split by periods, question marks, and exclamation points
        print(f"Warning: Using simple sentence splitting due to error: {str(e)}")
        sentences = re.split(r'(?<=[.!?])\\s+', text)
    
    chunks = []
    current_chunk = []
    current_token_count = 0
    
    for sentence in sentences:
        # Approximate token count by words (not perfect but simple)
        try:
            sentence_token_count = len(word_tokenize(sentence))
        except:
            # Fall back to simple word counting if tokenization fails
            sentence_token_count = len(sentence.split())
        
        if current_token_count + sentence_token_count > max_tokens and current_chunk:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
            current_token_count = sentence_token_count
        else:
            current_chunk.append(sentence)
            current_token_count += sentence_token_count
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks"""

# Add the import at the top of the file
modified_content = top_insert + content

# Replace the chunk_by_tokens function
modified_content = re.sub(
    chunk_by_tokens_pattern, 
    chunk_by_tokens_replacement, 
    modified_content,
    flags=re.DOTALL
)

# Write the modified content back to app.py
try:
    with open(app_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    print(f"Successfully modified {app_path} to use custom tokenization")
except Exception as e:
    print(f"Error writing to {app_path}: {str(e)}")
    print(f"You can restore the backup from {backup_path}")
    sys.exit(1)

print("\nApp.py has been modified to use a more robust tokenization approach.")
print("You can now run the FileMerger App.")
print(f"If you encounter issues, you can restore the backup from {backup_path}") 