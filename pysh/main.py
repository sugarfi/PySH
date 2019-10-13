import lexer
import run
import sys
import var
import getpass
COMMAND = 'command'
UNKNOWN = 'unknown'
print('PySh')
try:
    while True:
        try:
            code = input(getpass.getuser() + '@' + var.CD_NAME + ' $ ')
            if code == 'exit':
                break
            lexed = lexer.lex(code)
            code_type = lexer.code_type(lexed)
            if code_type == COMMAND:
                run.run_command(lexed)
            elif code_type == UNKNOWN:
                print('bash: error: unknown command "{}"'.format(lexed[0]), file=sys.stderr)
        except:
            print('bash: error')
except KeyboardInterrupt:
    pass
print('exit')
