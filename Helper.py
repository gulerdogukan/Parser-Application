from Tokens import reserved_words, operators


# This function is used to print a welcoming statement and a brief description about the program.
def introduction():
    print("\t\t\t\t\t\t ## Welcome to Lexical Analyzer and Parser Application ##")


# This function is checking if the input token is identifier or not.
# By checking if the first character of the token is alphabet or "_", then it is identifier, but the token
# should not be one of the reserved words or starting with numbers.
def is_identifier(input_token):
    if reserved_words.count(input_token) > 0:
        return False
    elif input_token[0].isalpha() or input_token[0] == "_":
        return True
    else:
        return False


# This function is checking if the input token is one of the stored reserved words or not.
# The reserved words we support are "for", "while", "if", and "else".
def is_reserved_word(input_token):
    return bool(reserved_words.count(input_token))


# This function is checking if the input token is one of the stored operators or not.
# The operators we support are "&", "&&", "|", and "||".
def is_operator(input_token):
    return bool(operators.count(input_token))


def is_integer(num):
    try:
        float(num)
    except ValueError:
        return False
    else:
        return float(num).is_integer()


def is_float(num):
    try:
        int_num = int(num)
    except ValueError:
        try:
            float_num = float(num)
        except ValueError:
            return False
        else:
            return True
    else:
        return False


# This function is used to exit from the program.
def end_the_program():
    exit()
