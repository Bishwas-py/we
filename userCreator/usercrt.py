from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import os
from address import add, Pre, Mid, Last, Fname
numberList = [111,222,333,444,555]
random.choice(numberList)
times = int(input("Nums of Users: "))
driver = webdriver.Chrome(executable_path='userCreator/chromedriver.exe')
for i in range(times):
    driver.get('http://127.0.0.1:8000/')
    randPre = random.choice(Pre)
    randMid = random.choice(Mid)
    randLast = random.choice(Last)
    randFname = random.choice(Fname)
    randAddr = random.choice(add)
    randDate = f'{random.choice(list(range(1, 12)))}/{random.choice(list(range(1, 30)))}/{random.choice(list(range(1900, 2030)))}'
    randNumstd = random.choice(list(range(91, 1000)))
    randSchool = f'{randPre} {randMid} {randLast}'
    website = f'{randLast}.com'.replace(' ','').lower()
    randEmail = f'{randPre}{randMid}{randLast}@{website}'.replace(' ','').lower() 
    randPrincipal = f'{randLast} {randFname}'
    username = f'{randLast}{randPre}'.replace(' ','').lower()+ str(random.choice(list(range(0, 555))))
    password = '777@Bhandari'
    List = [randSchool,randEmail,randPrincipal, randAddr, randDate,randNumstd, website, username, password]
    for i in range(len(List)):
        driver.implicitly_wait(1000)
        driver.find_element_by_xpath(f'/html/body/div[2]/div/div/div[2]/form/div[{i+1}]/input').send_keys(List[i])
        if i+1 == 9:
            driver.find_element_by_xpath(f'/html/body/div[2]/div/div/div[2]/form/div[9]/input').send_keys(Keys.RETURN)
            time.sleep(5)
            driver.get('http://127.0.0.1:8000/logout')

quit()