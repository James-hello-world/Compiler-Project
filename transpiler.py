import compiler_io
from constants import SymbolType, TRANSPILER_SYMBOLS


def find_begin(lines):
    for index, line in enumerate(lines):
        if line == "begin":
            return index
    return -1


def remove_declaration(lines):
    index = find_begin(lines)
    if index == -1:
        return lines
    return lines[index+1:]


def format_spaces(line):
    output = []
    for index in range(len(line)):
        current_token = line[index]
        if current_token in TRANSPILER_SYMBOLS[SymbolType.LEFT_SPACED]:
            output.append(" ")

        output.append(current_token)

        if current_token in TRANSPILER_SYMBOLS[SymbolType.RIGHT_SPACED]:
            output.append(" ")

        # `+` and `-` are special, since they can be part of numbers
        if current_token in TRANSPILER_SYMBOLS[SymbolType.SIGN]:
            preceding_token = line[index-1]
            succeeding_token = line[index+1]
            # if succeeding token comprises numbers, current token may be a sign
            if succeeding_token.isnumeric():
                if preceding_token in TRANSPILER_SYMBOLS[SymbolType.CAN_PREDATE_SIGN]:
                    continue  # don't add space after current token
            # if not a sign, then it must be an addition or subtraction operator
            # these should have a space after them
            output.append(" ")
    return output


def remove_semicolons(line):
    return line[:-1] if line[-1] == ";" else line


def format_for_test_exec(lines):
    output = []
    for line in lines:
        if "print" in line:
            continue
        output.append(line)
    return "".join([line + "\n" for line in output])


def transpile(lines):
    output = []
    code_segment = remove_declaration(lines)
    for line in code_segment:
        if line == "end.":
            break

        tokens = line.split()
        space_formatted = format_spaces(tokens)
        semicolon_removed = remove_semicolons(space_formatted)
        output.append("".join(semicolon_removed))

    test_run_target = format_for_test_exec(output)
    try:
        exec(test_run_target)
    except NameError:
        print("[ERROR]: Unknown identifier")
        exit(1)

    print("Resulting Python 3 code:")
    print("------------------------------")
    for index, line in enumerate(output):
        print(f"Line {index+1: >3}: {line}")
    print("------------------------------\n")

    return output


if __name__ == "__main__":
    print("Transpiler-only mode enabled")
    file_contents = compiler_io.read_lines("finalp2.txt")
    compiler_io.write_lines(transpile(file_contents), False)
