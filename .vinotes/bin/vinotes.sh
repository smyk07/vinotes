# Do not touch the below code unless you are really confident
case $0 in
open-daily | od)
  # execute daily note creation and opening python script
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
