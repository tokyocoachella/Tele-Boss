#!/bin/env python3
# code by : Coachella

"""

you can re run setup.py 
if you have added some wrong value

"""
import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
{re} _____       _             ___                    
{re}(_   _)     (_ )          (  _ \                  
{re}  | |    __  | |   __     | (_) )  _    ___  ___ 
{re}  | |  / __ \| | / __ \   |  _ ( / _ \/  __)  __) 
{re}  | | (  ___/| |(  ___/   | (_) ) (_) )__  \__  \ 
{re}  (_)  \____)___)\____)   (____/ \___/(____/____/ 

        Modified By Coachella
        Version : 007
{re}Make sure you Subscribed To 🔥 Hustlers Ground 🔥 on Telegram For More Updates.")
   {cy}https://t.me/+7EjHzPDkInMyY2Ux
        """)
        
        
banner()


print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] enter api ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] enter hash ID : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] enter phone number : "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] setup complete !")
print(gr+"[+] now you can run any tool !")
print(gr+"[+] make sure to read docs 4 installation & api setup")
print(gr+"[+] https://github.com/termuxprofessor/TeleGram-Scraper-Adder/blob/master/README.md")
