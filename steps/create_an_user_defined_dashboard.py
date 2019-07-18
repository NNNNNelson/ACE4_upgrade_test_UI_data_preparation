'''
Create an user defined dashboard
    Dashboard name: "Test user defined dashboard"
    Use template of "Current Alarms" -> "Universal" -> "Alarm List Summary"
'''

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


User_defined_dashboard_name = 'Test user defined dashboard'

# Create an user defined dashboard
def create_an_user_defined_dashboard(driver, wait, FMS_server_ip):
    # Click the "Create dashboard…" link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//li[text()="Create dashboard…"]')))
    elem.click()
    # In the new prompt "Create Dashboard" popup, keep the default choice "Use All Data", directly click the "» Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@name="next"][@value="» Next"]')))
    elem.click()
    # In the "View Properties" step, for the "Name" input, enter "User_defined_dashboard_name" value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="View Properties"]//following::label[text()="Name"]/following::input[1]')))
    elem.clear()
    elem.send_keys(User_defined_dashboard_name)
    # Click the "» Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="View Properties"]//following::input[@type="button"][@name="next"][@value="» Next"]')))
    elem.click()
    # In the "Select Dashboard Layout" step, keep the default choice "Two-Column Layout", directly click the "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Select Dashboard Layout"]//following::input[@type="button"][@name="finish"][@value="Finish"]')))
    elem.click()
    # In the new prompt "Add View" popup, expand the "Alarms" node
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//td[text()="Alarms"]/preceding::img[contains(@src, "expand")][1]')))
    elem.click()
    # Click to choose the "Current Alarms" row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//td[contains(text(), "Current Alarms")]')))
    elem.click()
    # Click the "» Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Add a Dashboard View Element"]/following::input[@type="button"][@name="next"][@value="» Next"]')))
    elem.click()
    # In the "Select a Template" step, expand the "Universal" node
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Select a Template"]/following::td[text()="Universal"]/preceding::img[contains(@src, "expand")][1]')))
    elem.click()
    # Click to choose the "Alarm List Summary" node
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Select a Template"]/following::td[text()="Alarm List Summary"]')))
    elem.click()
    # Click the "» Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Select a Template"]/following::input[@type="button"][@name="next"][@value="» Next"]')))
    elem.click()
    # In the "Filter List" step, click the "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Filter List"]//following::input[@type="button"][@name="finish"][@value="Finish"]')))
    elem.click()