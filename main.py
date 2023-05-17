from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait


PROMISED_DOWN=50
PROMISED_UP=25

ACTUAL_DOWN=0
ACTUAL_UP=0

USER_NAME="".join("tester_tests12")
PASSWORD="".join(os.environ["PASSWORD"])


chrome_driver_path="C:\Development\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
def getInternetSpeed():
    global ACTUAL_DOWN,ACTUAL_UP
    driver.get("https://www.speedtest.net/")
    go_button=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
    go_button.click()
   
    time.sleep(45)

    ACTUAL_DOWN=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
    ACTUAL_DOWN=float(ACTUAL_DOWN)

    ACTUAL_UP=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    ACTUAL_UP=float(ACTUAL_UP)

    if ACTUAL_UP<PROMISED_UP or ACTUAL_DOWN<PROMISED_DOWN:
        tweet()


def tweet():    
    

    driver.get("https://twitter.com/i/flow/signup")

    login_button=driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[7]/span[2]/span/span')
    login_button.click()

    time.sleep(2)

    username=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username.send_keys(USER_NAME)

    next_button=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
    next_button.click()

    time.sleep(1)

    password=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(PASSWORD)

    time.sleep(1)

    login_button=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
    login_button.click()

    time.sleep(3)
    autotw1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
    autotw1.click()

    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
    ActionChains(driver).move_to_element(element).send_keys(f"Hey! Airtel you claim to provide {PROMISED_UP}up/{PROMISED_DOWN}down but am only getting {ACTUAL_UP}up/{ACTUAL_DOWN}down ").perform()

    sendTw = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button"]/div/span/span')))
    sendTw.click()

    tweet_button=driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
    tweet_button.click()
getInternetSpeed()