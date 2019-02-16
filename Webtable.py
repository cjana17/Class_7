from selenium import webdriver

driver=webdriver.Chrome()
driver.get("C:/Users/Janardhanan/Desktop/Selenium/Webtable.html")
driver.maximize_window()
driver.implicitly_wait(15)

#ele = driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")
#ele = driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr[1]/td")
ele = driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr[1]/td")
print(len(ele))

first_part="//*[@id='emp']/thead/tr/th["
second_part="]"