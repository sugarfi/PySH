import getpass
DIR = {
    '/':['home'],
    '/home':[getpass.getuser()],
    '/home/' + getpass.getuser():['Desktop', 'Downloads'],
    '/home/' + getpass.getuser() + '/Desktop':[],
    '/home/' + getpass.getuser() + '/Downloads':[],
}
CD_NAME = '/'
CD = DIR[CD_NAME]