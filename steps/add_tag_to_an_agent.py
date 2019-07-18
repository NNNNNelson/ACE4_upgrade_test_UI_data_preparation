from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

Test_tag_name = 'testtag'

# Add a tag "testTag" to agent "Monitor_WMI"
def add_tag_to_an_agent(driver, wait, FMS_server_ip):
    # Go to "Agent Status" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_agents_agent_status.agentStatus')
    # Choose the "Monitor_WMI" row checkbox
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Monitor_WMI"]/ancestor::tr//input[@type="checkbox"]')))
    elem.click()
    # Click the "Edit Tags" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Edit Tags"]/preceding-sibling::img[contains(@src, "tag")][not(contains(@class, "disabled"))]')))
    elem.click()
    # In the new prompt "Edit Tags" popup, click the "Add Tags" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]/descendant::button[text()=" Add Tags          "]')))
    elem.click()
    # In the new prompt smaller popup, enter tag name "testtag" in "Add a new Tag" input
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Add a new Tag"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Test_tag_name)
    # Click the "Add" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Add"][@type="submit"]')))
    elem.click()
    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Save"][@type="submit"]')))
    elem.click()