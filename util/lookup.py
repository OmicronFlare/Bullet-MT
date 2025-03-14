import colorama
import pystyle
from colorama import Fore,Style
token = input(Fore.LIGHTBLACK_EX + "Token > " + Fore.RESET)
import requests

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

headers = {
    'Authorization': token
}

def get_user_info():
    response = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    response.raise_for_status()

    user_info = response.json()
    has_phone = 'phone' in user_info and user_info['phone'] is not None
    phone_number = user_info['phone'] if has_phone else 'None'
    email = user_info['email'] if 'email' in user_info else 'None'

    return has_phone, phone_number, email

def has_credit_card():
    response = requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers)
    response.raise_for_status()

    payment_sources = response.json()
    return len(payment_sources) > 0

def get_nitro_info():
    response = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
    response.raise_for_status()

    subscriptions = response.json()
    has_nitro = len(subscriptions) > 0
    nitro_type = subscriptions[0]['plan']['name'] if has_nitro else 'None'

    return has_nitro, nitro_type

phone, phone_number, email = get_user_info()
has_cc = has_credit_card()
has_nitro, nitro_type = get_nitro_info()

print(f'{lr}Phone Number: {b}{phone_number}\n{lr}Has Credit Card: {b}{has_cc}\n{lr}Email: {b}{email}\n{lr}Has Nitro: {b}{has_nitro}\n{lr}Nitro Type: {b}{nitro_type}')
input()