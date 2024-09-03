from pathlib import Path
import urllib.request
import urllib.error
from rich import print
import json

# dir variables, for testing
dir = "./"

print(f"Creating new [light_green]Vinotes[/] vault in [light_green bold]{dir}[/]")

# counter variable
file_counter = 0


def fetch_dir_contents(url: str):
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print(f"Errors while fetching directory contents: {err.code} {err.reason}")
        quit()


def fetch_and_write_file(file: dict):
    # fetching file contents
    try:
        with urllib.request.urlopen(file["download_url"]) as response:
            file_contents = response.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        print(f"Errors while fetching file contents: {err.code} {err.reason}")
        quit()

    # create directory if they dont exist
    dir_path = Path(dir + "/".join(file["path"].split("/")[:-1]))
    dir_path.mkdir(parents=True, exist_ok=True)

    # write files
    Path(dir + file["path"]).write_text(file_contents)


# fetch contents of .vinotes directory
vinotes_contents_json = fetch_dir_contents(
    "https://api.github.com/repos/smyk07/vinotes/contents/.vinotes?ref=dev"
)

# managing individual files within .vinotes
for f in [f for f in vinotes_contents_json if f["download_url"]]:
    fetch_and_write_file(f)
    file_counter += 1

# managing directories within .vinotes
for d in [d for d in vinotes_contents_json if not d["download_url"]]:
    if d["name"] == "dist":
        continue
    dir_contents_json = fetch_dir_contents(d["url"])
    for subf in [subf for subf in dir_contents_json if subf["download_url"]]:
        fetch_and_write_file(subf)
        file_counter += 1

print(
    "[light_green bold]New vinotes vault successfully created in the current directory.[/]"
)
print(f"[cyan bold]{file_counter}[/] files created")
