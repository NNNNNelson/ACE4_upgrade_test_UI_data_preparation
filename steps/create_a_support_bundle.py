'''
Create a Management Server support bundle
'''

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

Support_bundle_description = 'This is a test support bundle'

# Create a Management Server support bundle
def create_a_management_server_support_bundle(driver, wait, FMS_server_ip):
    # Go to "Support Bundles" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_setupsupport_supportbundles.supportDashboard')

    # Create a Management Server support bundle
    # Click the "Create Management Server Support Bundle" link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Create Management Server Support Bundle"]')))
    elem.click()
    # In the new prompt "Create Management Server Support Bundle" popup, for "Description:" textarea, enter Support_bundle_description value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Description:"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Support_bundle_description)
    # Click the "OK" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//button[@type="submit"][text()="OK"]')))
    elem.click()