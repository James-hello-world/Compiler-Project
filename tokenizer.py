from pathlib import Path

import compiler_io
from constants import TOKENIZER_SYMBOLS


def has_hyphens(line):
    #Check if a line of code contains double hyphens
    if "--" in line:
        return True
    return False


def is_balanced(line):
    #Checks whether a line has 1 or 2 sets of double hyphens
    if line.count("--") % 2 == 0:
        return True
    return False


def starts_with_hyphens(line):
# Check if line starts with hyphens
    hyphen_count = 0
    for character in line:
        if hyphen_count == 2:
            return True
        if character == "-":
            hyphen_count += 1
            continue
        if character == " ":
            continue
        if character == "\t":
            continue
        return False


def ends_with_hyphens(line):
# Check if line ends with hyphens
    hyphen_count = 0
    for character in reversed(line):
        if hyphen_count == 2:
            return True
        if character == "-":
            hyphen_count += 1
            continue
        if character == " ":
            continue
        if character == "\t":
            continue
        return False


def format_line(line):
# Format Tokens 
    characters = []
    words = []
    is_string_literal = False

    # Add to the character list until a full word is made and add it to words
    # Then clear character and move on to next token
    for character in line:
        # treat alphabets, digits, and quotation marks as part of the word
        if (
            character.isalnum() or
            character == "." or
            character == "\""
        ):
            characters.append(character)
            if character == "\"":
                is_string_literal = False if is_string_literal else True
            continue
            
        if character == " ":
            # Ignore spaces not in between words
            if characters:
                words.append("".join(characters))
                characters.clear()
            continue

        # special symbols are also tokens by themselves
        if character in TOKENIZER_SYMBOLS:
            # check for `"value="`, where `=` appears inside of the string literal
            if is_string_literal:
                characters.append(character)
                continue
            # if there's a missing space before a symbol, characters list will not be empty
            if characters:
                words.append("".join(characters))
                characters.clear()
            # add the symbol as token to words list
            words.append(character)
            continue

    # if there are no terminal spaces or newlines at end of line
    # then there's one last token in the characters list
    if characters:
        words.append("".join(characters))
    return " ".join(words)


def tokenize(lines):
# Make a list of tokens from the line from the input file
    output = []
    is_comment_block = False
    code_segment = ""

    for line in lines:
        # Remove blank line
        if not line:
            continue

        # Remove comments
        if starts_with_hyphens(line):
            if ends_with_hyphens(line):
                continue
            is_comment_block = True
            continue
        if is_comment_block:
            if ends_with_hyphens(line):
                is_comment_block = False
                continue
            continue
        # In-line comment
        if has_hyphens(line):
            # Start of block comment
            if not is_balanced(line):
                is_comment_block = True
            index = line.find("--")
            code_segment = line[:index]

        # Format code segment of line or whole line, and add to output list
        # if there's a comment in the line, `code_segment` would not be empty
        # else, it's empty and the whole line should be formatted
        output.append(format_line(code_segment) if code_segment else format_line(line))
        code_segment = ""
    print("Tokenization complete.")
    return output


if __name__ == "__main__":
    print("Tokenizer-only mode enabled")
    file_contents = compiler_io.read_lines()
    compiler_io.write_lines(tokenize(file_contents), True)
