from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

LINKABSEN = "https://bit.ly/absensi-mobile-oktober-pagi"

XPATHPAGE1PICKKELOMPOK = '//*[@id="i5"]/div[3]/div'
XPATHPAGE1NEXTBUTTON = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span'

XPATHPAGE2OPENSELECTION = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]'
XPATHPAGE2PICKNAME = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[10]/span'
XPATHPAGE2NEXTBUTTON = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'

XPATHPAGE3PICKHADIR = '//*[@id="i5"]/div[3]/div'
XPATHPAGE3SENDBUTTON = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'

SLEEP = 2

try :
    options  = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('start-maximized')
    browser = webdriver.Chrome("chromedriver", options=options)
    browser.get(LINKABSEN)
    sleep(SLEEP)

    kelompok_radio = browser.find_element(By.XPATH, XPATHPAGE1PICKKELOMPOK)
    kelompok_radio.click()
    sleep(SLEEP)

    next_button1 = browser.find_element(By.XPATH, XPATHPAGE1NEXTBUTTON)
    next_button1.click()
    sleep(SLEEP)

    open_seleksi = browser.find_element(By.XPATH, XPATHPAGE2OPENSELECTION)
    open_seleksi.click()
    sleep(SLEEP)

    seleksi_nama = browser.find_element(By.XPATH, XPATHPAGE2PICKNAME)
    seleksi_nama.click()
    sleep(SLEEP)

    next_button2 = browser.find_element(By.XPATH, XPATHPAGE2NEXTBUTTON)
    next_button2.click()
    sleep(SLEEP)

    hadir_radio = browser.find_element(By.XPATH, XPATHPAGE3PICKHADIR)
    hadir_radio.click()
    sleep(SLEEP)

    send_button = browser.find_element(By.XPATH, XPATHPAGE3SENDBUTTON)
    send_button.click()
    sleep(SLEEP)

    browser.close()

    with open("history.txt", "a") as file:
        file.write("\n[" + str(datetime.now()) + "] berhasil")
except:

    with open("history.txt", "a") as file:
        file.write("\n[" + str(datetime.now()) + "] gagal")
