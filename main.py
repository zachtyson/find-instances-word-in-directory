import os

# Define the directory to scan
directory = 'C:/Users/Zachary/WebstormProjects/CaSMM_fork_2023/server/'

# Define the word to search for
search_word = 'day'

# Define the output file to store scan results
output_file = 'scan_results.txt'


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
        # output.write(error_message)
        print(error_message)
        # do not output error message to file


# Open the output file for writing
with open(output_file, 'w', encoding='utf-8') as output:
    # Recursively scan all files in the directory
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            scan_file_for_word(file_path, search_word, output)
