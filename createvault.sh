#!/bin/bash

echo "▷ Cloning repo..."
echo ""
command git clone https://github.com/smyk07/vinotes.git .

echo "▷ Repo Cloned"
command rm -rf .git todo.md README.md

echo ""
echo "▷ Get started by entering the command:"
echo "    source .vinotes/bin/activate.sh"
echo ""
echo "▷ You can alias the above command in your ~/.bashrc to make it easier to enter into the vault."
echo ""
echo "▷ Make sure to edit your config by entering the command:"
echo "    vinotes conf"
echo ""
echo "▷ This default vault comes with a Zettlekasten note-taking system and a daily-note creation feature"
echo ""
echo "▷ For customization, view the documentation"
