import time, os
start = time.perf_counter()
os.system('cls')
from colorama import Fore
import threading,requests,requests,keyboard,random,ctypes

class GenNitroCode():
    def __init__(self):
        self.nitroCode = ''
        char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for i in range(16):
            self.nitroCode = self.nitroCode + random.choice(char)

def breakedFunction(testedCodes):
    print(f'{Fore.MAGENTA}Le program va s\'arreter dans 3 secondes...')
    with open('testedCodes.txt', 'r+', encoding="utf8") as file:
        count = file.read()
        newCount = int(count) + testedCodes
        file.close()

    with open('testedCodes.txt', 'w', encoding="utf8") as file:
        file.write(str(newCount))
        file.close()
    time.sleep(3)
    exit()

def getProxies():
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.replace('\r', '')
        if proxy:
            proxies.append(proxy)
    return proxies

def testNitroCodes():
    breaked=False
    testedCodes = 0
    for i in range(3):
        ProxyList = getProxies()
        finded = False
        for proxy in ProxyList:
            ProxyParameters ={'http://': proxy,'https://': proxy}
            for i in range(3):
                if keyboard.is_pressed('alt'):
                    breaked = True
                    break
                nitrocode = GenNitroCode()
                url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitrocode.nitroCode}", proxies=ProxyParameters, timeout=5)
                if url.status_code == 200:
                    print(f"{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}] {Fore.GREEN}INVALID CODE{Fore.WHITE} : https://discord.gift/{nitrocode.nitroCode}")
                    finded = True
                    break
                print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED}INVALID CODE{Fore.WHITE} : https://discord.gift/{nitrocode.nitroCode}")
                testedCodes += 1
            if finded == True:
                break
            elif breaked == True:
                break
        if breaked == True:
            breakedFunction(testedCodes)
    with open('testedCodes.txt', 'r+', encoding="utf8") as file:
        count = file.read()
        newCount = int(count) + testedCodes
        file.close()

    with open('testedCodes.txt', 'w', encoding="utf8") as file:
        file.write(str(newCount))
        file.close()
    testNitroCodes()

def main(start):
    ctypes.windll.kernel32.SetConsoleTitleA("Nitro generator")
    print(f"""{Fore.MAGENTA}
    _   ________________  ____     _____________   __
   / | / /  _/_  __/ __ \/ __ \   / ____/ ____/ | / /
  /  |/ // /  / / / /_/ / / / /  / / __/ __/ /  |/ / 
 / /|  // /  / / / _, _/ /_/ /  / /_/ / /___/ /|  /  
/_/ |_/___/ /_/ /_/ |_|\____/   \____/_____/_/ |_/   
                                                     
    """)
    finished = time.perf_counter()
    timeToLoad = finished-start
    print(f"PROGRAM CHARGÉ EN {timeToLoad}s...\n")
    print("[ Threads : 1 - 100 | à partir de 20 attention cpu ]\n")
    try:
        threads = int(input('Threads => '))
        if threads <= 100:
            for i in range(threads):
                thread = threading.Thread(target=testNitroCodes)
                thread.start()
        else:
            print(f'{Fore.RED}[!] Ta demande est invalide !')
            time.sleep(1)
            os.system('cls')
            main(start)
    except ValueError:
        os.system('cls')
        main(start)

main(start)
