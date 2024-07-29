# Changelog for Version 1.1

## Structure Changes

- Code is cleaned and optimized.

- `vn create-note` command structure has been made simpler, `vn create-note <principle_dir>/<file_path>`

- Vinotes now does not ship with the default templates for the zettelkasten note-taking system, instead allows user to create their own principle directories when editing config. (option to have a zettelkasten system is still there.)

  - All templates deleted except daily and example.
  - The defualt config will contain the 3 zettelkasten principle directories, but templates and directories will not be created unless the vault is **reloaded**.

## Feature Changes

- `vn reload` - detects changes for principle directories in `.vinotes/config.json`, and then creates new directories and templates.
- `vn open-note`

  - When file path is provided, the file is opened,
  - When file path is not provided, will open a fuzzy-finder to search across all notes in principle directories.

- `vn changelog` - open the `CHANGELOG.md` file in vim.

- `vn update` - updates binaries and utilities, and configs from main branch
