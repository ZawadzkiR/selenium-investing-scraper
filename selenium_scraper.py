from selenium import webdriver
import pyautogui
import random
import getpass
import os
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import pickle



driver = webdriver.Chrome(executable_path='C:\\selenium\\chromedriver.exe')

all_list=[]
for x in range(1,210):
    
    path= 'https://www.investing.com/equities/gamestop-corp-news/{}'.format(x)
    driver.get(path)
    time.sleep(5)
    head = driver.find_elements_by_xpath('/html/body/div[5]/section/div[8]/article/div[1]/a')
    date = driver.find_elements_by_xpath('/html/body/div[5]/section/div[8]/article/div[1]/span/span[2]')
    p = driver.find_elements_by_xpath('/html/body/div[5]/section/div[8]/article/div[1]/p')


    h_list = []
    d_list = []
    p_list = []

    for h in head:
        h_list.append(h.text)

    for d in date:
        d_list.append(d.text)

    for p_ in p:
        p_list.append(p_.text)

    for o1,o2,o3 in zip(h_list, d_list, p_list):
        all_list.append([o1,o2,o3, x])
        
                
driver.quit()
df = pd.DataFrame(all_list, columns=['Header', 'Date', 'Desc', 'page'])
df.to_csv('gme.csv')
