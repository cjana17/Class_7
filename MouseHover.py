from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(30)

element = driver.find_element_by_xpath("//span[text()='Men']")
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()


# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# firefox = webdriver.Firefox()
# firefox.get('http://foo.bar')
# element_to_hover_over = firefox.find_element_by_id("baz")
#
# hover = ActionChains(firefox).move_to_element(element_to_hover_over)
# hover.perform()