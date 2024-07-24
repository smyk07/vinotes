#!/bin/bash

echo "▷ Cloning repo..."
echo ""
command git clone https://github.com/smyk07/vinotes.git .

echo ""
echo "▷ Repo Cloned"
command rm -rf .git todo.md README.md

echo ""
echo "▷ Initial Setup Done ✔"

echo ""
echo "▷ Get started by entering the command:"
echo "    source .vinotes/bin/activate.sh"
echo ""
echo "▷ You can alias the above command in your ~/.bashrc to make it easier to activate Vinotes commands."
echo ""
echo "▷ Make sure to edit your config by entering the command:"
echo "    vn conf"
echo ""
echo "▷ After editing config.json, make sure to reload the vault using:"
echo "    vn reload"
echo ""
echo "▷ This default vault comes with a Zettlekasten note-taking system and a daily-note creation feature."
echo ""
echo "▷ Visit the kickstart wiki page for more information."
echo ""
echo "▷ For customization, view the detailed documentation."
