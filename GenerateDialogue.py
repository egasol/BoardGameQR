from TextToSpeech import TextToSpeech
import sys
import json
import argparse
from pathlib import Path


FILE_IGNORE = "map.json"
KEYS_INCLUDE = ["dialogue", "enter"]


def find_dialogue_files(map_path):
    file_list = list(map_path.glob("*.json"))
    # TODO: Change to exclude list of filenames
    if FILE_IGNORE in file_list:
        file_list.pop(FILE_IGNORE)

    return file_list


def extract_dialogue(file_list):
    dialogue_list = []

    for file_path in file_list:
        with open(file_path, "r") as f:
            file_dict = json.load(f)

        dialogue_list.extend(find_dialogue_keys(file_dict))

    return dialogue_list


def find_dialogue_keys(input_dict):
    dialogue_keys = []

    for key, value in input_dict.items():
        if isinstance(value, dict):
            dialogue_keys.extend(find_dialogue_keys(value))
        elif key.lower() in KEYS_INCLUDE:
            if isinstance(value, str):
                dialogue_keys.append(value)
            elif isinstance(value, list):
                dialogue_keys.extend(value)

    return dialogue_keys


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("path", type=Path, help="path to map folder")
    parser.add_argument("--voice", type=str, default="Dave",
                        help="voice to use (default: Dave)")
    parser.add_argument("--overwrite", type=bool, default=False,
                        help="overwrite files (default: False)")

    args = parser.parse_args()

    tts = TextToSpeech()

    file_list = find_dialogue_files(args.path)
    dialogue_list = extract_dialogue(file_list)

    print("Found", len(dialogue_list), "lines of dialogue.")

    # TODO: Add common modifiers (ex. scout action)

    print("Generating audio...")

    # TODO: Remove duplicates in dialogue_list

    for dialogue in dialogue_list:
        tts.generate_audio(dialogue, play_audio=False)
