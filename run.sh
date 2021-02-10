#!/bin/bash -i

# Check OS & Shell - TBD

# Check dependencies
python -m check_dependencies
result="$?"

if [ "0" != "$result" ]; then
    echo "Please make sure the following items installed properly:"
    echo $'\t Python'
    echo $'\t OpenCV v4.1.0 or above'
    echo $'\t PyQt5'
    exit 1
fi

python -m check_generated_files

# Generate Resource & UI
# PYRCC icons.qrc -o icons_rc.py
# PYUIC ./ui/editor.ui -o editor.py
# PYUIC ./ui/main_window.ui -o main_window.py

# Execute
python -m main
