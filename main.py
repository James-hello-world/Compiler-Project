import compiler_io
import tokenizer
import transpiler
import syntax


if __name__ == "__main__":
    print("Reading input...")
    file_contents = compiler_io.read_lines()

    print("Tokenizing...")
    tokenized_form = tokenizer.tokenize(file_contents)
    print("Saving tokenized output...")
    compiler_io.write_lines(tokenized_form, True)

    print("Checking syntax...")
    if not syntax.check_syntax(tokenized_form):
        print("Syntax Rejected")
        exit(1)
    print("Initial syntax checks passed.")

    print("Checking for unknown identifiers...")
    output_code = transpiler.transpile(tokenized_form)
    print("Syntax Accepted")

    print("Saving transpiled output...")
    compiler_io.write_lines(output_code, False)

    print("Running generated Python code:\n")
    print("Console: ---------------------")
    compiler_io.execute_output()
    print("End of script. Terminating...")
