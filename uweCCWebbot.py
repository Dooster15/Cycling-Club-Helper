from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
from datetime import timedelta
from fields import *

PATH = "C:\Program Files (x86)\chromedriver.exe"
attendingIDs = []


def test_eight_components(selectedSignup,dateOfTrip,nameOfTrip):
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.thestudentsunion.co.uk/login/")

    # title = driver.title
    # assert title == "Web form"
    driver.implicitly_wait(1.0)
    
    
    btnCurrentStudent = driver.find_element(By.XPATH, "//*[@id='skin_corners']/div[2]/div/div[2]/div[2]/div[4]")
    
    btnCurrentStudent.click()

    btnLogin = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl34_hlExtLogin']/center/span")
    btnLogin.click()

    inputUserName = driver.find_element(By.XPATH, "//*[@id='userNameInput']")
    inputUserName.send_keys(username)

    inputPassword = driver.find_element(By.XPATH, "//*[@id='passwordInput']")
    inputPassword.send_keys(password)

    btnSignin = driver.find_element(By.XPATH, "//*[@id='submitButton']")
    btnSignin.click()
    
    time.sleep(3)
    btnAcceptCookies = driver.find_element(By.XPATH, "//*[@id='msl']/div/div/a[1]")
    btnAcceptCookies.click()

    driver.get("https://www.thestudentsunion.co.uk/organisation/admin/signups/6198/")

    numberOfRows = -1
    tableRows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_gvSignups']/tbody/tr")))
    for num,tableRow in enumerate(tableRows[1:],start = 2):
        name = tableRow.find_element(By.XPATH, ".//td[1]")
        if name.text == selectedSignup:
            selectedSignup = num
        print(f"{num}. {name.text}")
        # if "MTB" in name.text:
        #     print("Found")
        #     btnSignups = tableRow.find_element(By.XPATH, ".//td[4]/a")
        #     btnSignups.click()
        #     break
        
    # selectedSignup = input("Please enter a number: ")
    # dateOfTrip = input("Date Of Trip yyyy/mm/dd: ")
    # nameOfTrip = input("Enter Name of Trip: ")


    btnSignups = tableRow.find_element(By.XPATH, f"//*[@id='ctl00_ctl00_Main_AdminPageContent_gvSignups']/tbody/tr[{selectedSignup}]/td[4]/a")
    btnSignups.click()

    tableSignupRows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='signup_list']/tbody/tr")))
    for tableSignupRow in tableSignupRows[1:]:
        name = tableSignupRow.find_element(By.XPATH, ".//td[1]")
        if name.text == " ":
            continue
        else:
            attendingIDs.append(name.text)
    # //*[@id="signup_list"]/tbody/tr[2]/td[1]
    
    for attendingID in attendingIDs:
        print(attendingID)

    driver.get("https://www.thestudentsunion.co.uk/organisation/editgroups/6198/")

    btnCreateTrip = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_lbCreateNewGroup']")
    btnCreateTrip.click()
    
    txtBoxTitle = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_txtName_txtTextbox']")
    txtBoxTitle.send_keys(f"{dateOfTrip} TRIP {nameOfTrip}")

    btnSelectTrip = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_ddType_dd']/option[4]")
    btnSelectTrip.click()

    btnCreateTrip = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_fsNewGroup_btnSubmit']")
    btnCreateTrip.click()

    
    tableTripSheets = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_gvGroups']/tbody/tr")))
    for tableTripSheet in tableTripSheets[1:]:
        name = tableTripSheet.find_element(By.XPATH, ".//td[1]")
        print(name.text)
        if name.text == f"{dateOfTrip} TRIP {nameOfTrip}":
            btnTripSheet = name.find_element(By.XPATH, ".//a")
            btnTripSheet.click()
            break

    tableTripNames = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_gvPotentialMembers']/tbody/tr")))
    for tableTripName in tableTripNames[1:]:
        id = tableTripName.find_element(By.XPATH, ".//td[3]")
        print(id.text)
        if id.text in attendingIDs:
            print("Match")
            btn = tableTripName.find_element(By.XPATH, ".//td[1]")
            btn.click()


    btnAddMembers = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_btnAddMembers']")
    btnAddMembers.click()
    

# test_eight_components()