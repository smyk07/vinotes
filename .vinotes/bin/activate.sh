# Bash prompt variables
OLD_PS1="${PS1}"
NEW_PS1="(vinotes) ${PS1}"

# update bash prompt
export PS1=${NEW_PS1}

# handling path
export VIRTUAL_ENV="/mnt/e/coding-projects/vinotes/.vinotes/"
OLD_PATH="$PATH"
NEW_PATH="$VIRTUAL_ENV/bin:$PATH"

# update path
export PATH=${NEW_PATH}

# deactivate function
deactivate() {
  export PATH=${OLD_PATH}
  export PS1=${OLD_PS1}
  echo "Bye..."
}
