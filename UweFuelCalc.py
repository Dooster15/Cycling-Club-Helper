x = 0
Dprice = 1.69
Pprice = 1.49
gallonsToLiters = 0.219
muitiplier = 1.2
totalCost = 0
import math
#make a optimal calculator
cars = [
    {"name" : "Jack", "mpg" : 40 , "fuelType" : 'd', "capBikes" : 9, "capPeople" : 3, "costPerMile" : 0},
    {"name" : "AlexV1", "mpg" : 45 , "fuelType" : 'd', "capBikes" : 5, "capPeople" : 2, "costPerMile" : 0},
    #{"name" : "AlexV2", "mpg" : 50 , "fuelType" : 'd', "capBikes" : 3, "capPeople" : 5, "costPerMile" : 0},
    {"name" : "MattyV1", "mpg" : 30 , "fuelType" : 'p', "capBikes" : 2, "capPeople" : 1, "costPerMile" : 0},
    #{"name" : "MattyV2", "mpg" : 30 , "fuelType" : 'p', "capBikes" : 0, "capPeople" : 5, "costPerMile" : 0},
    {"name" : "Isaac", "mpg" : 40 , "fuelType" : 'p', "capBikes" : 3, "capPeople" : 5, "costPerMile" : 0},
    {"name" : "Anais", "mpg" : 38 , "fuelType" : 'p', "capBikes" : 0, "capPeople" : 5, "costPerMile" : 0},
    {"name" : "Patsy", "mpg" : 40 , "fuelType" : 'p', "capBikes" : 0, "capPeople" : 5, "costPerMile" : 0},
    {"name" : "Toby", "mpg" : 56 , "fuelType" : 'p', "capBikes" : 2, "capPeople" : 2, "costPerMile" : 0},
]
carsTaken = []
print("Please Enter the amount of people paying: ")
numberOfPeople = int(input())
print("Please select which cars you are taking.")

for car in cars:
    if car["fuelType"] == 'p':
        car["costPerMile"] = (1 / (cars[x]["mpg"] * gallonsToLiters)) * Pprice
    else:
        car["costPerMile"] = (1 / (cars[x]["mpg"] * gallonsToLiters)) * Dprice
    
    print(str(x) + ". ",end="")
    print(str(car["name"])+" " + str(car["costPerMile"]) )
    x += 1

while True:
    print("Select a car:")
    car = int(input())
    if car in carsTaken:
        print("Already Added")
        continue 
    carsTaken.append(car)
    inputX = input("Another car?[y,n]")
    if inputX == "n":
        break
milesDriven = int(input("Please Enter miles driven: "))
for carsT in carsTaken:
    if cars[carsT]["fuelType"] == 'p':
        Cost = ((milesDriven/(cars[carsT]["mpg"]*gallonsToLiters)*Pprice)*muitiplier)
    else:
        Cost = ((milesDriven/(cars[carsT]["mpg"]*gallonsToLiters)*Dprice)*muitiplier)
    
    coSt = (math.ceil(Cost *100)/100)
    totalCost = totalCost + coSt
    cost = format(coSt, ".2f")
    print(f"{cars[carsT]['name']} £{cost}")

costPerPerson = totalCost / numberOfPeople
costPerPerson = (math.ceil(costPerPerson *100)/100)
costPerPerson = format(costPerPerson, ".2f")
print(costPerPerson)