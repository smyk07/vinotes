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

- [x] 1.5 Setup Directory Creation in `.vinotes/utils/create_note.py` (make it so that anyone can make a file like `./literature/books/Metamorphosis Franz Kafka.md`)

- [x] 1.6 shift all file creation to pathlib

- [x] 1.7 write a create-vault bash script to make a fresh vault every install

  - [x] clone git repo for creation of vault

- [x] 1.8 open file when created option in `config.json`.

- [ ] 1.9 after all config fields are setup for the first release, divide the "categories" of config to different lists.

- [x] 1.10 Add principle directory configuration options in `config.json`

  - [x] internal functionality at `todo-2.6`
  - [x] removes zettelkasten default features, upto the user to create principle directories, will only ship with daily and example templates.

- [x] 1.11 Implement a fuzzy finder functionality within the command `vn open-note`

- [x] 1.12 Clean up code, fix variables (24-07-2024).

- [ ] 1.13 add functionality for updating utilities if theres ever a new live update on GitHub.

  - [x] New command `vn update`
  - [x] Pull tracked files from remote, check if updates are needed by comparing data, update required files.
  - [ ] figure out a way to update new config fields with retaining the changes made by the user - can be done with the json library.

- [ ] 1.14 Dev mode

  - [x] create `dev.config.json`, accessible from `config-manager.py`

# 2. Commands

- [x] 2.1 help - `.vinotes/utils/help.py`

  - [x] write help docs for all commands until now

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

- [x] 2.5 - trashed - backup vault - users can setup their backup themselves.

- [x] 2.6 - add command `vn reload` to check for new templates and new principle directories.

- [x] 2.7 command - `vn open-note`

  - [x] Basic implementation
  - [x] # fuzzy finder (todo-1.11)

- [ ] 2.8 comamnd - `vn update` to update binaries and utilities.

- [x] 2.9 commmand - `vn changelog` - opens changelog in nvim.

# 3. Releases

- [x] v1.0 - First Production Release

  - [x] test for errors & bugs
  - [x] update `.vinotes/bin/help.sh`
  - [x] create setup script (either in bash or python)
  - [x] update `README.md` (usage, docs, credits)
  - [x] PUSH & PUBLISH RELEASE!

- [ ] v1.1 - Second Production Release

  - [ ] test for errors & bugs
  - [ ] update `.vinotes/bin/help.sh`
  - [ ] create setup script (either in bash or python)
  - [ ] update `README.md` (usage, docs, credits)
  - [ ] update `CHANGELOG.md`
  - [ ] PUSH & PUBLISH RELEASE!
