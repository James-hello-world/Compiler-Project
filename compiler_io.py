from pathlib import Path
from sys import exit


# Check Input File with Path Object
def get_input_path(file_name):
    file_path = Path(file_name)
    if not file_path.is_file():
        print(f"[ERROR] Could not locate '{file_name}'!")
        exit(1)
    return file_path

# Check Output File
def get_output_path(is_tokenizer):
    if is_tokenizer:
        return Path("finalp2.txt")
    return Path("finalp3.py")

# Read from Input File
def read_lines(file_name="finalp1.txt"):
    with open(get_input_path(file_name), "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Write to Output File
def write_lines(lines, is_tokenizer):
    output_path = get_output_path(is_tokenizer)
    with open(output_path, "w") as file:
        file.writelines([line + "\n" for line in lines])

# Backup Output
def execute_output(file_name="finalp3.py"):
    file_path = Path(file_name)
    if not file_path.is_file():
        print(f"[ERROR] Could not find {file_name}")
        exit(1)
    with open(file_path) as file:
        code = compile(file.read(), file_name, "exec")
        exec(code)
    print("------------------------------\n")
