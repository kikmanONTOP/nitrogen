import requests
import time
import random
import string
from colorama import init, Fore


print(Fore.LIGHTCYAN_EX + '''
         d8b 888                                                    
         Y8P 888                                                    
             888                                                    
88888b.  888 888888 888d888 .d88b.        .d88b.   .d88b.  88888b.  
888 "88b 888 888    888P"  d88""88b      d88P"88b d8P  Y8b 888 "88b 
888  888 888 888    888    888  888      888  888 88888888 888  888 
888  888 888 Y88b.  888    Y88..88P      Y88b 888 Y8b.     888  888 
888  888 888  "Y888 888     "Y88P"        "Y88888  "Y8888  888  888 
                                              888                   
                                         Y8b d88P                   
                                          "Y88P"                    ''')


def generate_gift_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(16))
    gift_code = f"https://discord.gift/{code}"
    return gift_code

def send_gift(webhook_url, gift_code):
    data = {
        "content": gift_code
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print(Fore.LIGHTGREEN_EX + f"Gift code sent: {gift_code}")
    else:
        print(Fore.RED + f"Failed to send gift code. Status code: {response.status_code}")

def main():
    webhook_url = input(Fore.LIGHTMAGENTA_EX + "Enter the webhook URL: ")

    while True:
        gift_code = generate_gift_code()
        send_gift(webhook_url, gift_code)
        time.sleep(0)

if __name__ == "__main__":
    main()