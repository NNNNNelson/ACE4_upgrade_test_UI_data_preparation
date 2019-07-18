from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(driver, wait, FMS_server_ip):
    # Visit the FMS
    driver.get('http://' + FMS_server_ip + ':8080')

    # Login FMS
    elem = wait.until(EC.presence_of_element_located((By.ID, 'user')))
    elem.send_keys('foglight')
    elem = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    elem.send_keys('foglight')
    elem.submit()

    # Wait for login successfully to show the content page
    wait.until(EC.presence_of_element_located((By.ID, 'portalContents')))