'''
Modify existed derived metric "activeAgentCount" description from empty to "test modify a derived metric
'''

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Derived_metric_comment = 'test modify a derived metric description'

# Modify an existed derived metric "activeAgentCount" description
def modify_a_derived_metric(driver, wait, FMS_server_ip):
    # Go to "Manage Registry Variables" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_data_manage_derived_metrics.manageDerivedMetrics')
    # Click the checkbox before the "activeAgentCount" derived metric
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="activeAgentCount"]/preceding::img[contains(@src, "edit")][1]')))
    elem.click()
    # In the new redirected "Edit Derived Metric" page, click the "Change Derived Metrics Details" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Change Derived Metrics Details"]')))
    elem.click()
    # In the new prompte "Change Derived Metric Details" popup, for the "Description" textarea, enter Derived_metric_comment value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Change Derived Metric Details"]/following::div[text()="Description:"][1]//following::textarea[1]')))
    elem.clear()
    elem.send_keys(Derived_metric_comment)
    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Save"]')))
    elem.click()