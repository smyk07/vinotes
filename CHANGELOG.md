# Changelog for Version 1.3

## Structure Changes

- `shell-executable` field in config.
- CLI is not hard coded in bash anymore, utilities system is completely revamped in python using Typer. This will help in cross-platform support later on.

## Feature Changes

- Files can now be created alongside the other principle directories, without needing a principle directories in the root directory of the vault (root template).
- Added 3rd-party plugins feature.
