import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Additional_process_pool_utilization_fatal_value = '91.0'

# Modify a rule's threshold
# Modify rule "Additional Process Pool Utilization" fatal alarm threshold from "90.0" to "91.0"
def modify_a_rule_threshold(driver, wait, FMS_server_ip):
    # Go to "Rules" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_rulesnotifications_rulemanagement.ruleManagement')

    # For "Cartridge" drop-down list, verify its value is "All Cartridges", if not, change it to "All Cartridges"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Cartridge: "]/following::input[@class="dropDownField"][1]')))
    if elem.get_attribute('value') != 'All Cartridges':
        elem.click()
        elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="popupSharedDiv"][contains(@style, "visibility: visible")]/descendant::span[text()="All Cartridges"][1]')))
        elem.click()
        time.sleep(1)

    # Click the fatal alarm threshold of rule "Additional Process Pool Utilization"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Additional Process Pool Utilization"]/following::div[@column-id="fatal"][1]')))
    elem.click()
    # In the new prompt "Fatal Condition Threshold" popup, modify the "INF_AdditionalProcPoolFatal" value from "90.0" to "91.0"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="INF_AdditionalProcPoolFatal"]/following::input[@type="text"][1]')))
    elem.clear()
    elem.send_keys(Additional_process_pool_utilization_fatal_value)
    # Click the "Update" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Update"]')))
    elem.click()