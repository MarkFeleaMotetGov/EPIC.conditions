import argparse
from openai import OpenAI
client = OpenAI()
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gpt import extract_info_chunked, count_conditions

def generate_batch_input_jsonl(condition_documents_folder_path):

    # List of all files in the folder
    files = os.listdir(condition_documents_folder_path)

    for file in files:
        print(file)
        # file_path = os.path.join(condition_documents_folder_path, file)
        # with open(file_path, 'r') as f:
            # file_conditions_count = count_conditions(f)
            # print(file_conditions_count, file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a JSONL file for batch API requests")
    parser.add_argument("condition_documents_folder", type=str, help="Path to the folder containing condition documents")
    args = parser.parse_args()

    generate_batch_input_jsonl(args.condition_documents_folder)