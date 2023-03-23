import time
import datetime
from datetime import timedelta
import json
import uweCCWebbotAddTrip
import keyboard
import uweCCWebbot
from inputimeout import inputimeout


weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

menuDates = []
menuDatesFile = []



def checkNewDates():
    now = datetime.datetime.now()
    x=1
    with open('sample.txt', 'a') as f:
        while x <= 21:
            tempDate = now + timedelta(days= x)
            print(tempDate.weekday())
            if tempDate.weekday() == 6 or tempDate.weekday() == 2:
                if str(tempDate.strftime("%d/%m/%Y")) in open('sample.txt').read():
                    print("Already in file")
                else:
                    tempDict = {'date': str(tempDate.strftime("%d/%m/%Y")), 'tripCreated': 0, 'tripName': '', 'shortTripName': '', 'submitDate': '', 'submitted': 0}
                    f.write(str(tempDict) + '\n')
                # menuDates.append(datetime.datetime.combine(tempDate, datetime.datetime.min.time()))
            x += 1



# d = {'0':menuDates[0]}
     


# with open('sample.txt', 'a') as f:
#     for dates in menuDates:
#         tempDict = {f'date': {dates}}
#         if str(tempDict) in open('sample.txt').read():
#             print("Already in file")
#         else:
#             f.write(str(tempDict) + '\n')    


def loopSubmit():
    y = 0
    trips = []
    with open('sample.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    for line in data:
        
        d = eval(line.strip())
        s = [y,d]
        trips.append(s)
        print(s)
        y += 1

    while True:
        now = datetime.datetime.now()
        if keyboard.is_pressed("q"):
            print("q pressed, ending loop")
            time.sleep(1)
            break

        for trip in trips:
            time.sleep(1)
            if trip[1]['submitted'] == 0:
                print(trip)
                if trip[1]['submitDate'] != "" and trip[1]:
                    tempDate = datetime.datetime.strptime(trip[1]['submitDate'], r'%d/%m/%Y')
                    nowTempDate = datetime.datetime.combine(now, datetime.datetime.min.time())
                    if tempDate == nowTempDate:
                        print(f"{now.hour}:{now.minute}")
                        if now.hour >= 12 and now.minute >= 0:
                            print("well hello")
                            tripDate = datetime.datetime.strptime(trip[1]['date'], r'%d/%m/%Y')
                            uweCCWebbot.test_eight_components(trip[1]['tripName'], tripDate.strftime(r'%Y/%m/%d'),trip[1]['shortTripName'])
                            lineNum = trip[0]
                            trip[1]['submitted'] = 1
                            data[lineNum] = str(trip[1]) + '\n'
                            with open('sample.txt', 'w') as f:
                                f.writelines(data)

                            #add code to call uweCCWebbot to submit trip sheet
                            break
                # if tempDate == 

def newTrip():
    y = 0
    with open('sample.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    for line in data:
        
        d = eval(line.strip())
        s = [y,d]
        menuDatesFile.append(s)
        print(s)
        y += 1


    print("")
    for dates in menuDatesFile:
            print(str(dates[0]) + ". ",end="")
            tempDate0 = datetime.datetime.strptime(dates[1]['date'], r'%d/%m/%Y')
            print(f"{weekDays[ tempDate0.weekday()]} {tempDate0.strftime(r'%d/%m/%Y')} Trip Created: {dates[1]['tripCreated']}")
    print("")

    lineNum = int(input("Please select a Date: "))
    tripDetails = menuDatesFile[lineNum]


    signupDate = uweCCWebbotAddTrip.test_eight_components(tripDetails[1]['date'])
    #signupDate = datetime.datetime.now()
    tripDetails[1]['submitDate'] = signupDate[0].strftime("%d/%m/%Y")
    tripDetails[1]['tripName'] = signupDate[1]
    tripDetails[1]['shortTripName'] = signupDate[2]
    tripDetails[1]['tripCreated'] = 1
    print(tripDetails)
    data[lineNum] = str(tripDetails[1]) + '\n'
    print(data)
    with open('sample.txt', 'w') as f:
        f.writelines(data)


def menu():
    print("Menu:")
    print("0. Check time for participant list upload")
    print("1. Upload new trip")
    try:
        inputUser = int(inputimeout(prompt='Please select a number: ', timeout=30))
    except:
        loopSubmit()
        print("outOfTime")

    if inputUser == 0:
        loopSubmit()
    elif inputUser == 1:
        checkNewDates()
        newTrip()
    else:
        print("error: incorrect value")
        menu()
while True:
    menu()
# loopSubmit()
input("")
