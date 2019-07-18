import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


Script_name = 'Script to create 200 alarms'
Script_of_creating_200_alarms = '''\
import com.quest.nitro.service.util.JDBCHelper;
import groovy.sql.Sql;
def allRules = server.RuleService.getAllRules();
def allObjects = [];
allObjects.addAll(server.QueryService.queryTopologyObjects("Host"));
//allObjects.addAll(server.QueryService.queryTopologyObjects("TopologyObject"));
def int num = 200;  //replace this num to what you want
def ran = new Random();
def alarmSvc = server.AlarmService;
def topSvc = server.TopologyService;
while(num > 0){
def rule = allRules[ran.nextInt(allRules.size())];
def topObj = allObjects[ran.nextInt(allObjects.size())];
def severity = ran.nextInt(3) + 2;
severity = (severity % 3) + 2;
alarmSvc.reportAlarm("SourceID"+num , severity, topObj.uniqueId,"This is alarm number " + num + ". Object = " + topSvc.getDisplayableName(topObj, true),rule.getName(),rule.id);
num --;
}
def sql = new Sql(JDBCHelper.getDataSource(null));
def numAlarms = sql.firstRow("select count(*) from alarm_alarm")[0];
return "Number of current alarms: " + alarmSvc.getCurrentAlarms().size() + "; Number of alarms in the database: " + numAlarms;\
'''

# Run script to create 10 alarms
def script_to_create_10_alarms(driver, wait, FMS_server_ip):
    # Go to "Manage Registry Variables" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:administration_tooling_script20editor.groovyScriptConsole')
    # Switch to "Scripts" tab
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Scripts"]')))
    elem.click()
    # Wait for the "Import Scripts" to appear
    wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Import Scripts"]')))
    # Click the "Add" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Add"]')))
    elem.click()
    # In the new prompt "Run Script" popup, for the "Name:" input, enter
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[text()="Name:"]/following::input[@type="text"][1]')))
    elem.clear()
    elem.send_keys(Script_name)
    # For the "Enter Script Text", enter script to run to generate 10 alarms
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//span[text()="Enter Script Text:"]/following::textarea[1]')))
    elem.clear()
    elem.send_keys(Script_of_creating_200_alarms)
    # Click the "Run" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//button[@type="submit"][text()="Run"]')))
    elem.click()
    # When the "Script Output" contains string "Number of current alarms", click the "Save" button, then click the "Cancel" button
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="prmPopupContainer"]//div[contains(@class, "componentBody")][contains(text(), "Number of current alarms")]')))
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"][text()="Save"]')))
    elem.click()
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="button"][text()="Cancel"]')))
    elem.click()

# In "Alarms" dashboard, pick the first 5 alarms to Acknowledge
def acknowledge_first_5_alarms(driver, wait, FMS_server_ip):
    # Go to "Alarms" dashboard
    driver.get('http://' + FMS_server_ip + ':8080/console/page/system:core_alarms.alarmsMain')
    # Click the first 5 alarms' checkbox
    for i in range(2, 7):
        elem = wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@type="checkbox"])[' + str(i) + ']')))
        elem.click()
    # Click the "Acknowledge" button
    elem = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Acknowledge"]')))
    elem.click()
