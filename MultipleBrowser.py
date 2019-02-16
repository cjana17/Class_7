from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https:facebook.com')
driver.maximize_window()
driver.delete_all_cookies()