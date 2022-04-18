from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
EMAIL = 'YOUR_EMAILL'
PASSWORD= 'YOUR_PASSWORD'
chrome_driver_path = "C:\\Users\\Hp EliteBook\\Desktop\\chrome Driver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com")
main_page = driver.current_window_handle
log_in_button = driver.find_element_by_xpath('//*[@id="s-522567612"]/div/div[1]/div/main/div[1]/div/div/div/div/header/'
                                             'div/div[2]/div[2]/a/span')
log_in_button.click()
time.sleep(3)
facebook_path_login= driver.find_element_by_xpath('//*[@id="s2044018608"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
facebook_path_login.click()
time.sleep(3)

for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle
        driver.switch_to.window(login_page)

email= driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys(EMAIL)
time.sleep(3)
password= driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(PASSWORD)
time.sleep(10)
# login_tinder = driver.find_element_by_xpath('//*[@id="u_0_0_nc"]')
# login_tinder.click()
password.send_keys(Keys.ENTER)

driver.switch_to.window(main_page)
time.sleep(15)
accept_loc_button = driver.find_element_by_xpath('//*[@id="s-522567612"]/div/div[2]/div/div/div[1]/div[1]/button/span')
accept_loc_button.click()

location_button = driver.find_element_by_xpath('//*[@id="s2044018608"]/div/div/div/div/div[3]/button[1]')
location_button.click()

time.sleep(15)
enable_button= driver.find_element_by_xpath('//*[@id="s2044018608"]/div/div/div/div/div[3]/button[1]/span')
enable_button.click()
time.sleep(10)
actions = ActionChains(driver)
for i in range(100):
    try:
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
        time.sleep(3)
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

            # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)


driver.quit()
