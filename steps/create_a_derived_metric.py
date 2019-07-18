'''
[Automation Case] Create a derived metric
Derived Metric Name: "testDerivedMetric"
Comment: "This calculates the memory capacity in GB"
Unit: "gigabyte / gigabyte"
Value type: default "Metric"
For Calculations part:
    Description: "Get the 1st memory capacity, its unit is MB, divide it by 1024, to get the memory capacity in unit of GB"
    Choose "Data Driven"
    For Scope:
        Topology Type: "Memory"
        Property: "capacity"
        Instance: choose the 1st one
        Copy the Selected Instance string
        Paste the string to Scope part
    Expression: "#capacity# / 1024"
'''

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Derived_metric_name = 'testDerivedMetric'
Derived_metric_comment = 'This calculates the memory capacity in GB'
Unit_previous = 'gigabyte'
Unit_later = 'gigabyte'
Calculation_description = 'Get the 1st memory capacity, its unit is MB, divide it by 1024, to get the memory capacity in unit of GB'
Topology_type = 'Memory'
Topology_property = 'capacity'
Topology_instance = 'Memory'
Calculation_expression = '#capacity# / 1024'


# Create a derived metric
def create_a_derived_metric(driver, wait, FMS_server_ip):
    # Go to "Manage Registry Variables" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_data_manage_derived_metrics.manageDerivedMetrics')
    # Click the "Add" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Add "]')))
    elem.click()
    # In the new prompt "Create Derived Metric " popup, for the "Derived Metric Name:" input, enter Derived_metric_name value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Derived Metric Name:"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Derived_metric_name)
    # For the "Comments:" textarea, enter Derived_metric_comment value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Comments:"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Derived_metric_comment)
    # For the "Unit" part, previous part as "gigabyte", later part as "gigabyte", for "Value Type", use default "Metric", don't modify it.
    # For unit previous part, choose "gigabyte"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Unit:"]/following::select[1]//option[text()="gigabyte"]')))
    elem.click()
    # For unit later part, choose "gigabyte"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Unit:"]/following::select[2]//option[text()="gigabyte"]')))
    elem.click()
    # Click the "Add" button in "Create Derived Metric" popup
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Add"]')))
    elem.click()
    # In the new prompt "Create Calculation" popup, for the "Description" part, enter value Calculation_description
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Create Calculation"]/following::div[text()="Description"][1]//following::textarea[1]')))
    elem.clear()
    elem.send_keys(Calculation_description)
    # for "Scope" textarea, click the "Type and Properties" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//button[text()="Type and Properties"]')))
    elem.click()
    # In the new prompt "Types and Properties" popup, for "Topology Type", choose "Memory"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Topology Type"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Topology_type)
    # Wait for the drop-down list to appear, then click the "Memory" option (The drop-down list which appears when typing is hard to locate... Use this below one as an experience)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="popup"][contains(@style, "visibility: visible")]//li[text()="Memory"]')))
    elem.click()
    # For "Property", choose "capacity"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Property"]/following::input[2]')))
    elem.clear()
    elem.send_keys(Topology_property)
    # Wait for the drop-down list to appear, then click the "Memory" option (The drop-down list which appears when typing is hard to locate... Use this below one as an experience)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="popup"][contains(@style, "visibility: visible")]//li[text()="capacity"]')))
    elem.click()
    # For "Instance", choose the 1st "Memory"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Instance"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Topology_instance)
    # Wait for the drop-down list to appear, then click the 1st "Memory" option (The drop-down list which appears when typing is hard to locate... Use this below one as an experience)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '(//div[@class="popup"][contains(@style, "visibility: visible")]//li[text()="Memory"])[1]')))
    elem.click()
    # Copy the string in "Selected Instance" to tempCopy
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Selected Instance:"]/following-sibling::div[contains(text(), "Memory")][1]')))
    tempCopy = elem.text
    # Click the "x" button of "Types and Properties" popup
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Types and Properties"]/preceding::img[contains(@src, "close")][1]')))
    elem.click()
    # In popup of "Create Calculation", for "Scope" textarea, enter tempCopy content
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Scope"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(tempCopy)
    # For "Expression" textare, enter Calculation_expression value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Expression"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Calculation_expression)
    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Save"]')))
    elem.click()
    # In the popup of "Create Derived Metric", click the "Add" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Add"]')))
    elem.click()