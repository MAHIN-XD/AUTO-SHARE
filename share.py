import os, platform, time, sys
 
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
 
print('\033[1;91m[\033[1;97m-\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print('\033[1;93m[\033[1;92m•\033[1;93m] \033[1;97mChecking For Update ')
 print('\033[1;93m[\033[1;92m•\033[1;93m] \033[1;97mAll Done')
 import SHARE
elif bit == '32bit':
 print('\033[1;93m[\033[1;92m•\033[1;93m] \033[1;97mChecking For Update ')
 print('\033[1;93m[\033[1;92m•\033[1;93m] \033[1;97mAll Done')
 import SHARE_32
 