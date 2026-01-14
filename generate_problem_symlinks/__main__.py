import os
import re
import sys
import glob

def extract_number_from_docstring(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    # Extract the first triple-quoted docstring
    match = re.search(r'"""(.*?)"""', content, re.DOTALL)
    if not match:
        match = re.search(r"'''(.*?)'''", content, re.DOTALL)
    if match:
        docstring = match.group(1)
        num_match = re.search(r'\b(\d+)\b', docstring)
        if num_match:
            return num_match.group(1)
    return None

def symlink_with_number(src, dest_folder):
    number = extract_number_from_docstring(src)
    if not number:
        print(f"No number found in docstring for {src}.")
        return
    filename = os.path.basename(src)
    symlink_name = f"{number}_{filename}"
    dest_path = os.path.join(dest_folder, symlink_name)
    os.makedirs(dest_folder, exist_ok=True)
    if not os.path.exists(dest_path):
        os.symlink(os.path.abspath(src), dest_path)
        print(f"Symlink created: {dest_path}")
    else:
        print(f"Symlink already exists: {dest_path}")

# Usage: python script.py "glob_pattern" /path/to/dest_folder
if __name__ == "__main__":
    pattern = sys.argv[1]
    dest_folder = sys.argv[2]
    for src_file in glob.glob(pattern):
        symlink_with_number(src_file, dest_folder)