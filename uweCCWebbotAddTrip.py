from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from fields import *
from locations import *

PATH = "C:\Program Files (x86)\chromedriver.exe"
attendingIDs = []


def test_eight_components():
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

    driver.get("https://www.thestudentsunion.co.uk/opportunities/howto/trip-form/")

    input("")

    btnStart = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnResubmit']")
    btnStart.click()

    btnTripType = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_2739_radioList_2']")
    btnTripType.click()

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    btnTripDays = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1350_radioList_0']")
    btnTripDays.click()
    
    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()
    
    boxName = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1354_txtTextbox']")
    boxName.send_keys(name)
    
    boxPhoneNumber = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1356_txtTextbox']")
    boxPhoneNumber.send_keys(phone)

    boxEmail = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1355_txtTextbox']")
    boxEmail.send_keys(email)

    tripDate = input("Enter date of trip (DD/MM/YYYY): ")

    boxDate = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1352_txtTextbox']")
    boxDate.send_keys(tripDate)

    boxDepartTime = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1357_txtTextbox']")
    boxDepartTime.send_keys(input("Enter time of departure (HH:MM): "))

    boxReturnTime = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1358_txtTextbox']")
    boxReturnTime.send_keys(input("Enter time of leaving venue (HH:MM): "))

    print("")
    x = 0
    for address in addresses:

        print(str(x) + ". ",end="")
        print(str(address["name"]))
        x += 1
    
    addressLocation = addresses[int(input("Please select a location: "))]

    boxLocationName = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1353_txtTextbox']")
    boxLocationName.send_keys(addressLocation['name'])

    boxLine1 = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1351_txtLine1']")
    boxLine1.send_keys(addressLocation['line1'])

    boxLine2 = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1351_txtLine2']")
    boxLine2.send_keys(addressLocation['line2'])

    boxLine3 = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1351_txtLine3']")
    boxLine3.send_keys(addressLocation['line3'])

    boxLine4 = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1351_txtLine4']")
    boxLine4.send_keys(addressLocation['line4'])

    boxPostCode = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1351_txtPostcode']")
    boxPostCode.send_keys(addressLocation['postCode'])

    boxCountry = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1351_ddCountry']/option[2]")
    boxCountry.click()

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    boxSport = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1372_dd']/option[143]")
    boxSport.click()

    boxDescription = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_5019_txtTextbox']")
    boxDescription.send_keys(f"MTB - Trip to {addressLocation['nameShort']}")

# add wednesday or sunday support
    boxTitle = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1373_txtTextbox']")
    boxTitle.send_keys(f"MTB - Trip to {addressLocation['nameShort']} on {tripDate[:4]}")

    boxFirstAider1 = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1370_txtTextbox']")
    boxFirstAider1.send_keys("Jack Holdsworth")

    boxFirstAider2 = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1371_txtTextbox']")
    boxFirstAider2.send_keys("Jesse Lawson")

    boxEquipment= driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1369_txtTextbox']")
    boxEquipment.send_keys("1 x 4 bike rack")

    boxNightAccess= driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_3654_txtTextbox']")
    boxNightAccess.send_keys("no")

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()
    
    boxRiskAssessment = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1474_dd']/option[2]")
    boxRiskAssessment.click()

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    boxDriverQuestion = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1482_dd']/option[4]")
    boxDriverQuestion.click()

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    boxTravelDescription= driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1453_txtTextbox']")
    boxTravelDescription.send_keys("Personal Vehicles")

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    boxRiskAssessmentQuestion = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1454_dd']/option[2]")
    boxRiskAssessmentQuestion.click()

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()



    

    


    input("")
    # numberOfRows = -1
    # tableRows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_gvSignups']/tbody/tr")))
    # for num,tableRow in enumerate(tableRows[1:],start = 2):
    #     name = tableRow.find_element(By.XPATH, ".//td[1]")
    #     print(f"{num}. {name.text}")
    #     # if "MTB" in name.text:
    #     #     print("Found")
    #     #     btnSignups = tableRow.find_element(By.XPATH, ".//td[4]/a")
    #     #     btnSignups.click()
    #     #     break
    # selectedSignup = input("Please enter a number: ")
    # btnSignups = tableRow.find_element(By.XPATH, f"//*[@id='ctl00_ctl00_Main_AdminPageContent_gvSignups']/tbody/tr[{selectedSignup}]/td[4]/a")
    # btnSignups.click()

    # tableSignupRows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='signup_list']/tbody/tr")))
    # for tableSignupRow in tableSignupRows[1:]:
    #     name = tableSignupRow.find_element(By.XPATH, ".//td[1]")
    #     if name.text == " ":
    #         continue
    #     else:
    #         attendingIDs.append(name.text)
    # # //*[@id="signup_list"]/tbody/tr[2]/td[1]
    
    # for attendingID in attendingIDs:
    #     print(attendingID)

    # driver.get("https://www.thestudentsunion.co.uk/organisation/editgroups/6198/")

    # btnCreateTrip = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_lbCreateNewGroup']")
    # btnCreateTrip.click()

    # dateOfTrip = input("Date Of Trip yyyy/mm/dd: ")
    # nameOfTrip = input("Enter Name of Trip: ")
    
    # txtBoxTitle = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_txtName_txtTextbox']")
    # txtBoxTitle.send_keys(f"{dateOfTrip} TRIP {nameOfTrip}")

    # btnSelectTrip = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_ddType_dd']/option[4]")
    # btnSelectTrip.click()

    # btnCreateTrip = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_fsNewGroup_btnSubmit']")
    # btnCreateTrip.click()

    
    # tableTripSheets = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_gvGroups']/tbody/tr")))
    # for tableTripSheet in tableTripSheets[1:]:
    #     name = tableTripSheet.find_element(By.XPATH, ".//td[1]")
    #     print(name.text)
    #     if name.text == f"{dateOfTrip} TRIP {nameOfTrip}":
    #         btnTripSheet = name.find_element(By.XPATH, ".//a")
    #         btnTripSheet.click()
    #         break

    # tableTripNames = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_gvPotentialMembers']/tbody/tr")))
    # for tableTripName in tableTripNames[1:]:
    #     id = tableTripName.find_element(By.XPATH, ".//td[3]")
    #     print(id.text)
    #     if id.text in attendingIDs:
    #         print("Match")
    #         btn = tableTripName.find_element(By.XPATH, ".//td[1]")
    #         btn.click()


    # btnAddMembers = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_btnAddMembers']")
    # btnAddMembers.click()
    
    #     # //*[@id="ctl00_ctl00_Main_AdminPageContent_gvPotentialMembers"]/tbody/tr[2]/td[3]
    #     # //*[@id="ctl00_ctl00_Main_AdminPageContent_gvPotentialMembers"]/tbody/tr[3]/td[1]
    #     # //*[@id="ctl00_ctl00_Main_AdminPageContent_gvPotentialMembers_ctl02_chkAdd"]
    #     # //*[@id="ctl00_ctl00_Main_AdminPageContent_gvPotentialMembers"]/tbody/tr[2]/td[3]
    #     # //*[@id="ctl00_ctl00_Main_AdminPageContent_gvGroups"]/tbody/tr[2]/td[1]/a
    # input("")
    # # element = driver.find_element(By.ID, "passwd-id")
    # # //*[@id="ctl00_ctl00_Main_AdminPageContent_gvGroups"]/tbody/tr[2]/td[1]/a
    


    # # text_box = driver.find_element(by=By.NAME, value="my-text")
    # # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # # text_box.send_keys("Selenium")
    # # submit_button.click()

    # # message = driver.find_element(by=By.ID, value="message")
    # # value = message.text
    # # assert value == "Received!"

    # # driver.quit()

test_eight_components()