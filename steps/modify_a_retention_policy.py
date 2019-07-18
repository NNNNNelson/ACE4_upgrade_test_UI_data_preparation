import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


After_value = '10'

# Modify a retention policy
# Modify the "Agent" -> "runningStateObservation" retention policy "5min" to "10min"
def modify_a_retention_policy(driver, wait, FMS_server_ip):
    # Go to "Manage Registry Variables" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_data.3')
    # Expand the "Agent" node (need to switch frame)
    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@src, "listRetentionPolicy")]'))))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Agent")]/preceding::img[contains(@src, "t_plus")][1]')))
    elem.click()
    # Expand the "runningStateObservation" node
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "runningStateObservation")]/preceding::img[contains(@src, "t_plus")][1]')))
    elem.click()
    # Click the "5min"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "runningStateObservation")]/following::span[contains(text(), "5min")][1]')))
    elem.click()
    # Wait for the "editRetentionPolicy" frame to be visible
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="editRetentionPolicy"][not(contains(@style, "visibility: hidden"))]')))
    # Modify the "After ..." value from '5' to '10'
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="rollValE"]')))
    elem.clear()
    elem.send_keys(After_value)
    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="editRetentionPolicy"]//input[@type="button"][@value="Save"]')))
    elem.click()