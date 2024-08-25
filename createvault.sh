#!/bin/bash

echo "▷ Cloning Vinotes github repo into ./vinotes_temp ..."
echo ""
command git clone https://github.com/smyk07/vinotes.git vinotes_temp

echo "▷ Copying files..."
echo ""
command cp -r ./vinotes_temp/.vinotes ./

echo "▷ Deleting temporary folder..."
echo ""
command rm -rf ./vinotes_temp

echo "▷ Removing Vinotes git remote..."
echo ""
command git remote remove origin

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
echo "▷ This default config comes with a Zettlekasten note-taking system and a daily-note creation feature, you can either edit the setup according to your needs, or keep it and try Vinotes out."
echo ""
echo "▷ Visit the kickstart wiki page for more information."
echo ""
echo "▷ For customization, view the detailed documentation."
