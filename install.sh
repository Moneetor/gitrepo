#!/bin/bash
if [ -e ~/bin ]; then
    echo "Installing Python files..."
    chmod u+x ./git-repo.py
    ln -s ./git-repo.py ~/bin/git-init
fi