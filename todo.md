# How this todo will work

- There will be a branch for each todo (`todo1.1`, `todo1.2`, etc.)
- These branches will stem off the `dev` branch.
- The dev branch will merge into `version` branches, where minor bug fixes will take place.
- And then finally each `version` branch will merge into the `main` branch for each tag.

# 1 Internal Functionality
- [x] 1.1 Setup virtualenv activate script - `.vinotes/bin/activate.sh`

- [x] 1.2 Setup templating system for file creation (other than daily) - `.vinotes/utils/create_note.py`
  - [x] file creation
  - [x] apply template content `.vinotes/templates/manager.py` and `.vinotes/utils/create_note.py`

- [ ] 1.3 Custom template creation / detection system
  - [ ] detect templates automatically
  - [ ] if directory does not exist, ask weather to create or exit from user (every time create_note runs)

# 2 Commands
- [x] 2.1 help - `.vinotes/bin/help.sh`

- [x] 2.2 open vault - `.vinotes/bin/openvault.sh`

- [ ] 2.3 open / create daily
  - [ ] ignore daily directory option in `create_note.py`
  - [ ] file creation and apply template content

- [ ] 2.4 create zettelkasten notes in `create_note.py`
  - [x] fleeting notes - on the fly, raw data
  - [ ] literature notes - from books, articles, web, distill the quotes and information 
  - [ ] permanent notes - interpret the above two into a single idea in our own words

- [ ] 2.5 backup vault 
