import os
import sys

# Check if the right number of command-line arguments are provided
if len(sys.argv) != 4:
    print("Usage: python script_name.py <directory> <search_word> <output_file>")
    sys.exit(1)

# Define the directory to scan
directory1 = sys.argv[1]

# Define the word to search for
search_word1 = sys.argv[2]

# Define the output file to store scan results
output_file1 = sys.argv[3]


# Function to scan a file for the word and save results to the output file
def scan_file_for_word(file_path, word, output):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_number = 0
            for line in file:
                line_number += 1
                if word in line:
                    result = f'Found "{word}" in {file_path}, line {line_number}: {line.strip()}\n'
                    output.write(result)
    except Exception as e:
        error_message = f'Error scanning {file_path}: {str(e)}\n'
        print(error_message)


# Open the output file for writing
with open(output_file1, 'w', encoding='utf-8') as output:
    # Recursively scan all files in the directory
    for root, _, files in os.walk(directory1):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            scan_file_for_word(file_path, search_word1, output)
