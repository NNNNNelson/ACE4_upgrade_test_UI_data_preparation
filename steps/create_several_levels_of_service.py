'''
Create Services
    testServiceCategory1
    This is test service category 1
        testServiceChildGlobalService1
        This is test child global service 1
            testServiceChildLocalService2
            This is test child local service 2
        testServiceChildLocalService3
        This is test child local service 3
            testServiceChildGlobalService4
            This is test child global service 4

In Service4, add component, choose the 1st agent
'''

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Service_category_name = 'testServiceCategory'
Service_category_description = 'This is test service category'
Child_service_name_1 = 'testServiceChildGlobalService1'
Child_service_description_1 = 'This is test child global service 1'
Child_service_name_2 = 'testServiceChildLocalService2'
Child_service_description_2 = 'This is test child local service 2'
Child_service_name_3 = 'testServiceChildLocalService3'
Child_service_description_3 = 'This is test child local service 3'
Child_service_name_4 = 'testServiceChildGlobalService4'
Child_service_description_4 = 'This is test child global service 4'

# Create several levels service
def create_several_levels_of_service(driver, wait, FMS_server_ip):
    # Go to "Service Builder" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:foglight_services.serviceBuilderContainer')

    # Add testServiceCategory
    # Click the "Add A New Category" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Add A New Category"]')))
    elem.click()
    # In the new prompt "New Category Wizard" popup, for "Name" input, enter Service_category_name value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[@class="summaryTitle"]/following::span[text()="Name"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Service_category_name)
    # For the "Short Description" textarea, enter Service_category_description value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[@class="summaryTitle"]/following::span[text()="Short Description"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Service_category_description)
    # For the "Description" textarea, enter Service_category_description value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[@class="summaryTitle"]/following::span[text()="Description"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Service_category_description)
    # Click the enabled "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="button"][@value="Finish"][@name="finish"][not(@disabled)]')))
    elem.click()

    # Add testServiceChildGlobalService1
    # Click the "+" button of testServiceCategory row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="testServiceCategory (FSMCategory)"]/following::img[contains(@src, "add")][1]')))
    elem.click()
    # In the popup, click "Create a child service"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Create a child service"]')))
    elem.click()
    # In the popup, click "New Global Service"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="New Global Service"]')))
    elem.click()
    # In the new prompt "New Global Service" popup, for "Name" input, enter Child_service_name_1 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Name"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Child_service_name_1)
    # For the "Short Description" textarea, enter Child_service_description_1 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Short Description"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Child_service_description_1)
    # For the "Description" textarea, enter Child_service_description_1 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Description"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Child_service_description_1)
    # Click the enabled "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@value="Finish"][@name="finish"][not(@disabled)]')))
    elem.click()

    # Add testServiceChildLocalService2
    # Click the expand icon before "testServiceCategory" row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="testServiceCategory (FSMCategory)"]/preceding::img[contains(@src, "expand")][1]')))
    elem.click()
    # Click the "+" button of testServiceChildGlobalService1 row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="testServiceChildGlobalService1 (FSMService)"]/following::img[contains(@src, "add")][1]')))
    elem.click()
    # In the popup, click "Create a child service"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Create a child service"]')))
    elem.click()
    # In the popup, click "New Local Service"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="New Local Service"]')))
    elem.click()
    # In the new prompt "New Service FortestServiceChildGlobalService1" popup, for "Name" input, enter Child_service_name_2 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Name"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Child_service_name_2)
    # For the "Short Description" textarea, enter Child_service_description_2 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Short Description"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Child_service_description_2)
    # For the "Description" textarea, enter Child_service_description_2 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Description"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Child_service_description_2)
    # Click the enabled "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@value="Finish"][@name="finish"][not(@disabled)]')))
    elem.click()

    # Add testServiceChildLocalService3
    # Click the "+" button of testServiceCategory row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="testServiceCategory (FSMCategory)"]/following::img[contains(@src, "add")][1]')))
    elem.click()
    # In the popup, click "Create a child service"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Create a child service"]')))
    elem.click()
    # In the popup, click "New Local Service"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="New Local Service"]')))
    elem.click()
    # In the new prompt "New Service For testServiceCategory" popup, for "Name" input, enter Child_service_name_3 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Name"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Child_service_name_3)
    # For the "Short Description" textarea, enter Child_service_description_3 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Short Description"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Child_service_description_3)
    # For the "Description" textarea, enter Child_service_description_3 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Description"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Child_service_description_3)
    # Click the enabled "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@value="Finish"][@name="finish"][not(@disabled)]')))
    elem.click()

    # Add testServiceChildGlobalService4
    # Click the expand icon before "testServiceCategory" row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="testServiceCategory (FSMCategory)"]/preceding::img[contains(@src, "expand")][1]')))
    elem.click()
    # Click the "+" button of testServiceChildLocalService3 row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="testServiceChildLocalService3 (FSMChildService)"]/following::img[contains(@src, "add")][1]')))
    elem.click()
    # In the popup, click "Create a child service"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Create a child service"]')))
    elem.click()
    # In the popup, click "New Global Service"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="New Global Service"]')))
    elem.click()
    # In the new prompt "New Global Service" popup, for "Name" input, enter Child_service_name_4 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Name"]/following::input[1]')))
    elem.clear()
    elem.send_keys(Child_service_name_4)
    # For the "Short Description" textarea, enter Child_service_description_4 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Short Description"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Child_service_description_4)
    # For the "Description" textarea, enter Child_service_description_4 value
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Description"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Child_service_description_4)
    # Click the enabled "Finish" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//input[@type="button"][@value="Finish"][@name="finish"][not(@disabled)]')))
    elem.click()

    # Add component to testServiceChildGlobalService2
    # Go to "Service Builder" dashboard again to make sure all nodes are collapsed
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:foglight_services.serviceBuilderContainer')
    # Expand "testServiceCategory", then expand "testServiceChildLocalService3"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="testServiceCategory (FSMCategory)"]/preceding::img[contains(@src, "expand")][1]')))
    elem.click()
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="testServiceChildGlobalService1 (FSMService)"]/preceding::img[contains(@src, "expand")][1]')))
    elem.click()
    # Click the "+" button of testServiceChildGlobalService2 row
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="testServiceChildLocalService2 (FSMChildService)"]/following::img[contains(@src, "add")][1]')))
    elem.click()
    # In the popup, click "Add components to this service"
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Add components to this service"]')))
    elem.click()
    # In the new prompt "Add components to this service" popup, click the "Add specific component" option
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//a[text()="Add specific component"]')))
    elem.click()
    # In the new prompt "Add specific components" popup, choose the 1st item in table by click its checkbox
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '(//div[@id="prmPopupContainer"]//input[@type="checkbox"])[1]')))
    elem.click()
    # Click the "Add Components" button to complete
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//button[text()="Add Components"]')))
    elem.click()