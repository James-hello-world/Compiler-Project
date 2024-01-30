import compiler_io
from constants import TERMINALS, NON_TERMINALS, KEYWORDS, PARSING_TABLE


# Predective Parsing Method
def check_syntax(lines):
    stack = ["$", "P"]  # Make stack and push $, P to stack

    # Import input file into an Array as Tokens
    preprocessed_tokens = []
    for line in lines:
        preprocessed_tokens.extend(line.split())

    post_tokens = []
    for token in preprocessed_tokens:
        if token in KEYWORDS:
            post_tokens.append(token)
        else:
            post_tokens.extend(token)
    
    if post_tokens[0] != "program":
        print(f"REJECTED: \"program\" is expected.")
        return False

    # Main Loop
    i = 0
    while True:
        top = stack.pop()
        if top == "$" and len(post_tokens) == i:
            break
        if i not in range(len(post_tokens)):
            res = stack.pop()
            if res == "$":
                print(f"SyntaxError: \"end.\" is expected.")
            else:
                print(f"SyntaxError: \"{res}\" is expected.")
            print(f"STACK: {'|'.join(stack)}")
            return False
        token = post_tokens[i]
        if top == token:
            i += 1
            continue
        # Check if top of stack is a Terminal
        if top not in NON_TERMINALS:
            print(f"STACK: {'|'.join(stack)}")
            if top == ";" and token == ")":
                print(f"SyntaxError: \"(\" is missing.")
                return False
            print(f"SyntaxError: \"{top}\" is expected.")
            return False
        # Check if top of Stack is Non-Terminal
        if token not in TERMINALS:
            print(f"STACK: {'|'.join(stack)}")
            print(f"SyntaxError: Unexpected Token: \"{token}\".")
            for word in KEYWORDS:
                if word.startswith(token):
                    print(f"SyntaxError: \"{word}\" is expected.")
                    return
            return False
        # Get Parsing Table Output
        val = PARSING_TABLE[NON_TERMINALS.index(top)][TERMINALS.index(token)]
        if val == "":
            if top == "V":
                print(f"SyntaxError: \"integer\" is missing.")
                return False
            print(f"STACK: {'|'.join(stack)}")
            # Pop the stack until the first non-terminal
            while stack[-1] not in TERMINALS:
                stack.pop()
            print(f"SyntaxError: \"{stack[-1]}\" is missing.")
            return False
        elif val == "lambda":
            continue
        to_push = val.split()
        for state in reversed(to_push):
            stack.append(state)
    return True


if __name__ == "__main__":
    print("Syntax-only mode enabled")
    file_contents = compiler_io.read_lines("finalp2.txt")
    print("Checking syntax...")
    if check_syntax(file_contents):
        print("Syntax check passed.")
    else:
        print("Syntax check failed.")
