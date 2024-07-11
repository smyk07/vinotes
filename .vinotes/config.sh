# vinotes - Markdown Note-Taking Utility for Neovim
# First step: change the vault_name variable
# Second step: source this .config file in your .bashrc
# Third step: happy note-taking :)

# Please name your vault appropriately, with no spaces and special characters...
# Also do not give the same name to more than one vault...
vault_name='my_vault_name'

# Do not touch the below code unless you are really confident
vinotes() {
  if [[ "$1" = $vault_name ]]; then
    shift
    case $1 in
    open-daily | od)
      # execute daily note creation and opening python script
      ;;
    open-literature | ol)
      # execute literature file opening script
      ;;
    create-literature | cl)
      # execute literature file creation script
      ;;
    open-random | or)
      # execute random file opening script
      ;;
    create-random | cr)
      # execute random file creation script
      ;;
    open)
      # execute vault opening python script
      ;;
    backup)
      # execute git backup script
      ;;
    --help | -h)
      # execute help message script
      ;;
    *)
      echo "Please enter a valid parameter... (use -h for help)"
      ;;
    esac
    return
  else
    echo "Please enter a valid vault name... (use -h for help)"
    return
  fi
}
