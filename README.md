# Chemical Simulator GUI

A cross-platform chemical process simulation GUI built using Python, PyQt5, and OpenModelica.

This project provides a graphical interface for creating and simulating chemical process flowsheets using unit operations and thermodynamic models.

---

# Features

* PyQt5-based graphical user interface
* Flowsheet creation and editing
* Material stream handling
* Unit operation support
* OpenModelica integration
* Equation-based simulation support
* Sequential modular simulation support
* Undo / Redo functionality
* CSV result generation
* Cross-platform support (Windows + Linux)

---

# Project Structure

```text
Chemical-Simulator-GUI/
├── src/
│   └── main/
│       └── python/
├── requirements.txt
├── requirements-windows.txt
├── ChemicalSimulator.spec
├── README.md
└── .gitignore
```

---

# Requirements

## Common Requirements

* Python 3.11
* OpenModelica
* pip
* virtualenv

## Python Dependencies

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

# OpenModelica Installation

## Linux (Ubuntu/Debian)

Install OpenModelica:

```bash
sudo apt update
sudo apt install openmodelica
```

Verify installation:

```bash
which omc
```

Expected output:

```bash
/usr/bin/omc
```

---

## Windows

Download and install OpenModelica from the official website:

[https://openmodelica.org/download/download-windows](https://openmodelica.org/download/download-windows)

Default installation path:

```text
C:\Program Files\OpenModelica1.25.4-64bit\bin\omc.exe
```

---

# Linux Setup

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd Chemical-Simulator-GUI
```

---

## 2. Create Virtual Environment

```bash
python3.11 -m venv env
```

---

## 3. Activate Environment

```bash
source env/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

---

## 5. Run Application

```bash
python src/main/python/Landing_page.py
```

---

# Windows Setup

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd Chemical-Simulator-GUI
```

---

## 2. Create Virtual Environment

```powershell
python -m venv env
```

---

## 3. Activate Environment

```powershell
env\Scripts\activate
```

---

## 4. Install Dependencies

```powershell
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install -r requirements-windows.txt
```

---

## 5. Run Application

```powershell
python src/main/python/Landing_page.py
```

---

# Cross-Platform Support

This project supports both:

* Linux
* Windows

Platform-specific functionality is handled internally using Python platform checks.

---

# Common Issues

## OpenModelica Not Found

### Linux

Check:

```bash
which omc
```

### Windows

Verify that OpenModelica is installed at:

```text
C:\Program Files\OpenModelica1.25.4-64bit\bin\omc.exe
```

---

## Missing Dependencies

Reinstall dependencies:

```bash
pip install -r requirements.txt
```

---

## PyQt5 Errors

Install system dependencies on Linux:

```bash
sudo apt install python3-pyqt5
```

---

# Development Notes

This project uses:

* Python
* PyQt5
* OpenModelica
* CSV-based result processing
* Pandas for data handling

---

# Recommended Improvements

Future improvements may include:

* Better error handling
* Automatic OpenModelica detection
* Docker support
* Executable packaging
* Enhanced flowsheet editor
* CI/CD integration
* Plugin architecture
* More unit operations

---

# Git Ignore

Recommended `.gitignore`:

```gitignore
__pycache__/
*.pyc
env/
venv/
build/
dist/
*.csv
*.log
```

---

# Contributing

Contributions are welcome.

You can contribute by:

* Fixing bugs
* Improving documentation
* Adding unit operations
* Improving Linux compatibility
* Enhancing GUI features

---

# License

Choose an open-source license before public release.

Recommended:

* MIT License
* Apache License 2.0

---

# Author

Chirag Koyande

---

# Acknowledgements

* OpenModelica
* PyQt5
* Python Community
