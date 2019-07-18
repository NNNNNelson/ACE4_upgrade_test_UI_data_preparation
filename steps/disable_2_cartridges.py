'''
Disable "SanHost" and "Usage-Feedback" cartridges
'''

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Cartridge_1_name = 'PythonAgentSDK'
Cartridge_2_name = 'Usage-Feedback'


# Disable 2 cartridges
def disable_2_cartridges(driver, wait, FMS_server_ip):
    # Go to "Cartridge Inventory" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_cartridges_cartridgeinventory.cartridgeInventory')

    # In the cartridge table search bar, search Cartridge_1_name value named cartridge
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="portalContents"]//input[contains(@class, "searchField")]')))
    elem.clear()
    elem.send_keys(Cartridge_1_name + Keys.ENTER)
    # Wait for the search to complete
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="portalContents"]//input[contains(@class, "searchField")]/following::img[contains(@src, "busy")][1][contains(@style, "visibility: hidden")]')))
    # Check the checkbox of Cartridge_1_name value named cartridge
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="' + Cartridge_1_name + '"]/preceding::input[@type="checkbox"][1]')))
    elem.click()
    # Click the "Disable" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Disable"]')))
    elem.click()
    # In the new prompt "Cartridge Confirmation" popup, click the "OK" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Cartridge Confirmation"]/following::button[@type="submit"][text()="OK"]')))
    elem.click()
    # In the new prompt "Operation(s) Complete" popup, click the "OK" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Operation(s) Complete"]/following::button[@type="submit"][text()="OK"]')))
    elem.click()
    # Wait for the popup to disappear
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]')))
    # In the cartridge table search bar, search Cartridge_2_name value named cartridge
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="portalContents"]//input[contains(@class, "searchField")]')))
    elem.clear()
    elem.send_keys(Cartridge_2_name + Keys.ENTER)
    # Wait for the search to complete
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="portalContents"]//input[contains(@class, "searchField")]/following::img[contains(@src, "busy")][1][contains(@style, "visibility: hidden")]')))
    # Check the checkbox of Cartridge_2_name value named cartridge
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="' + Cartridge_2_name + '"]/preceding::input[@type="checkbox"][1]')))
    elem.click()
    # Click the "Disable" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Disable"]')))
    elem.click()
    # In the new prompt "Cartridge Confirmation" popup, click the "OK" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Cartridge Confirmation"]/following::button[@type="submit"][text()="OK"]')))
    elem.click()
    # In the new prompt "Operation(s) Complete" popup, click the "OK" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Operation(s) Complete"]/following::button[@type="submit"][text()="OK"]')))
    elem.click()