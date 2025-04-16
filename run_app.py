"""
Simple script to run the FileMerger Streamlit app.
This is just a convenience wrapper for 'streamlit run app.py'.
"""
import os
import subprocess
import sys

def main():
    print("Starting FileMerger App...")
    try:
        # Check if streamlit is installed
        subprocess.run([sys.executable, "-m", "pip", "show", "streamlit"], 
                      check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("Streamlit is not installed. Installing required packages...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Run the Streamlit app
    subprocess.run(["streamlit", "run", "app.py"])

if __name__ == "__main__":
    main() 