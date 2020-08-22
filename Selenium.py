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


login = {
    "id": "cec7378@gmail.com",
    "pwd": "-!"
}

driver = webdriver.Chrome()
url = 'https://github.com/'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()

# login process
clipboard_input('//*[@id="login_field"]', login.get("id"))
clipboard_input('//*[@id="password"]', login.get("pwd"))
driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()

# profile img click
driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary/img').click()
# your repository click
driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/a[2]').click()
# blog.io click
driver.find_element_by_xpath('//a[@href="/naldal/naldal.github.io"]').click()
# readme update button
driver.find_element_by_xpath('//a[@href="/naldal/naldal.github.io/edit/master/README.md"]').click()
# line 5 click
driver.find_element_by_xpath('//*[@id="new_blob"]/div[5]/div[2]/div/div[5]/div[1]/div/div/div/div[5]/div[5]/pre').send_keys(Keys.SPACE)
driver.find_element_by_xpath('//*[@id="submit-file"]').click()
driver.find_element_by_xpath('/html/body/div[4]/div/main/div[1]/div/div/h1/span[1]/a').click()



