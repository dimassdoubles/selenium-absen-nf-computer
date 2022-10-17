from time import sleep
from click import option
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ABSENSIANG = "https://docs.google.com/forms/d/e/1FAIpQLScPMepooE6tA2DFqltVYWaf0vuqpahvkq0014Wn-8FvyiJh8A/viewform"

XPATHPAGE1PICKKELOMPOK = '//*[@id="i5"]/div[3]/div'
XPATHPAGE1NEXTBUTTON = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span'

XPATHPAGE2OPENSELECTION = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]'
XPATHPAGE2PICKNAME = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[10]/span'
XPATHPAGE2NEXTBUTTON = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'

XPATHPAGE3PICKHADIR = '//*[@id="i5"]/div[3]/div'
XPATHPAGE3SENDBUTTON = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span'

SLEEP = 2

options  = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('start-maximized')
browser = webdriver.Chrome("chromedriver", options=options)
browser.get(ABSENSIANG)

print("Memilih kelompok 1")
kelompok_radio = browser.find_element(By.XPATH, XPATHPAGE1PICKKELOMPOK)
kelompok_radio.click()
sleep(SLEEP)

print("Ke halaman 2")
next_button1 = browser.find_element(By.XPATH, XPATHPAGE1NEXTBUTTON)
next_button1.click()
sleep(SLEEP)

print("Membuka seleksi")
open_seleksi = browser.find_element(By.XPATH, XPATHPAGE2OPENSELECTION)
open_seleksi.click()
sleep(SLEEP)

print("Memilih nama")
seleksi_nama = browser.find_element(By.XPATH, XPATHPAGE2PICKNAME)
seleksi_nama.click()
sleep(SLEEP)

print("Ke halaman 3")
next_button2 = browser.find_element(By.XPATH, XPATHPAGE2NEXTBUTTON)
next_button2.click()
sleep(SLEEP)

print("Memilih hadir")
hadir_radio = browser.find_element(By.XPATH, XPATHPAGE3PICKHADIR)
hadir_radio.click()
sleep(SLEEP)

print("Klik tombol kirim")
send_button = browser.find_element(By.XPATH, XPATHPAGE3SENDBUTTON)
send_button.click()
sleep(SLEEP)

print("Selesai")
browser.close()





