#!/coding by Mahin Hasan
#---------------[ IMPORT-MODULE ]---------------#
import requests
import os
from bs4 import BeautifulSoup

session = requests.Session()
#---------------[ APP CHECKING DEF ]---------------#
def fb_app(session):
	os.system('clear')
	coki = input('\033[1;33m[\033[1;32m>\033[1;33m]\033[1;37m Enter Cookie \033[1;31m>\033[1;32m ')
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(50*'\033[1;31m-')
		print(f"\r\033[1;33m[\033[1;31m!\033[1;33m]\033[1;31m SORRY THERE IS NO ACTIVE APK")
	else:
		print(50*"\033[1;31m-")
		print(f'\r\033[1;33m[🔥\033[1;33m]\033[1;32m YOUR ACTIVE APPLICATION DETAILS ')
		print(40*'\033[1;31m-')
		for i in range(len(game)):
			print("\033[1;33m[\033[1;32m%s\033[1;33m]\033[1;32m %s\x1b[0m"%(i+1,game[i].replace("ACTIVE"," ACTIVE")))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(50*'\033[1;31m-')
		print(f"\r\033[1;33m[\033[1;31m!\033[1;33m]\033[1;31m SORRY THERE IS NO EXPIRED APK")
	else:
		print(50*'\033[1;31m-')
		print(f'\r\033[1;33m[\033[1;31m🔥\033[1;33m]\033[1;32m YOUR EXPIRED APPLICATION DETAILS ')
		print(40*'\033[1;31m-')
		for i in range(len(game)):
			print("\033[1;33m[\033[1;32m%s\033[1;33m]\033[1;32m %s\x1b[0m"%(i+1,game[i].replace("Expired"," Expired")))

#---------------[ END ]---------------#
fb_app(session)