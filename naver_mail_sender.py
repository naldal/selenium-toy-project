from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pyperclip
import time


def clipboard_input(user_xpath, user_input):
    pyperclip.copy(user_input)
    driver.find_element_by_xpath(user_xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)


driver = webdriver.Chrome()
url = 'https://naver.com'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

## Naver login

naver_account = {
    "id": "cec7777",
    "pwd": "-"
}

# goto login section
driver.find_element_by_xpath('//*[@id="account"]/a').click()

driver.execute_script("document.getElementsByName('id')[0].value=\'" + naver_account.get("id") + "\'")

driver.execute_script("document.getElementsByName('pw')[0].value=\'" + naver_account.get("pwd") + "\'")
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/fieldset/span[2]/a').click()
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[1]/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/a[1]').click()
time.sleep(2)


# 메일쓰기
def mail_sender_function(receiver, title, content):
    driver.find_element_by_xpath('//*[@id="toInput"]').send_keys(receiver)
    driver.find_element_by_xpath('//*[@id="subject"]').send_keys(title)
    driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="se2_iframe"]'))
    elem = driver.find_element_by_xpath('/html/body')
    elem.send_keys(content)
    driver.switch_to_default_content()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sendBtn"]').click()
    time.sleep(1)


mail_sender_function("antibody91@naver.com", "제목입니다", "호호이")


