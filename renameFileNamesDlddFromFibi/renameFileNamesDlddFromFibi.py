import os

def reverse_lines(input_file, output_file):
    # Read lines from input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Reverse the order of lines and add line numbers
    reversed_lines = enumerate(reversed(lines), start=1)

    # Write reversed lines with line numbers to output file
    with open(output_file, 'w') as f:
        for line_number, line in reversed_lines:
            f.write(f"{line_number}.pdf\t{line.strip()}.pdf\n")


def rename_files(output_file, directory):
    # Read lines from output file
    with open(output_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Check if the number of files in the directory matches the number of lines
    files_in_directory = [file for file in os.listdir(directory) if file.endswith('.pdf')]
    if len(lines) != len(files_in_directory):
        print("Error: Number of files in the directory does not match the number of lines in the output file.")
        return

    # Check if all files to be renamed exist in the directory
    files_to_rename = [line.strip().split('\t')[0] for line in lines]
    if not all(file in files_in_directory for file in files_to_rename):
        print("Error: Not all files to be renamed exist in the directory.")
        return

    # Iterate over each line and rename files
    for line in lines:
        line_parts = line.strip().split('\t')
        if len(line_parts) == 2:
            old_file_name = os.path.join(directory, f"{line_parts[0]}")
            new_file_name = os.path.join(directory, line_parts[1])
            if os.path.exists(old_file_name):
                os.rename(old_file_name, new_file_name)
                print(f"File '{old_file_name}' renamed to '{str(new_file_name)}'")
            else:
                print(f"Error: File '{old_file_name}' does not exist.")
                return  # Abort renaming if any file doesn't exist

# Example usage:
# This is the file names in the format to be saved. the order to add lines to this file is from oldest to newest,
# using copy from the site and than modify the file names to remove spaces and fit the desired format (date, etc.).
# The file should be located in the script's folder.
#input_file = 'renameFileNamesDlddFromFibi//input.txt'
#output_file = 'renameFileNamesDlddFromFibi//reversed_output_with_file_numbers.txt'
#directory = 'renameFileNamesDlddFromFibi//pdfs//'  # Replace '/path/to/files' with the directory containing the pdf files to be renamed.
input_file = 'input.txt'
output_file = 'reversed_output_with_file_numbers.txt'
directory = 'pdfs//'  # Replace '/path/to/files' with the directory containing the pdf files to be renamed.
# The PDF files should be downloaded from the site and be numbered 1.pdf, 2.pdf, etc. - so that 1.pdf is the oldest file and the newest will have the biggest number.

print("Current working directory:", os.getcwd())

# Reverse lines and write to output file
reverse_lines(input_file, output_file)

# Rename files based on the content of the output file
rename_files(output_file, directory)
