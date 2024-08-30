import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

dpt_city = 'SHH'
arv_city = 'WHN'
date = '2024-09-05'
seat = 'F'
train_num = 2
num = (train_num - 1) * 2 + 1

def buy_ticket(dpt, arv, train_time, seat_num, train_no):

    # 打开浏览器
    driver = webdriver.Chrome()
    url = 'https://kyfw.12306.cn/otn/resources/login.html'
    driver.get(url)

    # 输入账号密码
    # 定位文本框
    driver.find_element(By.ID, 'J-userName').send_keys('input('请输入账号：')')
    driver.find_element(By.ID, 'J-password').send_keys(input('请输入密码：'))
    driver.find_element(By.ID, 'J-login').click()
    time.sleep(0.5)
    driver.find_element(By.ID, 'id_card').send_keys('6511')
    driver.find_element(By.ID, 'verification_code').click()
    driver.find_element(By.ID, 'code').send_keys(input('请输入验证码：'))
    driver.find_element(By.ID, 'sureClick').click()
    # input('扫码完成：')
    time.sleep(1)
    driver.find_element(By.ID, 'link_for_ticket').click()
    time.sleep(1)
    driver.find_element(By.ID, 'fromStationText').click()
    driver.find_element(By.ID, 'fromStationText').send_keys(dpt)
    driver.find_element(By.ID, 'fromStationText').send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'toStationText').click()
    driver.find_element(By.ID, 'toStationText').send_keys(arv)
    driver.find_element(By.ID, 'toStationText').send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'train_date').click()
    driver.find_element(By.ID, 'train_date').clear()
    driver.find_element(By.ID, 'train_date').send_keys(train_time)
    driver.find_element(By.ID, 'train_date').send_keys(Keys.ENTER)
    driver.find_element(By.ID,'query_ticket').click()
    time.sleep(1)
    driver.find_element(By.XPATH, f'//tbody[@id = \'queryLeftTable\']/tr[{train_no}]/td[13]/a').click()
    time.sleep(1)
    driver.find_element(By.ID, 'normalPassenger_0').click()
    driver.find_element(By.ID, 'submitOrder_id').click()
    driver.find_element(By.XPATH, f'//div[@id = \'erdeng1\']/ul/li/a[@id = \'1{seat_num}\']').click()
    # 确认支付
    input('确认下单：')
    driver.find_element(By.ID, 'qr_submit_id').click()
    time.sleep(10)
    driver.find_element(By.ID, 'payButton').click()
    time.sleep(100)

