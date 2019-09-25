#!/bin/sh

# Detect environment
case "$OSTYPE" in
    linux*)
        alias PYRCC=pyrcc5
        alias PYUIC=pyuic5
        ;;
    bsd*)
        alias PYRCC=pyrcc5
        alias PYUIC=pyuic5
        ;;
    msys*)
        alias PYRCC=pyrcc5
        alias PYUIC=pyuic5.bat
        ;;
    *)
        echo "unknown: $OSTYPE" ;;
esac

# Clean-up
rm -f editor.py main_window.py icons_rc.py *.pyc *.bak

# Generate resource & UI
PYRCC icons.qrc -o icons_rc.py
PYUIC ./ui/editor.ui -o editor.py
PYUIC ./ui/main_window.ui -o main_window.py

# Execute
python -m main
