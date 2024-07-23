# Vinotes - External Markdown Note-Taking Utility for Neovim\^

^ or any text editor...

The motivation for me to create this project was for me to take notes in Neovim systematically. This repository is always open to contributions. Happy hacking :)

Create a vault in the current (empty) directory by pasting this command:

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/smyk07/vinotes/main/createvault.sh)"
```

When you first create a vault, you want to activate the vault, and setup configurations (more information below).

## Features

Vinotes comes with a simple note-taking system which includes:

- Zettelkasten System for:
  - Fleeting Notes
  - Literature Notes
  - Permanent Notes
- Daily notes

## Requirements

- Linux
- Git
- python3
- nvim, vim or any text editor for editing markdown files.

## Getting Started & Basic Usage

**You can access all of Vinotes' commands with either the `vinotes` or the `vn` prefix.**

### Activation

You first have to activate the Vinotes vault to access all of the commands for interaction as follows:

```
source .vinotes/bin/activate.sh
```

### Edit Configuration

To edit the configuration (in `nano`):

```
vinotes conf
```

### Create notes

To create notes in Vinotes, you can use either the `create-note` or `cn` keyword.

You can use any of the three commands below, for either a Fleeting, Literature, or Permanent note (For customization, refer to [Wiki](https://github.com/smyk07/vinotes/wiki)):

```
vinotes create-note fleeting/<name_of_note>

vinotes create-note literature/<name_of_note>

vinotes create-note permanent/<name_of_note>
```

_you do not need to give the file-extension, all files are created in markdown (`.md`) by default_

For example (with short-forms):

```
vn cn fleeting/books/1984 by George Orwell
```

### Open Daily

To open today's daily note, enter the command:

```
vinotes open-daily

OR

vn od
```

### Help

You can access help using any of the following commands:

```
vinotes --help

OR

vinotes -h

OR

vn --help

OR

vn -h
```

## Contributing

Follow the below steps:

1. Create an issue for a feature.
2. Fork the repo, add describe the feature in `todo.md`.
3. After the feature is properly implemented, create a pull request.
