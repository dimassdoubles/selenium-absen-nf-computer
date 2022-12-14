from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from bot_tele import send_message

LINKABSEN = "https://tinyurl.com/presensi-ma-desember-siang"

PAGE1PICKKELOMPOK = '//*[@id="i5"]/div[3]/div'
PAGE1NEXTBUTTON = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span'

PAGE2OPENSELECTION = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]'
PAGE2PICKNAME = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[10]/span'
PAGE2NEXTBUTTON = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'

PAGE3PICKHADIR = '//*[@id="i5"]/div[3]/div'
PAGE3SENDBUTTON = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'

SLEEP = 2

try :
    options  = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('headless')
    options.add_argument('start-maximized')
    browser = webdriver.Chrome("chromedriver", options=options)
    
    browser.get(LINKABSEN)
    sleep(SLEEP)

    kelompok_radio = browser.find_element(By.XPATH, PAGE1PICKKELOMPOK)
    kelompok_radio.click()
    sleep(SLEEP)

    next_button1 = browser.find_element(By.XPATH, PAGE1NEXTBUTTON)
    next_button1.click()
    sleep(SLEEP)

    open_seleksi = browser.find_element(By.XPATH, PAGE2OPENSELECTION)
    open_seleksi.click()
    sleep(SLEEP)

    seleksi_nama = browser.find_element(By.XPATH, PAGE2PICKNAME)
    seleksi_nama.click()
    sleep(SLEEP)

    next_button2 = browser.find_element(By.XPATH, PAGE2NEXTBUTTON)
    next_button2.click()
    sleep(SLEEP)

    hadir_radio = browser.find_element(By.XPATH, PAGE3PICKHADIR)
    hadir_radio.click()
    sleep(SLEEP)

    send_button = browser.find_element(By.XPATH, PAGE3SENDBUTTON)
    send_button.click()
    sleep(SLEEP)

    browser.close()

    send_message("Absen siang sukses")
    with open("history.txt", "a") as file:
        file.write("\n[" + str(datetime.now()) + "] berhasil")
except:

    send_message("Absen siang gagal")
    with open("history.txt", "a") as file:
        file.write("\n[" + str(datetime.now()) + "] gagal")
