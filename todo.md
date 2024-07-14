# 0. How this todo will work

- There will be a branch for each feature (`todo1.1`, `todo1.2`, etc.)
- These feature branches will merge into main when the feature implementation is complete (as this is a small project for now)

(upon release of the first production version, `dev` will split off `main`, which will then act as the parent for all feature branches.)

_First production version will be released at the completion of 1.4, 2.3, and 2.5._

# 1. Internal Functionality
- [x] 1.1 Setup virtualenv activate script - `.vinotes/bin/activate.sh`

- [x] 1.2 Setup templating system for file creation (other than daily) - `.vinotes/utils/create_note.py`
  - [x] file creation
  - [x] apply template content `.vinotes/templates/manager.py` and `.vinotes/utils/create_note.py`

- [ ] 1.3 Custom template creation / detection system
  - [ ] detect templates automatically
  - [ ] if directory does not exist, ask weather to create or exit from user (every time create_note runs)

- [x] 1.4 Setup Configuration `.vinotes/config.json`
  - [x] setup `.vinotes/utils/config-manager.py`
  - [x] setup `.vinotes/config.json`
  - [x] write appropriate `config.json`
  - [x] implement in all applicable `utils`

# 2. Commands
- [x] 2.1 help - `.vinotes/bin/help.sh`

- [x] 2.2 open vault - `.vinotes/bin/openvault.sh`

- [x] 2.3 open / create daily
  - [x] create template for daily
  - [x] ignore daily directory option in `create_note.py`
  - [x] file creation and apply template content for daily note and open note

- [x] 2.4 create zettelkasten notes in `create_note.py`
  - [x] fleeting notes - on the fly, raw data
  - [x] literature notes - from books, articles, web, distill the quotes and information 
  - [x] permanent notes - interpret the above two into a single idea in our own words
  - [x] update `template_manager.py`
  - [x] testing

- [ ] 2.5 backup vault 

# 3. Releases
- [ ] v1.0 - First Prodiction Release
  - [ ] test for errors & bugs
  - [ ] update `.vinotes/bin/help.sh`
  - [ ] create setup script (either in bash or python)
  - [ ] update `README.md` (usage, docs, credits)
  - [ ] PUSH & PUBLISH RELEASE!
