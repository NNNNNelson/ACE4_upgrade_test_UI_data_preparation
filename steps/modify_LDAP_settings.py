import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Nearest_LDAP_server_URL = 'ldap://torgdcw01.prod.quest.corp:389/'
Secondary_LDAP_server_URL = 'ldap://halgdcw01.prod.quest.corp:389/'
Service_account_name = 'CN=svc-ADSInteg,OU=Enabled SVC-Accounts,OU=SVC-Accounts,OU=IS,DC=prod,DC=quest,DC=corp'
Password = '6Sixthnum'
LDAP_query_suffix = ',OU=Employees,DC=prod,DC=quest,DC=corp'
Scope_for_groups = 'OU=Groups,DC=prod,DC=quest,DC=corp'
Second_group_namespace = 'OU=Dynamic Groups,DC=prod,DC=quest,DC=corp'
LDAP_context = 'ou=Employees,DC=prod,DC=quest,DC=corp'
Maximum_group_nesting = '15'

# Modify LDAP settings
def modify_LDAP_settings(driver, wait, FMS_server_ip):
    # Go to "Users & Security" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_userssecurity_directory_services.configureDirectoryServices')

    # In "LDAP Locations" area, click the "Edit" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="LDAP Locations"]/ancestor::div[@class="framedBox"][1]//span[text()="Edit"]')))
    elem.click()

    # In the "URLs Editor" popup, for the "Nearest LDAP server URL" parameter, enter the Nearest LDAP server URL
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="URLs Editor"]/following::span[text()="Nearest LDAP server URL"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Nearest_LDAP_server_URL)

    # For the "Secondary LDAP server URL" parameter, enter the Secondary LDAP server URL
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="URLs Editor"]/following::span[text()="Secondary LDAP server URL"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Secondary_LDAP_server_URL)

    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Save"]')))
    elem.click()

    # Wait for 2 seconds to make sure the popup dialog to disappear
    time.sleep(2)

    # In "Settings" area, click the "Edit" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Settings"]/ancestor::div[@class="framedBox"][1]//span[text()="Edit"]')))
    elem.click()

    # In the "Settings Editor" popup, for the "Distinguished name of the service account" parameter, enter the account
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Settings Editor"]/following::span[text()="Distinguished name of the service account"]/following::input[1]')))
    elem.clear()
    elem.click()
    elem.send_keys(Service_account_name)

    # For the "Password" parameter, enter the password
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Settings Editor"]/following::span[text()="Password"]/following::input[1]')))
    elem.clear()
    elem.click()
    elem.send_keys(Password)

    # For the "Confirm Password" parameter, enter the password again
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Settings Editor"]/following::span[text()="Confirm Password"]/following::input[1]')))
    elem.clear()
    elem.click()
    elem.send_keys(Password)

    # For the "LDAP query suffix" parameter, enter the suffix string
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Settings Editor"]/following::span[text()="LDAP query suffix"]/following::input[1]')))
    elem.clear()
    elem.send_keys(LDAP_query_suffix)

    # For the "The scope(s) to search for groups" parameter, enter the scope for group string
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Settings Editor"]/following::span[text()="The scope(s) to search for groups"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Scope_for_groups)

    # For the "The second group namespace" parameter, enter the second scope for group string
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Settings Editor"]/following::span[text()="The second group namespace"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Second_group_namespace)

    # For the "The LDAP context for user searching" parameter, enter the LDAP context string
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Settings Editor"]/following::span[text()="The LDAP context for user searching"]/following::input[1]')))
    elem.clear()
    elem.send_keys(LDAP_context)

    # For the "Maximum level of group nesting" parameter, enter the maximum level of group nesting
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Settings Editor"]/following::span[text()="Maximum level of group nesting"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Maximum_group_nesting)

    # Click the "Save" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Save"][@type="submit"]')))
    elem.click()