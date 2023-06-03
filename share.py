import os, platform, time, sys
 
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
 

os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
 import SHARE
elif bit == '32bit':
 import SHARE_32
 
