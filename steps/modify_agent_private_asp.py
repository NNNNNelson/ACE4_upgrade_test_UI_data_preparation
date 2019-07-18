from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Modify an agent's private asp
def modify_agent_private_asp(driver, wait, FMS_server_ip):
    # Go to "Agent Status" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_agents_agent_status.agentStatus')
    # Choose the "Monitor_WMI" row checkbox
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Monitor_WMI"]/ancestor::tr//input[@type="checkbox"]')))
    elem.click()
    # Click the "Edit Properties" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Edit Properties"]/preceding-sibling::img[contains(@src, "editProperties")][not(contains(@class, "disabled"))]')))
    elem.click()
    # Click the " Modify the private properties for this agent." link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()=" Modify the private properties for this agent."]')))
    elem.click()
    # Modify "Top CPU Processes" value from 5 to 8
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Top CPU Processes"]/following::input[1][not(@disabled)]')))
    elem.clear()
    elem.send_keys('8')
    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Save"]')))
    elem.click()