import commands
def run_command(lexed):
    if lexed[0] in dir(commands):
        command = eval('commands.' + lexed[0])
        return command(*lexed[1:])