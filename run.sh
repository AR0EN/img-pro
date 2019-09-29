#!/bin/bash -i

# Check OS & Shell
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
        echo "Unknown environment: $OSTYPE!"
        echo "The application has been tested in Windows (MSYS), and Linux (Bash) only!"
        exit 1
        ;;
esac

# Check dependencies
python -m check_dependencies
result="$?"

if [ "0" != "$result" ]; then
    exit 1
fi

# Generate Resource & UI
PYRCC icons.qrc -o icons_rc.py
PYUIC ./ui/editor.ui -o editor.py
PYUIC ./ui/main_window.ui -o main_window.py

# Execute
python -m main
