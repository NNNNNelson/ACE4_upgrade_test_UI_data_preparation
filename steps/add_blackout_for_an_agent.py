from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Black_name = 'Test_blackout_to_suspend_Monitor_WMI_data_collection_at_1st_day_of_month'
Black_reason = 'Blackout Monitor_WMI data collection just for testing'

# Add a blackout to suspend agent "Monitor_WMI" from collecting data in 1st day of month
def add_blackout_for_an_agent(driver, wait, FMS_server_ip):
    # Go to "Blackouts" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_blackout_configuration.blackouts')
    # Click the link "Create a Scheduled Blackout"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Create a Scheduled Blackout"]')))
    elem.click()
    # Check the radio before "Suspend Data Collection"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="radio"][2]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # Check the radio before "Select the Agents Directly from a List"
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Select Agents to Suspend Data Collection"]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="radio"][1]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # Choose the row of "Monitor_WMI"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Monitor_WMI"]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # Check the radio before "First day of month"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="First day of month"]/preceding::input[1]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # In "Blackout Name" input, enter "Test_blackout_to_suspend_Monitor_WMI_data_collection_at_1st_day_of_month"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Blackout Name"]/following::input[@type="text"][1]')))
    elem.clear()
    elem.send_keys(Black_name)
    # In "Reason for Blackout", enter "Blackout Monitor_WMI data collection just for testing"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Reason for Blackout"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Black_reason)
    # Click the "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Finish"][@name="finish"]')))
    elem.click()