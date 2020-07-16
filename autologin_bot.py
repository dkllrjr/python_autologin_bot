from mechanize import Browser
from http.cookiejar import CookieJar
from subprocess import call
from time import sleep
from sys import argv

# functions defined here

# ping uses the shell command "ping" to ping the given hostname
def ping(hostname,params):
    
    command = ['ping'] + params + [hostname]

    return call(command) == 0

# extract_credentials extracts the credentials in the given password_file into a dictionary containing the url,login, and password
def extract_credentials(password_file):

    with open(password_file) as file:
        text = file.readlines()

    credentials = {}
    for line in text:
        words = line.split()

        if words[0] == 'url:':
            credentials['url'] = words[1]        
        elif words[0] == 'login:':
            credentials['login'] = words[1]
        elif words[0] == 'password:':
            credentials['password'] = words[1]

    return credentials

# login takes the credentials dictionary built by extract_credentials and performs the login 
def login(credentials):

    try:
        cj = CookieJar()
        br = Browser()
        br.set_cookiejar(cj)
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.open(credentials['url'])

        # entering login
        br.select_form(nr=0)
        br.form['login'] = credentials['login']
        br.form['password'] = credentials['password']
        br.submit()

        # confirming again if there is a redirect
        br.open(br.response().geturl())
        br.select_form(nr=0)
        br.submit()
        
        print('logged in')

    except:
        print('failed login, retrying after delay period') 

# starting the process

# giving the login file via command line "python autologin_bot.py credential_file.txt"
credential_file = argv[1]

# if the desired delay is given in the command line (must be after the credential_file.txt), this reads it in, otherwise the pause between internet pings is 5 min
if len(argv) < 3:
    delay = 300
else:
    delay = int(argv[2])

credentials = extract_credentials(credential_file)

# the actual process loop
while True:
    
    if ping('google.com',['-c','1']):
        print('sleeping between internet pings for: ' + str(delay) + ' seconds')
        sleep(delay)
    else:
        login(credentials)
        sleep(delay)
