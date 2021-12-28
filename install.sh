#!/bin/bash
if [ -e ~/bin ]; then
    start=$(pwd)
    echo "Installing Python files..."
    chmod u+x ./git-repo.py
    ln -s "$start/git-repo.py" ~/bin/git-init
fi