from openai import OpenAI
client = OpenAI()
import argparse
import json

def retrieve_batch_api_responses(batch_id):
    batch_status = client.batches.retrieve(batch_id)
    print("\nBatch status:")
    print(batch_status)
    print("Output file ID: ", batch_status.output_file_id)

    print("Downloading output file...")
    file = client.files.content(batch_status.output_file_id)
    file_data_bytes = file.read()

    # write the file data to a new file
    with open("batch_output.jsonl", "wb") as file:
        file.write(file_data_bytes)

def merge_responses_into_json(batch_file_path):
    conditions = []
    
    with open(batch_file_path, "r") as file:
        for line in file:
            data = json.loads(line)
            response_body = data.get("response", {}).get("body", {})
            tool_calls = response_body.get("choices", [])[0].get("message", {}).get("tool_calls", [])
            for call in tool_calls:
                arguments = json.loads(call.get("function", {}).get("arguments", "{}"))
                conditions.extend(arguments.get("conditions", []))

    merged_conditions = {"conditions": conditions}

    with open("merged_conditions.json", "w") as file:
        json.dump(merged_conditions, file, indent=4)

    return merged_conditions


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve batch API responses from OpenAI")
    parser.add_argument("batch_id", type=str, help="Batch ID")
    args = parser.parse_args()

    retrieve_batch_api_responses(args.batch_id)
    merge_responses_into_json("batch_output.jsonl")