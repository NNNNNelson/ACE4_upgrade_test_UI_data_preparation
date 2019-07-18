from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Report_name = 'testScheduledReport'

# Create a "Hourly" scheduled report named "testScheduledReport" which uses template of "Agent Properties Report"
def create_a_scheduled_report(driver, wait, FMS_server_ip):
    # Go to "Reports" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:foglight_reports.main')
    # Click the "Run a Report" link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Run a Report")]')))
    elem.click()
    # In the new prompt "Run Report" pupup, in "Select Template" step, click the radio before "Agent Properties Report"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]/descendant::div[@class="summaryTitle"][text()="Select Template"]/following::span[text()="Agent Properties Report"]/preceding::input[@type="radio"]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # In "Set Input Parameters" step, click the "Next" button
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]/descendant::div[@class="summaryTitle"][text()="Set Input Parameters"]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # In "Set Properties" step, enter "Name" property value of "testScheduledReport"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]/descendant::div[@class="summaryTitle"][text()="Set Properties"]/following::div[text()="Name"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Report_name)
    # Click the checkbox after "Schedule This Report"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Schedule This Report"]/following::input[@type="checkbox"][1]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # In "Select Schedule" step, click the radio before "Hourly"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Hourly"]/preceding::input[@type="radio"][1]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # In "Summary" step, click "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]/descendant::div[@class="summaryTitle"][text()="Summary"]/following::input[@type="button"][@value="Finish"][@name="finish"]')))
    elem.click()