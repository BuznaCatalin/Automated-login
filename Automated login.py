from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(options=option, executable_path='where is your chromedriver located')
driver.get('https://www.facebook.com')


id = driver.find_element_by_name("email")
psw = driver.find_element_by_name("pass")

print(id.is_displayed())
print(psw.is_displayed())

id.send_keys("your facebook email address")
psw.send_keys("your facebook password")

driver.find_element_by_xpath("//*[@id='u_0_d']").click()








