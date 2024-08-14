import os
import re
import json
import argparse
import sys


def find_strings_in_t_function(base_path, extensions):
    # t_function_pattern = re.compile(r"t\('([^']+)'\)")
    # t_function_pattern = re.compile(r"t\(\s*['\"]([^'\"]+)['\"]\s*\)")
    t_function_pattern = re.compile(r"(?<!\w)t\(\s*['\"]([^'\"]+)['\"]\s*\)")
    strings_dict = {}

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.split('.')[-1] in extensions:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    matches = t_function_pattern.findall(content)
                    for match in matches:
                        if match not in strings_dict:
                            strings_dict[match] = ""
                except (IOError, OSError) as e:
                    print(f"Error reading file {file_path}: {e}", file=sys.stderr)
    return strings_dict


def validate_base_path(base_path):
    while not os.path.exists(base_path):
        print(f"Error: The path '{base_path}' does not exist.")
        base_path = input("Please enter a valid base path: ")
    return base_path


def parse_extensions(extensions_str):
    return [ext.strip() for ext in extensions_str.split(",")]


def save_to_json(data, output_path):
    try:
        if os.path.exists(output_path):
            response = input(
                f"The file {output_path} already exists. Do you want to overwrite it? (y/n): ").strip().lower()
            if response != 'y':
                print("Operation canceled.")
                return

        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
        print(f"JSON file saved successfully at {output_path}")
    except (IOError, OSError) as e:
        print(f"Error saving JSON file to {output_path}: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Search for strings inside t() functions in specified file types.")
    parser.add_argument("-b", "--base-path", required=True, type=str, help="The base path of the project to search in.")
    parser.add_argument("-e", "--extensions", type=str, required=True,
                        help="A string of space-separated file extensions to search for (e.g., 'js,ts').")
    parser.add_argument("-o", "--output", type=str, required=True, help="The output file path to save the JSON data.")

    args = parser.parse_args()

    try:
        base_path = validate_base_path(args.base_path)
        extensions = parse_extensions(args.extensions)

        result = find_strings_in_t_function(base_path, extensions)
        if not result:
            print("No matching strings found.")
        else:
            save_to_json(result, args.output)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
