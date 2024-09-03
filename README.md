# Vinotes - External Markdown Note-Taking Utility for Neovim\^

^ or any text editor...

The motivation for me to create this project was for me to take notes in Neovim systematically. This repository is always open to contributions. Happy hacking :)

Refer to [Kickstart](https://github.com/smyk07/vinotes/wiki/1.-Kickstart) to get started, or run this command in your corrent (empty) directory:

```
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/smyk07/vinotes/main/create-vault.py)"
```

For more in-depth documentation and on customizations, refer to the [Wiki](https://github.com/smyk07/vinotes/wiki).

## Default Features

Vinotes's default config comes with a simple note-taking system which includes:

- Zettelkasten System for:
  - Fleeting Notes
  - Literature Notes
  - Permanent Notes
- Daily notes

You may either edit the `principle_dirs` field in the config to customize vinotes according to your liking, or use the default config and try Vinotes out for the first time.

## Requirements

- Linux (cross-platform support coming soon)
- Git
- python3
- fzf
- nvim, vim or any text editor for editing markdown files.

## Contributing

Follow the below steps:

1. Create an issue for a feature.
2. Fork the repo, describe the feature in `todo.md`.
3. After the feature is properly implemented, create a pull request.
