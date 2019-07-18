from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Modify an agent's all asp
def modify_agent_all_asp(driver, wait, FMS_server_ip):
    # Go to "Agent Status" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_agents_agent_status.agentStatus')
    # Choose the "Monitor_WinRM" row checkbox
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Monitor_WinRM"]/ancestor::tr//input[@type="checkbox"]')))
    elem.click()
    # Click the "Edit Properties" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Edit Properties"]/preceding-sibling::img[contains(@src, "editProperties")][not(contains(@class, "disabled"))]')))
    elem.click()
    # Click the " Modify the properties for all WindowsAgent agents" link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), " Modify the properties for all ")]')))
    elem.click()
    # Modify "Top Memory Processes" value from 5 to 7
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Top Memory Processes"]/following::input[1][not(@disabled)]')))
    elem.clear()
    elem.send_keys('7')
    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Save"]')))
    elem.click()
    # In the new prompt "Confirm Save" popup, click "Yes" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Confirm Save"]/following::button[@type="submit"][text()="Yes"]')))
    elem.click()