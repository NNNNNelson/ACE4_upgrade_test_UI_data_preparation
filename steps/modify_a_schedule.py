'''
Modify the "Frequent" schedule:
    Schedule Description: Change from
        "A schedule that runs very frequently.  Primarily used for testing.   This schedule is used to trigger an activity.  As a result it does not have a significant duration."
        to
        "A schedule that runs very frequently.  Primarily used for testing.   This schedule is used to trigger an activity.  As a result it does not have a significant duration.
        ============================================
        Test modify "Frequent" schedule description"
'''

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Schedule_description_add = '\n=======================\nTest modify "Frequent" schedule description'

# Modify a schedule
def modify_a_schedule(driver, wait, FMS_server_ip):
    # Go to "Manage Schedules" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_schedules_manageschedules.manageSchedules')
    # Click the "Frequent" schedule name
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Frequent"]')))
    elem.click()
    # In the new prompt "Edit Schedule" popup, for the "Schedule Description" textarea, add Schedule_description_add content
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Description/Comments:"]/following::textarea[1]')))
    elem.send_keys(Schedule_description_add)
    # Click the "Change" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//button[@type="submit"][text()="Change"]')))
    elem.click()