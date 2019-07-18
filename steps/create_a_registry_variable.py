import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Registry_variable_name = 'testRegistryVariable'
Registry_variable_description = 'Test Registry Variable'
Registry_variable_value = 'Test Registry Variable value'
Performance_calendar_registry_variable_value = 'Registry variable performance calendar test value'
Topology_object_registry_value_value = 'Test registry variable registry value'

# Create a registry variable
# Create a registry variable, name as "testRegistryVariable", description as "Test Registry Variable", value type as "Static Value", value as "Test Registry Variable value"
def create_a_registry_variable(driver, wait, FMS_server_ip):
    # Add a registry variable
    # Go to "Manage Registry Variables" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_rulesnotifications_registryvariables.1')
    # Click the "Add..." button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Add..."]/preceding::img[contains(@src, "add")][1]')))
    elem.click()
    # In the new prompt "New Registry Variable Wizard" popup, for the drop-down list of under "Select type for registry variable:", choose "String" option
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Select type for registry variable:"]/following::select[1]//option[text()="String"]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # In the "Name" input, enter name as Registry_variable_name content
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Name"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Registry_variable_name)
    # In the "description" textarea, enter description as Registry_variable_description content
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Description"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Registry_variable_description)
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # Click the radio before "Static Value"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="radio"][@value="0"]')))
    elem.click()
    # In the "Enter desired value:" textarea, enter Registry_variable_value value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Enter desired value:"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Registry_variable_value)
    # Click the "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Finish"][@name="finish"]')))
    elem.click()

    # After adding registry variable, it will automatically redirect to "Edit Registry Variable: testRegistryVariable" page, in the "Performance Calendars List", add schedule as "First day of month", value type as "Static Value", value as "Registry variable performance calendar test value"
    # In "Performance Calendars List" panel, click the "Add..." button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Performance Calendars List"]/ancestor::div[@class="framedBox"][1]//span[text()="Add..."]/preceding::img[contains(@src, "add")][1]')))
    elem.click()
    # In the new prompt "Performance Calendar Wizard" popup, click the radio before "First day of month"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="First day of month"]/preceding::input[@type="radio"][1]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # Click the radio before "Static Value"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="radio"][@value="0"]')))
    elem.click()
    # In the "Enter desired value:" textarea, enter Registry_variable_value value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Enter desired value:"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Performance_calendar_registry_variable_value)
    # Click the "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@value="Finish"][@name="finish"]')))
    elem.click()

    # In the "Registry Values" panel, click the "Add..." button, choose "Topology Type" as "AccessInformation", then choose object as "Access Information for /", then choose value type as "Static Value", and set value as "Test registry variable registry value"

    # In the "Registry Values" panel, click the "Add..." button
    # Wait for the previous popup to disappear
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Registry Values"]/ancestor::div[@class="framedBox"][1]//span[text()="Add..."]/preceding::img[contains(@src, "add")][1]')))
    elem.click()
    # In the new prompt "Registry Value Wizard" popup, choose the "AccessInformation" row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="AccessInformation"]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # In the "Select objects of the desired type or all:" step, click the checkbox before "Access Information for /"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Select objects of the desired type or all:"]/following::span[text()="Access Information for /"][1]/preceding::input[@type="checkbox"][1]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # Click the radio before "Static Value"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="radio"][@value="0"]')))
    elem.click()
    # In the "Enter desired value:" textarea, enter Registry_variable_value value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Enter desired value:"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Topology_object_registry_value_value)
    # Click the "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@value="Finish"][@name="finish"]')))
    elem.click()