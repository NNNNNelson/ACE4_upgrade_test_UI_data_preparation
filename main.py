from selenium import webdriver
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from steps import login
from steps import create_WMI_WinRM_agents
from steps import create_a_new_user
from steps import modify_LDAP_settings
from steps import modify_agent_private_asp
from steps import modify_agent_all_asp
from steps import add_tag_to_an_agent
from steps import add_blackout_for_an_agent
from steps import create_a_scheduled_report
from steps import create_a_simple_rule
from steps import create_a_multiple_rule
from steps import modify_email_settings
from steps import enable_a_rule_and_disable_a_rule
from steps import modify_the_test_multiple_rule
from steps import modify_a_rule_threshold
from steps import create_a_registry_variable
from steps import script_to_create_10_alarms_and_acknowledge_5_of_them
from steps import modify_a_retention_policy
from steps import create_a_derived_metric
from steps import modify_a_derived_metric
from steps import create_a_schedule
from steps import modify_a_schedule
from steps import create_several_levels_of_service
from steps import create_a_support_bundle
from steps import create_an_user_defined_dashboard
from steps import modify_service_operation_console
from steps import disable_2_cartridges

# Prepare some environment parameters
# WMI machine information
WMI_machine_IP = '10.30.152.104'
WMI_machine_username = 'administrator'
WMI_machine_password = 'Rdis2fun'
# WinRM machine informaiton
WinRM_machine_IP = '10.30.152.109'
WinRM_machine_username = 'administrator'
WinRM_machine_password = 'Rdis2fun'
# New create user informaiton
new_create_user_username = 'testnewuser'
new_create_user_password = 'Rdis2fun!'


# This is for test, when real using, delete below lines
FMS_server_ip = '10.30.168.239'

# # Expect when executing py file, there will be a parameter to indicate the FMS IP.
# # If there's no parameter, will prompt user to enter a FMS IP
# # If there's no user input, directly exit the py file executing
# if len(sys.argv) == 1:
#     print('You need to enter the FMS server IP: ')
#     FMS_server_ip = input()
#     if FMS_server_ip == '':
#         sys.exit('No Server IP, can\'t start auto test.')
# else:
#     FMS_server_ip = sys.argv[1]

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# Login FMS
login.login(driver, wait, FMS_server_ip)

# # Create "Monitor_WMI" agent
# create_WMI_WinRM_agents.monitor_WMI(driver, wait, FMS_server_ip, WMI_machine_IP, WMI_machine_username, WMI_machine_password)
#
# # Create "Monitor_WinRM" agent
# create_WMI_WinRM_agents.monitor_WinRM(driver, wait, FMS_server_ip, WinRM_machine_IP, WinRM_machine_username, WinRM_machine_password)
#
# # Create a new user "testnewuser" with password "Rdis2fun!"
# create_a_new_user.create_a_new_user(driver, wait, FMS_server_ip, new_create_user_username, new_create_user_password)
#
# # Modify LDAP settings
# modify_LDAP_settings.modify_LDAP_settings(driver, wait, FMS_server_ip)
#
# # Modify an agent's private asp
# modify_agent_private_asp.modify_agent_private_asp(driver, wait, FMS_server_ip)
#
# # Modify an agent's all asp
# modify_agent_all_asp.modify_agent_all_asp(driver, wait, FMS_server_ip)
#
# # Add a tag "testTag" to agent "Monitor_WMI"
# add_tag_to_an_agent.add_tag_to_an_agent(driver, wait, FMS_server_ip)
#
# # Add a blackout to suspend agent "Monitor_WMI" from collecting data in 1st day of month
# add_blackout_for_an_agent.add_blackout_for_an_agent(driver, wait, FMS_server_ip)
#
# # Create a "Hourly" scheduled report named "testScheduledReport" which uses template of "Agent Properties Report"
# create_a_scheduled_report.create_a_scheduled_report(driver, wait, FMS_server_ip)
#
# # Create a simple rule name "testSimpleRule" to send mail to "nelson.wang@quest.com"
# create_a_simple_rule.create_a_simple_rule(driver, wait, FMS_server_ip)
#
# # Create a multiple rule name "testMultipleRule" to send mail to "nelson.wang@quest.com"
# create_a_multiple_rule.create_a_multiple_rule(driver, wait, FMS_server_ip)
#
# # Modify email configuration to make FMS be able to send mail
# modify_email_settings.modify_email_settings(driver, wait, FMS_server_ip)
#
# # Enable a rule, and disable a rule
# # Enable a rule
# enable_a_rule_and_disable_a_rule.enable_a_rule(driver, wait, FMS_server_ip)
# # Disable a rule
# enable_a_rule_and_disable_a_rule.disable_a_rule(driver, wait, FMS_server_ip)
#
# # Modify the rule "testMultipleRule"
# modify_the_test_multiple_rule.modify_the_test_multiple_rule(driver, wait, FMS_server_ip)
#
# # Modify a rule's threshold
# modify_a_rule_threshold.modify_a_rule_threshold(driver, wait, FMS_server_ip)
#
# # Create a registry variable
# create_a_registry_variable.create_a_registry_variable(driver, wait, FMS_server_ip)
#
# # Run script to create 10 alarms
# script_to_create_10_alarms_and_acknowledge_5_of_them.script_to_create_10_alarms(driver, wait, FMS_server_ip)
#
# # In "Alarms" dashboard, pick the first 5 alarms to Acknowledge
# script_to_create_10_alarms_and_acknowledge_5_of_them.acknowledge_first_5_alarms(driver, wait, FMS_server_ip)
#
# # Modify a retention policy
# modify_a_retention_policy.modify_a_retention_policy(driver, wait, FMS_server_ip)
#
# # Create a derived metric
# create_a_derived_metric.create_a_derived_metric(driver, wait, FMS_server_ip)
#
# # Modify an existed derived metric description
# modify_a_derived_metric.modify_a_derived_metric(driver, wait, FMS_server_ip)
#
# # Create a schedule
# create_a_schedule.create_a_schedule(driver, wait, FMS_server_ip)
#
# # Modify a schedule
# modify_a_schedule.modify_a_schedule(driver, wait, FMS_server_ip)
#
# # Create several levels service
# create_several_levels_of_service.create_several_levels_of_service(driver, wait, FMS_server_ip)
#
# # Create a Management Server support bundle
# create_a_support_bundle.create_a_management_server_support_bundle(driver, wait, FMS_server_ip)
#
# # Create an user defined dashboard
# create_an_user_defined_dashboard.create_an_user_defined_dashboard(driver, wait, FMS_server_ip)
#
# # Modify Service Operations Console
# modify_service_operation_console.modify_service_operation_console(driver, wait, FMS_server_ip)

# Disable 2 cartridges
disable_2_cartridges.disable_2_cartridges(driver, wait, FMS_server_ip)