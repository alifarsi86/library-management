# 📚 Library Management System

A simple, modular library management system built with Python. This project was created as a programming exercise to practice object-oriented programming, Python modules and packages, and local package installation with `pip`.

The application provides a command-line interface for managing a collection of books, while the core library functionality is organized into a reusable Python package.

## ✨ Features

- **Add books** — add a book using its title and author.
- **Remove books** — remove a book by title.
- **Search books** — look up a book by title.
- **Display all books** — view the books currently stored in the library.
- **Modular structure** — keep the library logic separate from the command-line interface.
- **Reusable package** — import the `Library` class from the `mylibrary` package.
- **Local installation** — install the package from the project directory using `pip`.

## 🧰 Built With

- **Python 3**
- Python modules and packages
- Object-oriented programming (OOP)
- `setuptools` and `pip` for local package installation

No third-party runtime dependencies are required for the core functionality, unless additional dependencies have been introduced in your local version.

## 📁 Project Structure

```text
library-management/
├── mylibrary/
│   ├── __init__.py
│   └── library.py       # Library class and book-management methods
├── main.py              # Command-line entry point
├── setup.py             # Package installation configuration
├── README.md            # Project documentation
└── .gitignore           # Files and folders excluded from Git
```

Generated folders such as `build/`, `*.egg-info/`, and `__pycache__/` may also appear locally after building or running the project. They are generated artifacts and generally do not need to be committed to Git.

## ✅ Requirements

- Python 3
- `pip`

To check that Python and pip are available, run:

```bash
python --version
python -m pip --version
```

Depending on your environment, you may need to use `python3` instead of `python`.

## 🚀 Getting Started

### 1. Get the project

Clone the repository after it has been published to GitHub, replacing the placeholder URL with your repository's actual URL:

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

Alternatively, download the repository as a ZIP file and open the project folder in your terminal or code editor.

### 2. Install the package locally

From the project's root directory—the directory containing `setup.py`—run:

```bash
python -m pip install .
```

This installs the package using the configuration in `setup.py`. If you edit the package source later and want to test those changes without reinstalling each time, you can use an editable installation:

```bash
python -m pip install -e .
```

### 3. Run the application

From the project root, run:

```bash
python main.py
```

Follow the menu shown in the terminal to add, remove, search for, or display books.

> **Note:** Run the command from the project root so Python can locate the project files as expected.

## 💻 Using the Package in Python

After installing the package locally, you can import the `Library` class from another Python file or an interactive Python session:

```python
from mylibrary.library import Library

library = Library()

library.add_book("The Hobbit", "J. R. R. Tolkien")
library.show_books()

library.search_book("The Hobbit")
library.remove_book("The Hobbit")
```

This example demonstrates the expected method calls. The exact messages or return values depend on how the methods are implemented in `mylibrary/library.py`.

## 🧠 How It Works

The project separates the application into two main parts:

- **`mylibrary/library.py`** contains the `Library` class and the methods responsible for adding, removing, searching for, and displaying books.
- **`main.py`** provides the command-line interface and runs the menu when the file is executed directly.

The `if __name__ == "__main__":` guard helps keep the command-line startup behavior separate from code that is imported as a module.

The package's `__init__.py` file marks `mylibrary` as a Python package and can also be used to define a more convenient public import interface.

## 📦 Package Installation Notes

This project demonstrates **local package installation** with `pip install .`. That does not automatically publish the package to the Python Package Index (PyPI). Publishing to PyPI is a separate process that requires package metadata and distribution files to be prepared and uploaded.

## ⚠️ Current Scope

Book data is kept in the program's in-memory list. Unless persistence has been added separately, the collection resets when the application process ends. The project does not claim to provide database storage, user accounts, or a graphical interface.

## 🔮 Possible Improvements

Ideas for future development include:

- Save and load the book collection from a JSON file or database.
- Add input validation and clearer error handling.
- Support duplicate-title handling and more flexible search options.
- Add automated tests with `unittest` or `pytest`.
- Improve the package metadata and prepare a release for PyPI.
- Add type hints and more detailed docstrings.

## 🎯 Learning Goals

This project is intended to provide practice with:

- Defining and using Python classes
- Organizing code into modules and packages
- Importing custom modules
- Using the `__name__ == "__main__"` pattern
- Configuring a package with `setup.py`
- Installing a local Python package with `pip`

## 📄 License

No license has been specified in this repository yet. Add a `LICENSE` file if you plan to grant others explicit permission to use, modify, or distribute the project.

---

**Built as a Python learning project.**
Made with Python 🐍 and curiosity. Made by Ali Farsi.
