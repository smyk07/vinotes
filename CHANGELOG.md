# Changelog for Version 1.1

## Structure Changes

- Code is cleaned and optimized.

- Vinotes now does not ship with the default zettelkasten note-taking system, instead allows user to create their own principle directories when editing config.

  - Templates also deleted
  - The defualt config will contain the 3 zettelkasten directories, but templates and directories will not be created unless **reloaded**.

## Feature Changes

- `vn reload` - detects changes for principle directories in `.vinotes/config.json`, and then creates new directories and templates.
- `vn open-note`

  - When file path is provided, the file is opened,
  - When file path is not provided, will open a fuzzy-finder to search across all notes in principle directories.
