from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Create a new user "testnewuser" with password "Rdis2fun!"
def create_a_new_user(driver, wait, FMS_server_ip, new_create_user_username, new_create_user_password):
    # Go to "Users & Security" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_userssecurity.main')

    # Click the "There are \d users (\d managed by Active Directory)." link to go to "User Management" page "Users" tab
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Manage Users, Groups, Roles"]/ancestor::div[1]/following-sibling::div//a')))
    elem.click()

    # When "New User" button appears, click it
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="New User"]')))
    elem.click()

    # When the prompt dialog appears, for the "Name" parameter in it, enter "testnewuser"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Name"]/following::input[1]')))
    elem.send_keys(new_create_user_username)

    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"]')))
    elem.click()

    # In "Group Assignment" step, click the checkbox in title row to select all groups
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Group Assignment"]/following::input[@type="checkbox"][1]')))
    elem.click()

    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"]')))
    elem.click()

    # In "User Password" step, for the "Password" parameter, enter "Rdis2fun!"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="User Password"]/following::div[text()="Password"]/following-sibling::div[1]//input')))
    elem.send_keys(new_create_user_password)

    # For the "Confirm Password" parameter, enter "Rdis2fun!" again
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="User Password"]/following::div[text()="Confirm Password"]/following-sibling::div[1]//input')))
    elem.send_keys(new_create_user_password)

    # Uncheck the checkbox before "Change Password at the next logon"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Change Password at the next logon"]/preceding-sibling::div[1]/input[@type="checkbox"]')))
    elem.click()

    # Click the "Next" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"]')))
    elem.click()

    # In "Select Home Page (Optional)" step, click the "Next" button
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[@class="summaryTitle"][contains(text(), "Home Page (Optional)")]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"]')))
    elem.click()

    # In "Select Default Time Range" step, click the "Next" button
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[@class="summaryTitle"][text()="Select Default Time Range"]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Next" and @name="nextCard"]')))
    elem.click()

    # In "Refresh Interval (Optional)" step, click the "Finish" button
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[@class="summaryTitle"][contains(text(), "Refresh Interval")]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="Finish" and @name="finish"]')))
    elem.click()

    # In the new prompt "Make User Process", click the "Ok" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Ok"]')))
    elem.click()