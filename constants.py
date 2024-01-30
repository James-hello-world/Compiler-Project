from enum import Enum


TOKENIZER_SYMBOLS = {
    "+",
    "-",
    "*",
    "/",
    "(",
    ")",
    ",",
    ":",
    ";",
    "=",
}


class SymbolType(Enum):
    LEFT_SPACED = 1
    RIGHT_SPACED = 2
    SIGN = 3
    CAN_PREDATE_SIGN = 4


TRANSPILER_SYMBOLS = {
    SymbolType.LEFT_SPACED: {"+", "-", "*", "/", "="},
    SymbolType.RIGHT_SPACED: {",", ":", "*", "/", "="},
    SymbolType.SIGN: {"+", "-"},
    SymbolType.CAN_PREDATE_SIGN: {"+", "-", "*", "/", ",", "="},
}


TERMINALS = [  # Ordered terminals in columns
    "program",
    "var",
    "begin",
    "end.",
    ":",
    ";",
    ",",
    "integer",
    "print",
    "(",
    ")",
    "\"value=\"",
    "=",
    "+",
    "-",
    "*",
    "/",
    "a",
    "b",
    "c",
    "d",
    "f",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

NON_TERMINALS = [  # Ordered Rows in table
    "P",
    "I",
    "X",
    "C",
    "D",
    "B",
    "V",
    "R",
    "S",
    "W",
    "G",
    "A",
    "E",
    "Q",
    "T",
    "Y",
    "F",
    "N",
    "Z",
    "O",
    "U",
    "L",
]

KEYWORDS = {  # Reserved words
    "program",
    "var",
    "begin",
    "end.",
    "integer",
    "print",
    "\"value=\"",
}

PARSING_TABLE = [
    ["program I ; var C begin R end.", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "L X", "L X", "L X", "L X", "L X", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "lambda", "lambda", "lambda", "", "", "", "lambda", "", "lambda", "lambda", "lambda", "lambda", "lambda", "L X", "L X", "L X", "L X", "L X", "U X", "U X", "U X", "U X", "U X", "U X", "U X", "U X", "U X", "U X"],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "D : V ;", "D : V ;", "D : V ;", "D : V ;", "D : V ;", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "I B", "I B", "I B", "I B", "I B", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "lambda", "", ", D", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "integer", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "lambda", "", "", "", "", "S R", "", "", "", "", "", "", "", "", "S R", "S R", "S R", "S R", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "W", "", "", "", "", "", "", "", "", "A", "A", "A", "A", "A", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "print ( G I ) ;", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "\"value=\" ,", "", "", "", "", "", "lambda", "lambda", "lambda", "lambda", "lambda", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "I = E ;", "I = E ;", "I = E ;", "I = E ;", "I = E ;" "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "T Q", "", "", "", "T Q", "T Q", "", "", "T Q", "T Q", "T Q", "T Q", "T Q", "T Q", "T Q", "T Q", "T Q", "T Q", "T Q", "T Q", "T Q", "T Q", "T Q"],
    ["", "", "", "", "", "lambda", "", "", "", "", "lambda", "", "", "+ T Q", "- T Q", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "F Y", "", "", "", "F Y", "F Y", "", "", "F Y", "F Y", "F Y", "F Y", "F Y", "F Y", "F Y", "F Y", "F Y", "F Y", "F Y", "F Y", "F Y", "F Y", "F Y"],
    ["", "", "", "", "", "lambda", "", "", "", "", "lambda", "", "", "lambda", "lambda", "* F Y", "/ F Y", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "( E )", "", "", "", "N", "N", "", "", "I", "I", "I", "I", "I", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "O U Z", " O U Z", "", "", "", "", "", "", "", "U Z", "U Z", "U Z", "U Z", "U Z", "U Z", "U Z", "U Z", "U Z", "U Z"],
    ["", "", "", "", "", "lambda", "", "", "", "", "lambda", "", "", "lambda", "lambda", "lambda", "lambda", "", "", "", "", "", "U Z", "U Z", "U Z", "U Z", "U Z", "U Z", "U Z", "U Z", "U Z", "U Z"],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "+", "-", "", "", "", "", "", "", "", "lambda", "lambda", "lambda", "lambda", "lambda", "lambda", "lambda", "lambda", "lambda", "lambda"],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "a", "b", "c", "d", "f", "", "", "", "", "", "", "", "", "", ""],
]
