import commands
def lex(code):
    code = code.split()
    for i in range(len(code)):
        word = code[i]
        if word.isdigit():
            code[i] = int(code[i])
    return code
def code_type(lexed):
    if lexed[0] in dir(commands):
        return 'command'
    else:
        return 'unknown'

