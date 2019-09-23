#!/bin/sh

# Clean-up
rm -f editor.py main_window.py icons_rc.py *.pyc *.bak

# Generate resource & UI
pyrcc5 icons.qrc -o icons_rc.py
pyuic5.bat ./ui/editor.ui -o editor.py
pyuic5.bat ./ui/main_window.ui -o main_window.py

# Execute
python -m main
