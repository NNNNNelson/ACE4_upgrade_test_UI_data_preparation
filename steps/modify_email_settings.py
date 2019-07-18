import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Mail_server = 'relay.prod.quest.corp'
Mail_sender = 'nelson.wang@quest.com'
Mail_user = 'nelson.wang@quest.com'

# Modify email configuration to make FMS be able to send mail
def modify_email_settings(driver, wait, FMS_server_ip):
    # Go to "Email Configuration" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_setupsupport.82')

    # For "Mail Server (Name or IP) *" property, click the "Edit" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Mail Server (Name or IP) *"]/following::img[contains(@src, "edit")][1]')))
    elem.click()
    # In the new prompt "Host name for sending emails" popup, for the textarea, enter Mail_server content
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Host name for sending emails"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Mail_server)
    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Save"]')))
    elem.click()

    # For "Email Sender Address *" property, click the "Edit" button
    time.sleep(0.5)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Email Sender Address *"]/following::img[contains(@src, "edit")][1]')))
    elem.click()
    # In the new prompt "Host name for sending emails" popup, for the textarea, enter Mail_sender content
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Sender\'s email address"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Mail_sender)
    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Save"]')))
    elem.click()

    # For "Username to Login to Server" property, click the "Edit" button
    time.sleep(0.5)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Username to Login to Server"]/following::img[contains(@src, "edit")][1]')))
    elem.click()
    # In the new prompt "Username for mail server login" popup, for the textarea, enter Mail_user content
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Username for mail server login"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Mail_user)
    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Save"]')))
    elem.click()

    # For "Mail Server Port" property, click the "Edit" button
    time.sleep(0.5)
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Mail Server Port"]/following::img[contains(@src, "edit")][1]')))
    elem.click()
    # In the new prompt "Mail server port for sending emails" popup, keep the default value "25" (do not change it at all), directly click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Mail server port for sending emails"]/following::button[@type="submit"][text()="Save"]')))
    elem.click()