from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
from datetime import timedelta
from fields import *
from locations import *
import os
PATH = "C:\Program Files (x86)\chromedriver.exe"



def test_eight_components(tripDate):
    
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.thestudentsunion.co.uk/login/")

    now1 = datetime.datetime.now()
    parent_dir = "C:/Users/doost/OneDrive/Documents/Code/CyclingClub/screenshots/"
    
    
    
    count = 0

    # title = driver.title
    # assert title == "Web form"
    driver.implicitly_wait(1.0)

    

    #tripDate = input("Enter date of trip (DD/MM/YYYY): ")

    day, month, year = (int(x) for x in tripDate.split('/')) 
    ans = datetime.date(year, month, day)
    weekDay = ans.weekday()
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    print(ans.weekday())

    if weekDay == 2:
        departureTime = input("Enter time of departure (HH:MM): Press enter for 12:30 ") or "12:30"
        returnTime = input("Enter time of leaving venue (HH:MM): Press enter for 19:00 ") or "19:00"
    elif weekDay == 6:
        departureTime = input("Enter time of departure (HH:MM): Press enter for 10:00 ") or "10:00"
        returnTime = input("Enter time of leaving venue (HH:MM): Press enter for 16:00 ") or "16:00"
    else:
        departureTime = input("Enter time of departure (HH:MM): ")
        returnTime = input("Enter time of leaving venue (HH:MM): ")

    
    
    
    x = 0
    for address in addresses:

        print(str(x) + ". ",end="")
        print(str(address["name"]))
        x += 1
    
    addressLocation = addresses[int(input("Please select a location: "))]

    directory = f"{addressLocation['nameShort']}-{ans.day}.{ans.month}.{ans.year}" 
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
    except:
        pass

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1
    
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
    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1
    try:
        btnCancel = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnCancel']")
        btnCancel.click()
        driver.switch_to.alert.accept()
        time.sleep(3)
    except NoSuchElementException:
        print("Location check correct")
        pass
    
    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    #input("Please check the page is reset properly and then press enter: ")

    btnStart = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnResubmit']")
    btnStart.click()

    btnTripType = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_2739_radioList_2']")
    btnTripType.click()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    btnTripDays = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1350_radioList_0']")
    btnTripDays.click()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1
    
    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()
    
    boxName = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1354_txtTextbox']")
    boxName.send_keys(name)

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1
    
    boxPhoneNumber = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1356_txtTextbox']")
    boxPhoneNumber.send_keys(phone)

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    boxEmail = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1355_txtTextbox']")
    boxEmail.send_keys(email)

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    # tripDate = input("Enter date of trip (DD/MM/YYYY): ")

    boxDate = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1352_txtTextbox']")
    boxDate.send_keys(tripDate)

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    # departureTime = input("Enter time of departure (HH:MM): ")

    boxDepartTime = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1357_txtTextbox']")
    boxDepartTime.send_keys(departureTime)

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    # returnTime = input("Enter time of leaving venue (HH:MM): ")

    boxReturnTime = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1358_txtTextbox']")
    boxReturnTime.send_keys(returnTime)

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    # print("")
    # x = 0
    # for address in addresses:

    #     print(str(x) + ". ",end="")
    #     print(str(address["name"]))
    #     x += 1
    
    # addressLocation = addresses[int(input("Please select a location: "))]

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

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    boxCountry = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1351_ddCountry']/option[2]")
    boxCountry.click()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    boxSport = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1372_dd']/option[143]")
    boxSport.click()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    boxDescription = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_5019_txtTextbox']")
    boxDescription.send_keys(f"MTB - Trip to {addressLocation['nameShort']}")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

# add wednesday or sunday support
    boxTitle = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1373_txtTextbox']")
    boxTitle.send_keys(f"MTB - Trip to {addressLocation['nameShort']} on {tripDate[:5]}")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    boxFirstAider1 = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1370_txtTextbox']")
    boxFirstAider1.send_keys("Jack Holdsworth")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    boxFirstAider2 = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1371_txtTextbox']")
    boxFirstAider2.send_keys("Jesse Lawson")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    boxEquipment= driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1369_txtTextbox']")
    boxEquipment.send_keys("1 x 4 bike rack")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    boxNightAccess= driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_3654_txtTextbox']")
    boxNightAccess.send_keys("no")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()
    
    boxRiskAssessment = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1474_dd']/option[2]")
    boxRiskAssessment.click()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    boxDriverQuestion = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1482_dd']/option[4]")
    boxDriverQuestion.click()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    boxTravelDescription= driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1453_txtTextbox']")
    boxTravelDescription.send_keys("Personal Vehicles")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    boxRiskAssessmentQuestion = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_question_1454_dd']/option[2]")
    boxRiskAssessmentQuestion.click()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    btnNext = driver.find_element(By.XPATH, "//*[@id='ctl00_survey1_btnNext']")
    btnNext.click()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    input("")

    driver.get("https://www.thestudentsunion.co.uk/organisation/admin/signups/edit/6198/")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    
    

    title = f"MTB - {weekDays[weekDay]} at {addressLocation['nameShort']} {ans.day:02d}/{ans.month:02d}"
    shortTile = f"MTB - {weekDays[weekDay]} at {addressLocation['nameShort']}"

    signupEventName= driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_txtName_txtTextbox']")
    signupEventName.send_keys(title)

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    signupEventDate= driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_datesEvent_txtFromDate']")
    signupEventDate.send_keys(tripDate)

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    signupEventTime= driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_datesEvent_txtFromTime']")
    if weekDay == 2:
        signupEventTime.send_keys("12:30")
        driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
        count += 1
    elif weekDay == 6:
        signupEventTime.send_keys("10:00")
        driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
        count += 1
    else:
        input("There has been an error on Signups event time")

    signupEventDateEnd= driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_datesEvent_txtToDate']")
    signupEventDateEnd.send_keys(tripDate)

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    signupEventTimeEnd= driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_datesEvent_txtToTime']")
    signupEventTimeEnd.send_keys("19:00")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    now = datetime.datetime.now()

    signupSignupTime= driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_datesSignup_txtFromDate']")
    signupSignupTime.send_keys(f"{now.day:02d}/{now.month:02d}/{now.year}")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    signupSignupTimeTime= driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_datesSignup_txtFromTime']")
    signupSignupTimeTime.send_keys(f"{now.hour:02d}:{now.minute:02d}")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    signupSignupTimeEnd= driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_datesSignup_txtToDate']")

    signupSignupTimeTimeEnd= driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_datesSignup_txtToTime']")

    if weekDay == 2:
        signupDate = datetime.datetime.strptime(tripDate, r'%d/%m/%Y') - timedelta(days=2)
        signupSignupTimeEnd.send_keys(f"{signupDate.day:02d}/{signupDate.month:02d}/{signupDate.year}")
        signupSignupTimeTimeEnd.send_keys("12:00")
        driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
        count += 1
    elif weekDay == 6:
        signupDate = datetime.datetime.strptime(tripDate, r'%d/%m/%Y') - timedelta(days=3)
        signupSignupTimeEnd.send_keys(f"{signupDate.day:02d}/{signupDate.month:02d}/{signupDate.year}")
        signupSignupTimeTimeEnd.send_keys("12:00")
        driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
        count += 1
    else:
        input("There has been an error on Signups event time 2 ")

    btnSubmit = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_fsUpdate_btnSubmit']")
    btnSubmit.click()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    numberOfRows = -1
    tableRows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_gvSignups']/tbody/tr")))

    for num,tableRow in enumerate(tableRows[1:],start = 2):
        rowName = tableRow.find_element(By.XPATH, ".//td[1]")
        print(f"{num}. {rowName.text}")
        if rowName.text == title:
            btnCopySheet = tableRow.find_element(By.XPATH, f"//*[@id='ctl00_ctl00_Main_AdminPageContent_gvSignups']/tbody/tr[{num}]/td[5]/a")
            btnCopySheet.click()
            break

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    signupEventName= driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_txtName_txtTextbox']")
    signupEventName.clear()

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    signupEventName.send_keys(f"Lifts: {title}")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    btnCapacity = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_numCapacity_txtTextbox']")
    btnCapacity.send_keys("3")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    btnReserved = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_numReserveCapacity_txtTextbox']")
    btnReserved.send_keys("10")

    driver.save_screenshot(f"screenshots/{directory}/screenshot_{count}.png")
    count += 1

    btnSubmit = driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_Main_AdminPageContent_fsUpdate_btnSubmit']")
    btnSubmit.click()
    

    input("Press any key to finish")
    return [signupDate,title,shortTile]
    


#test_eight_components()