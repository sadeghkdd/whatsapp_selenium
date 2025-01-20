
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from colorama import init, Fore, Style
import time
import os

driver_path = 'Your address driverweb'
service = Service(driver_path)
browser = webdriver.Chrome(service=service)
browser.get('https://web.whatsapp.com/')

input("In\nRUN??\n\n")
init()
os.system('cls')

while True:
    Message = input(Fore.LIGHTCYAN_EX + 'Enter a message: ' + Fore.WHITE)
    if Message.lower() == 'exit':
        break
    time.sleep(0.3)
    Names = input(Fore.LIGHTCYAN_EX + 'Enter Names [& separated]: ' + Fore.WHITE).split('&')
    time.sleep(0.3)
    NumberRange = int(input(Fore.LIGHTCYAN_EX + 'Enter Number: ' + Fore.WHITE))
    time.sleep(0.8)

    for name in Names:
        try:
            
            chat = browser.find_element(By.XPATH, f'//span[@title="{name.strip()}"]')
            chat.click()
            time.sleep(1)  

            for number in range(NumberRange):
                message_box = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                message_box.send_keys(Message + Keys.ENTER)
                time.sleep(0.3)  

            print(Fore.LIGHTGREEN_EX + '[+] - ' + Fore.RED + name.strip())
        except Exception as e:
            print(Fore.RED + f'[-] Error with {name.strip()}: {e}')

input('\nEXIT??\n\n')
browser.quit()

