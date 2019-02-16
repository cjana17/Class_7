import time
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://phptravels.com')
browser.maximize_window()
browser.implicitly_wait(30)

#browser.delete_all_cookies()

current_window_id=browser.current_window_handle
print(current_window_id)
time.sleep(10)
browser.find_element_by_xpath("//span[text()='Login']").click()
windows_id=browser.window_handles
print(type(windows_id))
for handle in windows_id:
    print(handle)
    if handle != current_window_id:
        browser.switch_to.window(handle)
        browser.find_element_by_name("username").send_keys("Test")
#browser.close()
browser.quit()
