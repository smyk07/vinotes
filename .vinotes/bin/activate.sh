# Bash prompt variables
OLD_PS1="${PS1}"
NEW_PS1="(vinotes) ${PS1}"

# update bash prompt
export PS1=${NEW_PS1}

# handling path and venv variables
export VIRTUAL_ENV="$PWD/.vinotes/"
OLD_PATH="$PATH"
NEW_PATH="$VIRTUAL_ENV/bin:$PATH"

# update path
export PATH=${NEW_PATH}

# alias cd function
cd() {
  if [[ "$1" = '--force' ]] || [[ "$1" = '-f' ]]; then
    shift
    command cd "${@}"
    return
  fi
  command echo "Vinotes requires you to stay in your vault directory always."
  command echo "(use -f or --force to use the command but note that doing so, Vinotes functionality may break.)"
  command echo ""
}

# alias vinotes function to vn
alias vn=vinotes

# deactivate function
deactivate() {
  export PS1=${OLD_PS1}
  export PATH=${OLD_PATH}
  unset cd
  unset deactivate
  echo "Bye..."
}
