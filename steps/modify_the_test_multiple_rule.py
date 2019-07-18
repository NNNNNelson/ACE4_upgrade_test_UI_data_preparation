import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Rule_description_add_content = '\ntest modify rule description'
Alarm_description_add_content = '\ntest modify alarm description'
Rule_critical_condition = '#freeMemory# < 99'
Rule_critical_alarm_message = 'testMultipleRule critical alarm message'
Severity_level_variable_name = 'testSeverityLevelVariable'
Severity_level_variable_message = 'testSeverityLevelVariable message'
Command_line_value = 'test_COMMAND_LINE'
Hostname_value = 'testHostName'
Behavior_fire_out_of_previous_num = '1'
Behavior_fire_out_of_later_num = '2'
Message_name = 'testRuleVariable'
Message_content = 'testRuleVariable message'

# Modify the rule "testMultipleRule"
def modify_the_test_multiple_rule(driver, wait, FMS_server_ip):
    # Go to "Rules" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_rulesnotifications_rulemanagement.ruleManagement')

    # For "Cartridge" drop-down list, verify its value is "Non-Cartridge", if not, change it to "Non-Cartridge"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Cartridge: "]/following::input[@class="dropDownField"][1]')))
    if elem.get_attribute('value') != 'Non-Cartridge':
        elem.click()
        elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="popupSharedDiv"][contains(@style, "visibility: visible")]/descendant::span[text()="Non-Cartridge"][1]')))
        elem.click()
        time.sleep(1)

    # Choose "testMultipleRule" to enter its edit page
    # Click the rule name of rule "testMultipleRule"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="testMultipleRule"]')))
    elem.click()
    # In the new prompt "testMultipleRule" popup, click the "View and Edit" item
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="tmpPopupContainer"]//div[text()="testMultipleRule"]/following::a[text()="View and Edit"][1]')))
    elem.click()
    # In the new prompt "Rule Detail -  testMultipleRule" popup, click the "Rule Editor" link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Rule Detail -  testMultipleRule"]/following::a[text()="Rule Editor"][1]')))
    elem.click()

    # Go to "Rule Definition" tab (here needs to switch iframe)
    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@src, "editRule")]'))))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Rule Definition					")]')))
    elem.click()
    # In the "Rule Description" text area, add string Rule_description_add_content content
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="commentField"]')))
    elem.send_keys(Rule_description_add_content)
    # In the "Alarm Description" text area, add string Alarm_description_add_content content
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="helpField"]')))
    elem.send_keys(Alarm_description_add_content)
    # Click the "Save" button (I tried but failed to click the "Save" button, so, change to execute script "save()" to simulate clicking the "Save" button)
    driver.execute_script("save()")

    # Go to "Conditions, Alarms & Actions" tab
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Conditions, Alarms & Actions				")]')))
    elem.click()
    # In the new prompt "Rule Confirmation" popup, click the "OK" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="confirmDialog"]//button[@type="button"][text()="OK"]')))
    elem.click()
    # In "Condition & Actions" tab, expand the "Critical" bar
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="titlebar_critical"]')))
    elem.click()
    # In the "Condition" tab of "Critical", click the checkbox before "Activate"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="utc3"][@type="checkbox"][@name="useThisC3"]')))
    elem.click()
    # In the "Condition" tab of "Critical", in the condition textarea, enter "#freeMemory# < 99"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="condition3"]')))
    elem.clear()
    elem.send_keys(Rule_critical_condition)
    # In the "Condition" tab of "Critical", in the "Alarm Message" textarea, enter "testMultipleRule critical alarm message"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="alarm3"]')))
    elem.clear()
    elem.send_keys(Rule_critical_alarm_message)
    # Click the "Severity Level Variables" tab to switch "Severity Level Variables" tab
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="titlebar_critical"]/following::div[contains(text(), "Severity Level Variables			")][1]/following::img[contains(@src, "transparent.gif")][1]')))
    elem.click()
    # Click the radio before "Message" item
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="messageRadio1"]')))
    elem.click()
    # In "Name" input, enter "testSeverityLevelVariable"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="varName1"]')))
    elem.clear()
    elem.send_keys(Severity_level_variable_name)
    # In "Expression/Message" textarea, enter "testSeverityLevelVariable message"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="varValue1"]')))
    elem.clear()
    elem.send_keys(Severity_level_variable_message)
    # Click the "<<Add" button to add the SeverityLevelVariable to left "Severity Level Variables" table
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@value="<<Add"][@type="button"])[3]')))
    elem.click()
    # Click the "Action" tab to switch "Action" tab (can't click it in my test, change to execute script "showActionTab(1)" to simulate clicking "Action" tab)
    time.sleep(2)
    driver.execute_script('showActionTab(1)')
    # In "Action" tab, for the "Action" property, click the drop-down list and choose "EmailAction"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="content_critical"][not(contains(@style, "visibility: hidden;"))]//select[@id="newActionName1"]')))
    elem.click()
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="newActionName1"]//option[@value="RemoteCommandAction"]')))
    elem.click()
    time.sleep(2)
    # Click the "<<Add" button to add the "EmailAction" to left "Actions" table
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="titlebar_critical"]/following::input[@value="<<Add"][@type="button"][2]')))
    elem.click()
    # Wait for the "Action Parameters" table to appear, then, for the "COMMAND_LINE", click the "Default" link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="COMMAND_LINE"]/following::span[1]')))
    elem.click()
    # In the new prompt "Action Parameter Editor" popup, click the tab "User Defined" (wait for the id="workaroundFramePE" iframe to be visible first)
    wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@id="workaroundFramePE"][contains(@style, "visibility: visible")]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@id="userDefinedLabel"]/following::img[contains(@src, "transparent.gif")][1]')))
    elem.click()
    # In the "User Defined" tab, in the textarea, enter Command_line_value value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="newContentText"]')))
    elem.clear()
    elem.send_keys(Command_line_value)
    # Click the "Change" button (I can't use the element click to click the "Change" button, so I change to run script "updateFromUserDefined()" to do the "Chagne" action)
    driver.execute_script('updateFromUserDefined()')
    # For the "HostName", click the "Default" link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="HostName"]/following::span[1]')))
    elem.click()
    # In the new prompt "Action Parameter Editor" popup, click the tab "User Defined" (wait for the id="workaroundFramePE" iframe to be visible first)
    wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@id="workaroundFramePE"][contains(@style, "visibility: visible")]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@id="userDefinedLabel"]/following::img[contains(@src, "transparent.gif")][1]')))
    elem.click()
    # In the "User Defined" tab, in the textarea, enter Hostname_value value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="newContentText"]')))
    elem.clear()
    elem.send_keys(Hostname_value)
    # Click the "Change" button (I can't use the element click to click the "Change" button, so I change to run script "updateFromUserDefined()" to do the "Chagne" action)
    driver.execute_script('updateFromUserDefined()')
    # Wait for the prompt "Action Parameter Editor" popup to disappear, then, click the "Save All" button (I can't use the element click to click the "Save All" button, so I change to run script "saveAllSeverities()" to do the "Save All" action)
    wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@id="workaroundFramePE"][contains(@style, "visibility: hidden")]')))
    driver.execute_script('saveAllSeverities()')

    # Go to "Schedules" tab
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Schedules				")]')))
    elem.click()
    # In the "--- Available Schedules ---" option table on the left of "--- Effective Schedules ---" option table, click the "Always" option
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//optgroup[@label="--- Effective Schedules ---"]/preceding::optgroup[@label="--- Available Schedules ---"][1]//option[text()="Always"]')))
    elem.click()
    # Click the "Add>>" button on the left of "--- Effective Schedules ---" option table
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//optgroup[@label="--- Effective Schedules ---"]/preceding::input[@type="button"][@value="Add>>"][1]')))
    elem.click()
    # In the "--- Available Schedules ---" option table on the left of "--- Blackout Schedules ---" option table, click the "Beginning of the month" option
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//optgroup[@label="--- Blackout Schedules ---"]/preceding::optgroup[@label="--- Available Schedules ---"][1]//option[contains(text(), "First") and contains(text(), "day") and contains(text(), "of") and contains(text(), "month")]')))
    elem.click()
    # Click the "Add>>" button on the left of "--- Blackout Schedules ---" option table
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//optgroup[@label="--- Blackout Schedules ---"]/preceding::input[@type="button"][@value="Add>>"][1]')))
    elem.click()
    # Click the "Save" button (I can't use the element click to click the "Change" button, so I change to run script "saveSchedules()" to do the "Save" action)
    driver.execute_script('saveSchedules()')

    # Go to "Behavior" tab
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Behavior					")]')))
    elem.click()
    # Click the checkbox before "Fire actions if 0 out of 0 evaluations are true"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//label[text()="out of"]/preceding::input[@type="checkbox"][1]')))
    elem.click()
    # Modify the numbers in "Fire actions if 0 out of 0 evaluations are true" from "0 out of 0" to "1 out of 2"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="fireNooMN"]')))
    elem.clear()
    elem.send_keys(Behavior_fire_out_of_previous_num)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="fireNooMM"]')))
    elem.clear()
    elem.send_keys(Behavior_fire_out_of_later_num)
    # Click the "Save" button (I can't use the element click to click the "Save" button, so I change to run script "saveStrategy()" to do the "Save" action)
    driver.execute_script('saveStrategy()')

    # Go to "Rule Variables" tab
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Rule Variables					")]')))
    elem.click()
    # Click the radio before "Message" option
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="messageRadio"]')))
    elem.click()
    # In "Name" input, enter Message_name value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="varName"]')))
    elem.clear()
    elem.send_keys(Message_name)
    # In "Expression/Message" textarea, enter Message_content value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="varValue"]')))
    elem.clear()
    elem.send_keys(Message_content)
    # Click the "<<Add" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="<<Add"]')))
    elem.click()