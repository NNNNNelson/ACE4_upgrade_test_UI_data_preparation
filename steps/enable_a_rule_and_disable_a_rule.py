import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Rule_name_to_be_enabled = 'Run Queue Length Threshold'
Rule_name_to_be_disabled = 'Run Queue Length'

# Enable a rule, and disable a rule

# Enable a rule
def enable_a_rule(driver, wait, FMS_server_ip):
    # Go to "Rules" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_rulesnotifications_rulemanagement.ruleManagement')

    # For "Cartridge" drop-down list, verify its value is "All Cartridges", if not, change it to "All Cartridges"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Cartridge: "]/following::input[@class="dropDownField"][1]')))
    if elem.get_attribute('value') != 'All Cartridges':
        elem.click()
        elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="popupSharedDiv"][contains(@style, "visibility: visible")]/descendant::span[text()="All Cartridges"][1]')))
        elem.click()
        time.sleep(1)
    # In Rules table search bar, enter "Run Queue Length Threshold" to search
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="searchField"]')))
    elem.clear()
    elem.send_keys(Rule_name_to_be_enabled + Keys.ENTER)
    time.sleep(2)
    # Click the checkbox of rule "Run Queue Length Threshold"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Run Queue Length Threshold"]/preceding::input[@type="checkbox"][1]')))
    elem.click()
    # Click the enabled "Enable" button in the top of the rules table
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Enable"]/preceding::img[contains(@src, "true")][not(contains(@class, "disabled"))][1]')))
    elem.click()
    # In the new prompt "Enable Rules" popup, click the "Yes" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Enable Rules"]/following::button[@type="button"][text()="Yes"][1]')))
    elem.click()

# Disable a rule
def disable_a_rule(driver, wait, FMS_server_ip):
    # Go to "Rules" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_rulesnotifications_rulemanagement.ruleManagement')

    # For "Cartridge" drop-down list, verify its value is "All Cartridges", if not, change it to "All Cartridges"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Cartridge: "]/following::input[@class="dropDownField"][1]')))
    if elem.get_attribute('value') != 'All Cartridges':
        elem.click()
        elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="popupSharedDiv"][contains(@style, "visibility: visible")]/descendant::span[text()="All Cartridges"][1]')))
        elem.click()
        time.sleep(1)
    # In Rules table search bar, enter "Run Queue Length" to search
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="searchField"]')))
    elem.clear()
    elem.send_keys(Rule_name_to_be_disabled + Keys.ENTER)
    time.sleep(2)
    # Click the checkbox of rule "Run Queue Length"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Run Queue Length"]/preceding::input[@type="checkbox"][1]')))
    elem.click()
    # Click the enabled "Disable" button in the top of the rules table
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Disable"]/preceding::img[contains(@src, "false")][not(contains(@class, "disabled"))][1]')))
    elem.click()
    # In the new prompt "Disable Rules" popup, click the "Yes" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Disable Rules"]/following::button[@type="button"][text()="Yes"][1]')))
    elem.click()