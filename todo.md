# Individial Functionality
- [x] Setup virtualenv activate script - `.vinotes/bin/activate.sh`

- [x] Setup templating system for file creation (other than daily) - `.vinotes/utils/create_note.py`
  - [x] file creation
  - [x] apply template content `.vinotes/templates/manager.py` and `.vinotes/utils/create_note.py`

- [ ] Custom template creation / detection system
  - [ ] detect templates automatically
  - [ ] if directory does not exist, ask weather to create or exit from user (every time create_note runs)

# Vinote Commands
- [x] help - `.vinotes/bin/help.sh`
- [x] open vault - `.vinotes/bin/openvault.sh`
- [ ] open / create daily
  - [ ] ignore daily directory option in `create_note.py`
  - [ ] file creation and apply template content
- [ ] create zettelkasten notes in `create_note.py`
  - [x] fleeting notes - on the fly, raw data
  - [ ] literature notes - from books, articles, web, distill the quotes and information 
  - [ ] permanent notes - interpret the above two into a single idea in our own words
- [ ] backup vault 
