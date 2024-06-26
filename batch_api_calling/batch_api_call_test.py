from openai import OpenAI
client = OpenAI()

# batch_input_file = client.files.create(
#   file=open("batch_input.jsonl", "rb"),
#   purpose="batch"
# )

# batch_input_file_id = batch_input_file.id

# response = client.batches.create(
#     input_file_id=batch_input_file_id,
#     endpoint="/v1/chat/completions",
#     completion_window="24h",
#     metadata={
#       "description": "Mark's test batch 6 real call",
#     }
# )

# print("\nBatch created:")
# print(response)


# batches = client.batches.list(limit=10)
# print("\nBatches:")
# print(batches)

batch_status = client.batches.retrieve("batch_LRze8RMBfJt9FQW1sbigClQu")
print("\nBatch status:")
print(batch_status)
print("Output file ID: ", batch_status.output_file_id)

print("Downloading output file...")
file = client.files.content("file-hDJog2k6CXDskRKFwFwHz9gV")
file_data_bytes = file.read()

# write the file data to a new file
with open("batch_output.jsonl", "wb") as file:
    file.write(file_data_bytes)