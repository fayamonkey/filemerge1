# FileMerger App

A Streamlit application for converting various document formats to Markdown, with options for merging and chunking documents for AI consumption.

## Features

- **Document Conversion**: Convert various file formats to Markdown:
  - PDF (.pdf)
  - Word (.docx, .doc)
  - PowerPoint (.pptx, .ppt)
  - Excel/CSV (.xlsx, .xls, .csv)
  - HTML (.html, .htm)
  - Text (.txt, .text)
  - Markdown (.md, .markdown)
  - Data formats (.json, .xml, .yaml, .yml)
- **Bulk Processing**: Upload and process multiple files simultaneously
- **Output Options**: 
  - Merge all documents into a single Markdown file
  - Process each document individually and download as a ZIP archive
- **Advanced AI-Friendly Chunking**:
  - Smart Paragraph chunking (respects document structure and headings)
  - Semantic chunking (groups similar content using TF-IDF and cosine similarity)
  - Structure-based chunking (splits by document headings and sections)
  - Traditional token-based chunking
  - Configurable thresholds and settings for each method
- **Metadata Enrichment**: 
  - Add source information and chunk identifiers to processed documents
  - Automatic keyword extraction from content
  - Customizable number of keywords per chunk
  - Token count information for each chunk
- **Clean, Professional UI**: Intuitive interface with navigation sidebar

## Installation

### Windows (Easy Setup)
1. Simply run the `setup.bat` file by double-clicking it or running it from the command prompt.
2. After installation completes, run the application using the generated `run.bat` file.

### Manual Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/filemerger-app.git
   cd filemerger-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Download required NLTK data:
   ```
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

5. Run the application:
   ```
   streamlit run app.py
   ```

## Usage

1. **Upload Files**: 
   - Navigate to the "Upload Files" section
   - Drag and drop or click to select files
   - Supported formats: PDF, Word, PowerPoint, Excel, HTML, Text, etc.

2. **Process Files**:
   - Choose output format (single file or multiple files)
   - Enable chunking if desired and select chunking method:
     - Smart Paragraph: Respects document structure and preserves headings
     - Semantic: Groups content by similarity (requires scikit-learn)
     - Structure-based: Splits by document headings and sections
     - Token-based: Splits by approximate token count
   - Configure metadata options including keyword extraction
   - Click "Process Files" button

3. **Download Results**:
   - Preview the converted content
   - Download as a single Markdown file or ZIP archive

## Chunking Methods Explained

### Smart Paragraph
Intelligently groups paragraphs, respecting document structure like headings. Creates new chunks at logical boundaries.

### Semantic Chunking
Uses TF-IDF and cosine similarity to group content by meaning. Similar paragraphs stay together, making chunks more coherent for AI processing.

### Structure-based Chunking
Preserves document hierarchy by creating chunks based on headings. Each section becomes its own chunk when possible.

### Token-based Chunking
Traditional chunking method that creates chunks of approximately equal token counts, splitting at sentence boundaries.

## Requirements

- Python 3.8+
- Streamlit
- PyPDF2/pdfplumber
- python-docx
- python-pptx
- pandas
- openpyxl
- pytesseract (for OCR capabilities)
- NLTK (for text chunking and keyword extraction)
- scikit-learn (for advanced semantic chunking)
- BeautifulSoup4 (for HTML processing)
- tabulate (for table formatting)

See `requirements.txt` for the full list of dependencies.

## Project Structure

- `app.py`: Main Streamlit application file
- `requirements.txt`: Python dependencies
- `setup.bat`: Automated setup script for Windows
- `run.bat`: Script to start the application on Windows
- Documentation:
  - `README.md`: Project overview and instructions
  - `thoughts.md`: Development thought process
  - `journal.md`: Development journal
  - `projectplan.md`: Detailed project plan
  - `checklist.md`: Development progress tracker

## License

MIT

## Acknowledgements

- Icons by [Icons8](https://icons8.com/)
- Built with [Streamlit](https://streamlit.io/) 