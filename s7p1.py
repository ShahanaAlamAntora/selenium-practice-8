from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")
driver.maximize_window()
driver.get("https://www.sastaticket.pk/airlines/serene-air.aspx?gclid=EAIaIQobChMIoL2xnMj-6wIVmaiyCh0hpwCwEAAYASAAEgLEKvD_BwE")
driver.implicitly_wait(20)
driver.find_element_by_class_name("mc-closeModal").click()
driver.find_element_by_name("origin").send_keys("Karachi")
driver.find_element_by_xpath("//*[@id='body']/ul[1]/li/a").click()
time.sleep(3)
driver.find_element_by_name("destination").send_keys("Lahore")
driver.find_element_by_xpath("//*[@id='body']/ul[2]/li/a").click()
driver.find_element_by_name("fr").click()
driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[1]/td[7]/a").click()
driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[2]/table/tbody/tr[2]/td[3]/a").click()
#driver.find_element_by_xpath("//*[@id='tsb-oneway']/span").click()
driver.find_element_by_css_selector("input[value=Search]").click()
#explicitwait (Waiting for a particular element to be visible)
wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/button"))).click()
time.sleep(5)
driver.quit()