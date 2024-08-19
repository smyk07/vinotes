# Bash prompt variables
OLD_PS1="${PS1}"
NEW_PS1="(vinotes) ${PS1}"

# update bash prompt
export PS1=${NEW_PS1}

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

# install vinotes
command pip install --user ${PWD}/.vinotes/dist/vinotes-0.1.0-py3-none-any.whl >/dev/null 2>&1

# deactivate function
deactivate() {
  export PS1=${OLD_PS1}
  command pip uninstall ${PWD}/.vinotes/dist/vinotes-0.1.0-py3-none-any.whl --yes >/dev/null 2>&1
  unset cd
  unset deactivate
  echo "Bye..."
}
