'''
Modify Service Operations Console
'''

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Modify Service Operations Console
def modify_service_operation_console(driver, wait, FMS_server_ip):
    # Go to "Service Operations Console" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:foglight_services.28')

    # Click the "Select services and tiers to monitor" link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//li[text()="Select services and tiers to monitor"]')))
    elem.click()
    # In the new prompt "Select services and tiers to monitor" popup, switch to "Tier Selector" tab
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Select services and tiers to monitor"]/following::a[text()="Tier Selector"]')))
    elem.click()
    # Uncheck the checkbox of "DB"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Select services and tiers to monitor"]/following::span[text()="DB"]/preceding::input[@type="checkbox"][1]')))
    elem.click()
    # Click the "Apply" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Select services and tiers to monitor"]/following::button[@type="submit"][text()="Apply"]')))
    elem.click()