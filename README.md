
# Book Search Engine

## What does it do?

- Search for books from a huge library of online books using the Open Library API
- Find editions and authors of books you like or want to read

## How to Use

### Using the Executable

1. Download the executable from the `dist` folder (or from your distribution source).
2. Double-click the `.exe` file to run the application. No Python installation is required.

### Building the Executable Yourself

If you want to build the executable from source:

1. Make sure you have Python 3.7+ installed.
2. Install dependencies:
	```powershell
	python -m venv .venv
	.venv\Scripts\activate
	pip install pyinstaller
	```
3. Build the executable:
	```powershell
	.venv\Scripts\pyinstaller.exe --onefile main.py
	```
4. The executable will be created in the `dist` folder.

---
For any issues, please open an issue on the repository.
