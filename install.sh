#!/bin/bash
if [ -e ~/bin ]; then
    echo "Installing Python files..."
    chmod u+x ./git-init
    ln -s ./git-init ~/bin/git-init
fi