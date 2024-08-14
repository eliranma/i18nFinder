# i18nFinder

## Overview

This Python tool automates the extraction of translation keys from a project directory. It searches for strings inside `t()` function calls (commonly used for internationalization) in specified file types (like `.js`, `.ts`). The extracted keys are saved into a JSON file, ready for localization tasks.

## Features

- **Recursive Directory Search**: Scans all files within the specified directory and its subdirectories.
- **Customizable File Extensions**: Specify which file types to search (e.g., `.js`, `.ts`).
- **Robust Error Handling**: Manages file access issues and unexpected conditions gracefully.
- **JSON Output**: Saves translation keys in a JSON file format, which is ideal for i18n purposes.
- **User-Friendly Prompts**: Asks for user confirmation before overwriting an existing output file.

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **No External Dependencies**: This tool uses only Python's standard libraries.

## Installation

1. Clone this repository or download the script file.
2. Ensure Python 3.x is installed.

## Usage

To run the tool, use the following command in your terminal:

```sh
python i18nFinder.py -b /path/to/project -e "js,ts" -o output_file.json
```

## Command-Line Arguments
•	-b, --base-path (Required) : The base directory path where the search will begin.  
•	-e, --extensions (Required) : A comma-separated list of file extensions to search. Example: "js,ts".  
•	-o, --output (Required) : The path where the JSON output file will be saved. If the file exists, you will be prompted to confirm whether to overwrite it.  
