import requests
import pystyle
from pystyle import *
from colorama import *
from colorama import Fore
import os
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
ly = Fore.LIGHTYELLOW_EX

print(Fore.RED + f"""

                                     ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄     ▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
                                    █  ▄    █  █ █  █   █   █   █   █       █       █
                                    █ █▄█   █  █ █  █   █   █   █   █    ▄▄▄█▄     ▄█
                                    █       █  █▄█  █   █   █   █   █   █▄▄▄  █   █  
                                    █  ▄   ██       █   █▄▄▄█   █▄▄▄█    ▄▄▄█ █   █  
                                    █ █▄█   █       █       █       █   █▄▄▄  █   █  
                                    █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█  
                                              {lr}<{b}Webhook Deleter{lr}>

""")

hook = input(f" {lr}Enter Webhook To Delete {b}> ")
msg = input(f" {lr}Enter deletion message {b}> ")
if msg == "":
    msg = "Next time obfuscate your code."

requests.post(hook, data={"content": f"{msg}"})
requests.delete(hook)

input(f"{lr} Success | Press {b}[{lr}ENTER{b}] {lr}to continue > ")