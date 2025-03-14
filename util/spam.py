import requests
import os
from colorama import Fore
import pystyle
os.system("cls")

w = Fore.WHITE
r = Fore.RED
b = Fore.LIGHTBLACK_EX
g = Fore.LIGHTGREEN_EX
c = Fore.CYAN
m = Fore.LIGHTMAGENTA_EX
ll = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
fr = Fore.RESET

print(Fore.RED + """

                                 ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄     ▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
                                █  ▄    █  █ █  █   █   █   █   █       █       █
                                █ █▄█   █  █ █  █   █   █   █   █    ▄▄▄█▄     ▄█
                                █       █  █▄█  █   █   █   █   █   █▄▄▄  █   █  
                                █  ▄   ██       █   █▄▄▄█   █▄▄▄█    ▄▄▄█ █   █  
                                █ █▄█   █       █       █       █   █▄▄▄  █   █  
                                █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█  


""")

hook = input(f"{lr} Webhook To Spam > {b} ")
msg = input(f"{lr} Message To send > {b} ")
amount = int(input(f"{lr}How many times do you want to spam? {b} "))

for i in range(amount):
    requests.post(hook, data={"content": f"{msg}"})
    print(f"{b} Message Sent [{msg}]")

input(f"{lr} Press [{b}ENTER{b}] to continue : ")  