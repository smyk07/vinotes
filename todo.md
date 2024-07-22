# 0. How this todo will work

- There will be a branch for each feature (`todo1.1`, `todo1.2`, etc.)
- These feature branches will merge into `dev` when the feature implementation is completed
- The `dev` branch is merged into `main` for every major release update.

# 1. Internal Functionality

- [x] 1.1 Setup virtualenv activate script - `.vinotes/bin/activate.sh`

- [x] 1.2 Setup templating system for file creation (other than daily) - `.vinotes/utils/create_note.py`

  - [x] file creation
  - [x] apply template content `.vinotes/templates/manager.py` and `.vinotes/utils/create_note.py`

- [x] 1.3 Custom template creation / detection system

  - [x] detect templates automatically

- [x] 1.4 Setup Configuration `.vinotes/config.json`

  - [x] setup `.vinotes/utils/config-manager.py`
  - [x] setup `.vinotes/config.json`
  - [x] write appropriate `config.json`
  - [x] implement in all applicable `utils`

- [ ] 1.5 Setup Directory Creation in `.vinotes/utils/create_note.py` (make it so that anyone can make a file like `./literature/books/Metamorphosis Franz Kafka.md`)

- [x] 1.6 shift all file creation to pathlib

- [ ] 1.7 write a create-vault bash script to make a fresh vault every install

# 2. Commands

- [x] 2.1 help - `.vinotes/bin/help.sh`

- [x] 2.2 - trashed - open vault - `.vinotes/bin/openvault.sh` (Functionality trashed cuz doesnt make sense)

  - [x] basic integration (just opens `./index.md`)
  - [ ] every time command is run:
    - [x] update `index.md` with past 5 daily files --- `config.md` integration opportunity for how many files to display
    - [x] update `index.md` with random quote
    - [ ] update `index.md` with latest created files (very experimental and exceptional to first production release)

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
