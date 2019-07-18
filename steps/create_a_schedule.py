'''
Create a new schedule:
    Start: Current day 00:00
    End Time: Current day 00:30
    Recurrence: Once
    Schedule Name: testSchedule
    Schedule Description: This is a test schedule
'''

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Start_time = '0:00'
End_time = '0:30'
Schedule_name = 'testSchedule'
Schedule_description = 'This is a test schedule'

# Create a schedule
def create_a_schedule(driver, wait, FMS_server_ip):
    # Go to "Manage Schedules" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_schedules_manageschedules.manageSchedules')
    # Click the "Add" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Add"]')))
    elem.click()
    # In the new prompt "Create Schedule" popup, for "Start" part, leave date as default, for time, choose "0:00"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Start:"]/following::input[@type="text"][@class="dropDownField"][1]')))
    elem.clear()
    elem.send_keys(Start_time)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="popup"][contains(@style, "visibility: visible")]//li[text()="0:00"]')))
    elem.click()
    # For "End" part, leave date as default, for time, choose "0:30"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="End:   "]/following::input[@type="text"][@class="dropDownField"][1]')))
    elem.clear()
    elem.send_keys(End_time)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="popup"][contains(@style, "visibility: visible")]//li[text()="0:30"]')))
    elem.click()
    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # In the "Occurrence" step, use the default choice of "Onece", directly click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[@class="summaryTitle"][text()="Recurrence"]/following::input[@type="button"][@value="Next"][@name="nextCard"]')))
    elem.click()
    # In the "Summary" step, for "Schedule Name" input, enter Schedule_name value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Schedule Name:"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Schedule_name)
    # For "Schedule Description" textarea, enter Schedule_description value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Schedule Description :"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Schedule_description)
    # Click the "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@value="Finish"][@name="finish"]')))
    elem.click()
    # In the new prompt "Schedule Confirmation" popup, click the "OK" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Schedule Confirmation"]/following::button[@type="submit"][text()="OK"]')))
    elem.click()
    # Click the "Cancel" button to close the popup
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@value="Cancel"][@name="cancel"]')))
    elem.click()