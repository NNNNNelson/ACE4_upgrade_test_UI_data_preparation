# Test: Upgrade for IC/Fglam
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Monitor a WMI
def monitor_WMI(driver, wait, FMS_server_ip, WMI_machine_IP, WMI_machine_username, WMI_machine_password):
    # Go to "Agent Status" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_agents_agent_status.agentStatus')
    # Click the "Create Agent" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//img[contains(@src, "create_agent16")]')))
    elem.click()
    # In the prompt dialog "Create Agent", click the checkbox bofore the first fglam
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '((//div[@id="system:administration_agents_agent_status.hostSelectorAgentStatus:1_summary"]/following-sibling::div//table)[2]//td//input[@type="checkbox"])[1]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"][not(@disabled)]')))
    elem.click()
    # Choose "WindowsAgent" row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="system:administration_agents_agenthost_createagent.AgentTypeandInstanceName:1_summary"]/following-sibling::div//td//span[text()="WindowsAgent"]')))
    elem.click()
    # Choose "Specify Name"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="radio"][2]')))
    elem.click()
    # Enter "Monitor_WMI" in the "Name" part
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Name"]/following-sibling::div/input')))
    elem.send_keys("Monitor_WMI")
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"][not(@disabled)]')))
    elem.click()
    # Click the "Finish" button to complete the creating agent process
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Finish" and @name="finish"][not(@disabled)]')))
    elem.click()
    # Choose the new created "Monitor_WMI" row checkbox
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Monitor_WMI"]/ancestor::tr//input[@type="checkbox"]')))
    elem.click()
    # Click the "Edit Properties" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Edit Properties"]/preceding-sibling::img[contains(@src, "editProperties")][not(contains(@class, "disabled"))]')))
    elem.click()
    # Click the " Modify properties for this agent only." link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()=" Modify properties for this agent only."]')))
    elem.click()
    # When the "Host" parameter input is enabled, send WMI machine IP to it
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Host"]/following-sibling::div//input[@type="text"][not(@disabled="disabled")]')))
    elem.send_keys(WMI_machine_IP)
    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Save"]')))
    elem.click()
    # Wait for the save completes (the "Host" parameter input becomes disabled again), go to "Credential" dashboard
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Host"]/following-sibling::div//input[@type="text"][@disabled="disabled"]')))

    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_credentials.Credentials')
    # Click the "Manage Credentials" link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Manage Credentials"]')))
    elem.click()
    # Click the "Add" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="toolbar"]//img[contains(@src, "add")]')))
    elem.click()
    # In the popup list, choose "Domain, User Name, and Password (Windows)"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Domain, User Name, and Password (Windows)"]')))
    elem.click()
    # In "User Name" parameter input, enter the WMI machine username
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="User Name"]/following-sibling::div/input')))
    elem.send_keys(WMI_machine_username)
    # In "Password" parameter input, enter the WMI machine password
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Password"]/following-sibling::div/input')))
    elem.send_keys(WMI_machine_password)
    # In "Confirm Password" parameter input, enter the WMI machine password again
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Confirm Password"]/following-sibling::div/input')))
    elem.send_keys(WMI_machine_password)
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"]')))
    elem.click()
    # In the "Please provide a unique name to identify this credential." input filed, enter credential name as "WMI_machine_credential"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Please provide a unique name to identify this credential."]//following-sibling::div/input')))
    elem.clear()
    elem.send_keys('WMI_machine_credential')
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"]')))
    elem.click()
    # Wait for the "Resource Mapping" step appears, click the "Add" button to add mapping
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="summaryTitle"][text()="Resource Mapping"]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[@class="toolbar"]//img[contains(@src, "add")]')))
    elem.click()
    # In the popup window, for the "Usage" parameter, click the link to show dropdown list, then choose "Infrastructure Monitoring for Windows"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Usage"]/following-sibling::div[1]//a')))
    elem.click()
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Infrastructure Monitoring for Windows"]')))
    elem.click()
    # For the "Access Resources Using" parameter, click the link to show dropdown list, then choose "Target Host Address"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Access Resources Using"]/following-sibling::div[1]//a')))
    elem.click()
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Target Host Address"]')))
    elem.click()
    # Click the "Add a New IP Address" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Add a New IP Address"]')))
    elem.click()
    # Enter the WMI_machine_IP to the "IP Address" row. (Nelson note: element.send_keys failed, so, change to use ActionChain to send_keys)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@column-id="IPAddress"][text()]')))
    elem.click()
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(WMI_machine_IP)
    actions.perform()
    # Click the "Add" button to continue the "Resource Mapping" process
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Add"]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"]')))
    elem.click()
    #  When the "Policies" step appears, click the "Finish" button to complete credential creation
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="summaryTitle"][text()="Policies"]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Finish" and @name="finish"]')))
    elem.click()

    # Go to "Agent Status" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_agents_agent_status.agentStatus')
    # Click the checkbox of "Monitor_WMI" row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '((//span[text()="Monitor_WMI"]/ancestor::td)[1]//preceding-sibling::td)[1]//input[@type="checkbox"]')))
    elem.click()
    # Wait for the "Activate" button is enabled, click the button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Activate"]/preceding-sibling::img[not(contains(@class, "disabled"))]')))
    elem.click()


# Monitor a WinRM
def monitor_WinRM(driver, wait, FMS_server_ip, WinRM_machine_IP, WinRM_machine_username, WinRM_machine_password):
    # Go to "Agent Status" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_agents_agent_status.agentStatus')
    # Click the "Create Agent" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//img[contains(@src, "create_agent16")]')))
    elem.click()
    # In the prompt dialog "Create Agent", click the checkbox bofore the first fglam
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '((//div[@id="system:administration_agents_agent_status.hostSelectorAgentStatus:1_summary"]/following-sibling::div//table)[2]//td//input[@type="checkbox"])[1]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"][not(@disabled)]')))
    elem.click()
    # Choose "WindowsAgent" row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="system:administration_agents_agenthost_createagent.AgentTypeandInstanceName:1_summary"]/following-sibling::div//td//span[text()="WindowsAgent"]')))
    elem.click()
    # Choose "Specify Name"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="radio"][2]')))
    elem.click()
    # Enter "Monitor_WinRM" in the "Name" part
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Name"]/following-sibling::div/input')))
    elem.send_keys("Monitor_WinRM")
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"][not(@disabled)]')))
    elem.click()
    # Click the "Finish" button to complete the creating agent process
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Finish" and @name="finish"][not(@disabled)]')))
    elem.click()
    # Choose the new created "Monitor_WinRM" row checkbox
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Monitor_WinRM"]/ancestor::tr//input[@type="checkbox"]')))
    elem.click()
    # Click the "Edit Properties" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Edit Properties"]/preceding-sibling::img[contains(@src, "editProperties")][not(contains(@class, "disabled"))]')))
    elem.click()
    # Click the " Modify properties for this agent only." link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()=" Modify properties for this agent only."]')))
    elem.click()
    # When the "Host" parameter input is enabled, send WinRM machine IP to it
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Host"]/following-sibling::div//input[@type="text"][not(@disabled="disabled")]')))
    elem.send_keys(WinRM_machine_IP)
    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Save"]')))
    elem.click()
    # Wait for the save completes (the "Host" parameter input becomes disabled again), go to "Credential" dashboard
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Host"]/following-sibling::div//input[@type="text"][@disabled="disabled"]')))

    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_credentials.Credentials')
    # Click the "Manage Credentials" link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Manage Credentials"]')))
    elem.click()
    # Click the "Add" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="toolbar"]//img[contains(@src, "add")]')))
    elem.click()
    # In the popup list, choose "Domain, User Name, and Password (Windows)"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@column-id="Name"]/span[text()="Domain, User Name, and Password (Windows)"]')))
    elem.click()
    # In "User Name" parameter input, enter the WinRM machine username
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="User Name"]/following-sibling::div/input')))
    elem.send_keys(WinRM_machine_username)
    # In "Password" parameter input, enter the WinRM machine password
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Password"]/following-sibling::div/input')))
    elem.send_keys(WinRM_machine_password)
    # In "Confirm Password" parameter input, enter the WinRM machine password again
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Confirm Password"]/following-sibling::div/input')))
    elem.send_keys(WinRM_machine_password)
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"]')))
    elem.click()
    # In the "Please provide a unique name to identify this credential." input filed, enter credential name as "WinRM_machine_credential"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Please provide a unique name to identify this credential."]//following-sibling::div/input')))
    elem.clear()
    elem.send_keys('WinRM_machine_credential')
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"]')))
    elem.click()
    # Wait for the "Resource Mapping" step appears, click the "Add" button to add mapping
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="summaryTitle"][text()="Resource Mapping"]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[@class="toolbar"]//img[contains(@src, "add")]')))
    elem.click()
    # In the popup window, for the "Usage" parameter, click the link to show dropdown list, then choose "Infrastructure Monitoring for Windows"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Usage"]/following-sibling::div[1]//a')))
    elem.click()
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Infrastructure Monitoring for Windows"]')))
    elem.click()
    # For the "Access Resources Using" parameter, click the link to show dropdown list, then choose "Target Host Address"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Access Resources Using"]/following-sibling::div[1]//a')))
    elem.click()
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Target Host Address"]')))
    elem.click()
    # Click the "Add a New IP Address" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Add a New IP Address"]')))
    elem.click()
    # Enter the WinRM_machine_IP to the "IP Address" row. (Nelson note: element.send_keys failed, so, change to use ActionChain to send_keys)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@column-id="IPAddress"][text()]')))
    elem.click()
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(WinRM_machine_IP)
    actions.perform()
    # Click the "Add" button to continue the "Resource Mapping" process
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Add"]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"]')))
    elem.click()
    #  When the "Policies" step appears, click the "Finish" button to complete credential creation
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="summaryTitle"][text()="Policies"]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Finish" and @name="finish"]')))
    elem.click()

    # Go to "Agent Status" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_agents_agent_status.agentStatus')
    # Click the checkbox of "Monitor_WinRM" row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '((//span[text()="Monitor_WinRM"]/ancestor::td)[1]//preceding-sibling::td)[1]//input[@type="checkbox"]')))
    elem.click()
    # Wait for the "Activate" button is enabled, click the button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Activate"]/preceding-sibling::img[not(contains(@class, "disabled"))]')))
    elem.click()