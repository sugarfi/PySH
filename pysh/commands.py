import var
def echo(*text):
    out = ''
    for word in text:
        if word == '>' or word == '>>':
            break
        out += word
        out += ' '
    if '>' not in text and '>>' not in text:
        print(out)
    else:
        path = var.CD
        if '>' in text:
            for item in path:
                if type(item) == list:
                    if item[0] == text[text.index('>') + 1]:
                        file = item
            file[1] = out
        elif '>>' in text:
            for item in path:
                if type(item) == list:
                    if item[0] == text[text.index('>>') + 1]:
                        file = item
            file[1] += out
def cd(*to):
    to = to[0]
    if to in list(var.DIR.keys()):
        var.CD_NAME = to
    elif to in var.CD:
        var.CD_NAME = var.CD_NAME.rstrip('/') + '/' + to
    else:
        print('bash: error: no such file or directory {}'.format(to))
    var.CD = var.DIR[var.CD_NAME]
def ls():
    for file in var.CD:
        if type(file) == list:
            print(file[0])
        else:
            print(file)
def dir():
    ls()
def vdir():
    ls() 
def pwd():
    print(var.CD_NAME)
def mkdir(*name):
    name = name[0]
    var.DIR[var.CD_NAME].append(name)
    var.DIR[name] = ''
def touch(*name):
    name = name[0]
    var.DIR[var.CD_NAME].append([name, ''])
def cat(*name):
    name = name[0]
    path = var.DIR[var.CD_NAME]
    for file in path:
        if type(file) == list:
            if file[0] == name:
                print(file[1])
                return
    print('bash: error: no such file or directory {}'.format(name))


