import argparse
from openai import OpenAI
client = OpenAI()
import json
import os

from gpt import extract_info

def generate_batch_input_jsonl(condition_documents_folder_path):

    # List of all files in the folder
    files = os.listdir(condition_documents_folder_path)

    for file in files:
        print(file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a JSONL file for batch API requests")
    parser.add_argument("condition_documents_folder", type=str, help="Path to the folder containing condition documents")
    args = parser.parse_args()

    generate_batch_input_jsonl(args.condition_documents_folder)