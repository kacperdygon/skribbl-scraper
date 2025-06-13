# Skribbl Scraper

Scribbl scraper is a tool for collecting possible skribbl.io words. It uses a web browser driver to simulate gameplay and sends phrases to SQLite database.

## Requirements
- **Python**
- **Web browser** (Chrome, Firefox, Edge or Safari)

## Installation
### 1. Clone repo (or download zip) and create virtual enviroment
```
git clone https://github.com/kacperdygon/skribbl.io-scraper
cd skribbl.io-scraper-main
python -m venv .venv
```
### 2. Activate virtual enviroment
- Windows (cmd):
```
venv\Scripts\activate.bat
```
- Windows (PowerShell):
```
venv\Scripts\Activate.ps1
```
- Linux / macOS:
```
source venv/bin/activate
```
### 3. Install python packages
```
pip install -r "requirements.txt"
```

## Usage
### Run program:
```
python main.py
```
### Export words to json:
```
python export.py --language <language>
```
File with exported words will be named words.json. You can change export directory by using `--export-file <filename>` when running the program. Example:
```
python export.py --language polish --export-file list.json
```

## Configuration (config.json)

| Field                  | Description                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `browser`              | Browser to use. Can be one of: `"chrome"`, `"firefox"`, `"edge"`, `"safari"` (you need to have it installed first) |
| `browser_profile_path` | Path to a browser profile folder. If left empty, a fresh profile will be used                                      |
| `check_for_popups`     | Set to `true` to check for popup ads blocking UI (enable if no ad blocker is present)                              |
| `timeout`              | Time (in seconds) to wait for elements to load                                                                     |
| `iterations`           | Number of games to play (number or `"inf"` for infinite)                                                           |
| `start_tracker`        | Starts a tracker showing words per second at the end of all iterations (doesn't work with `"inf"`)                 |

### Lobby settings

| Field          | Description                                                                                                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `language`     | Language used in the game lobby, must be one of the languages avaible on skribbl.io (e.g. `"English"`, `"German"`)                       |
| `rounds`       | Number of rounds per game (2–10)                                                                                                         |
| `word_count`   | Number of word choices per round (1–5, no real reason to have less than 5)                                                               |
| `player_count` | Maximum number of players (bots). Can range from 2 to 15, since more than 15 will fail due to many players connecting from one IP adress |

## Notes
- Edge doesn't work for some reason, maybe I'll fix it
- Higher player count doesn't change much (I've recorded 8% performance increase when 15 bots were playing instead of 2, it's probably even smaller on worse systems)
- You can't open two browser instances of the same profile
- I suggest using Chrome without profile set or Firefox + uBlock Origin with `check_for_popups` set to `false` (you'll need to make a new profile and specify a path to it)
- Sometimes there is a long video ad on firefox lasting around 30 seconds, if you don't use adblock I suggest setting `timeout` to 35 or more (timeout doesn't impact efficiency in any way)