import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Rule_name = 'testSimpleRule'
Rule_description = 'testSimpleRule description'
Alarm_description = 'testSimpleRule alarm description'
Rule_scope = 'Memory'
Rule_condition = '#utilization# > 1'
Email_recipient = 'nelson.wang@@quest.com'
Email_subject = 'testSimpleRule email subject'
Email_message = 'testSimpleRule email message'
Behavior_fire_consecutive = '1'

# Create a simple rule name "testSimpleRule" to send mail to "nelson.wang@quest.com"
def create_a_simple_rule(driver, wait, FMS_server_ip):
    # Go to "Create Rule" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_rulesnotifications.1')
    # In "Rule Name" property, enter value as "testSimpleRule" (here needs to switch iframe)
    driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@src, "createCompleteRule")]'))))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//label[text()="Rule Name:"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Rule_name)
    # In "Rule Description" textarea, enter description content
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//label[text()="Rule Description:"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Rule_description)
    # In "Alarm Description" textarea, enter alarm description
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//label[text()="Alarm Description:"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Alarm_description)
    # In "Rule Scope" first textarea, enter "Memory" as scope
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="scopeField"]')))
    elem.clear()
    elem.send_keys(Rule_scope)
    # Click the "Next >>" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next >>"]')))
    elem.click()

    # In "Condition & Actions" tab, expand the "Fire" bar
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="titlebar_fire"]')))
    elem.click()
    # In the "Condition" tab of "Fire", in the condition textarea, enter "#utilization# > 1"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="condition1"]')))
    elem.clear()
    elem.send_keys(Rule_condition)
    # Click the "Action" tab to switch "Action" tab
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '(//div[contains(text(), "Action			")])[1]/following::img[contains(@src, "transparent.gif")][1]')))
    elem.click()
    # In "Action" tab, for the "Action" property, click the drop-down list and choose "EmailAction"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="newActionName0"]')))
    elem.click()
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="EmailAction"]')))
    elem.click()
    time.sleep(2)
    # Click the "<<Add" button to add the "EmailAction" to left "Actions" table
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@value="<<Add"][@type="button"])[2]')))
    elem.click()
    # Wait for the "Action Parameters" table to appear, then, for the "mail.recipient", click the "Default" link
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="mail.recipient"]/following::span[1]')))
    elem.click()
    # In the new prompt "Action Parameter Editor" popup, click the tab "User Defined" (wait for the id="workaroundFramePE" iframe to be visible first)
    wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@id="workaroundFramePE"][contains(@style, "visibility: visible")]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@id="userDefinedLabel"]/following::img[contains(@src, "transparent.gif")][1]')))
    elem.click()
    # In the "User Defined" tab, in the textarea, enter Email_recipient
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="newContentText"]')))
    elem.clear()
    elem.send_keys(Email_recipient)
    # Click the "Change" button (I can't use the element click to click the "Change" button, so I change to run script "updateFromUserDefined()" to do the "Chagne" action)
    driver.execute_script('updateFromUserDefined()')
    # For the "mail.subject", click the "Default" link (need to click "Default" twice, because 1st time click will show the horizontal scroll bar, the 2nd time click can really click the default link)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="mail.subject"]/following::span[1]')))
    elem.click()
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="mail.subject"]/following::span[1]')))
    elem.click()
    # In the new prompt "Action Parameter Editor" popup, click the tab "User Defined" (wait for the id="workaroundFramePE" iframe to be visible first)
    wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@id="workaroundFramePE"][contains(@style, "visibility: visible")]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@id="userDefinedLabel"]/following::img[contains(@src, "transparent.gif")][1]')))
    elem.click()
    # In the "User Defined" tab, in the textarea, enter Email_subject
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="newContentText"]')))
    elem.clear()
    elem.send_keys(Email_subject)
    # Click the "Change" button (I can't use the element click to click the "Change" button, so I change to run script "updateFromUserDefined()" to do the "Chagne" action)
    driver.execute_script('updateFromUserDefined()')
    # For the "mail.message", click the "Default" link (need to click "Default" twice, because 1st time click will show the horizontal scroll bar, the 2nd time click can really click the default link)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="mail.message"]/following::span[1]')))
    elem.click()
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="mail.message"]/following::span[1]')))
    elem.click()
    # In the new prompt "Action Parameter Editor" popup, click the tab "User Defined" (wait for the id="workaroundFramePE" iframe to be visible first)
    wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@id="workaroundFramePE"][contains(@style, "visibility: visible")]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@id="userDefinedLabel"]/following::img[contains(@src, "transparent.gif")][1]')))
    elem.click()
    # In the "User Defined" tab, in the textarea, enter Email_message
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="newContentText"]')))
    elem.clear()
    elem.send_keys(Email_message)
    # Click the "Change" button (I can't use the element click to click the "Change" button, so I change to run script "updateFromUserDefined()" to do the "Chagne" action)
    driver.execute_script('updateFromUserDefined()')
    # Wait for the "Action Parameter Editor" to disappear
    wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@id="workaroundFramePE"][contains(@style, "visibility: hidden")]')))

    # Go to "Behavior" tab
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Behavior			")]')))
    elem.click()
    # Click the checkbox before "Fire action if 0 consecutive evaluations are true"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//label[text()="consecutive evaluations are true"]/preceding::input[@type="checkbox"][1]')))
    elem.click()
    # Modify the number in "Fire action if 0 consecutive evaluations are true" from "0" to "1"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="fireConsecutiveN"]')))
    elem.clear()
    elem.send_keys(Behavior_fire_consecutive)

    # Click the "Finish" button to finish the rule creation
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@id="finishButton"][@value="Finish"]')))
    elem.click()