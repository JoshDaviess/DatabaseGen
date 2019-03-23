from random import *
import math
import os
import string

def main(totalCount):
    masterCount = 1
    pubCount = 1
    totalPub = totalCount
    if os.path.exists("GeneratedSQL.sql") == True:
        os.remove("GeneratedSQL.sql")
    SQLFile = open("GeneratedSQL.sql", "w")
    print("DELETE FROM Coursework.Permanent;", file=SQLFile)
    print("DELETE FROM Coursework.Staff;", file=SQLFile)
    print("ALTER TABLE Coursework.Staff AUTO_INCREMENT = 1;", file = SQLFile)
    print("ALTER TABLE Coursework.Pub AUTO_INCREMENT = 1;", file = SQLFile)
    for j in range(totalCount):
        print("Pub Number " + str(pubCount))
        print('SELECT "Importing Pub Number ' + str(pubCount) + '" as "";', file = SQLFile)
        print("/* Pub Number " + str(pubCount) + " */", file=SQLFile)
        fields = StaffGen() + '\'Venue Manager\', NULL);'
        print(fields, file=SQLFile)
        print("/* Venue Manager ID is " + str(masterCount) + " */", file=SQLFile)
        print(PermanentGen(masterCount, "Venue"), file = SQLFile)
        print(pubGen(pubCount, masterCount), file = SQLFile)
        print("UPDATE Coursework.Staff SET staff_pub = " + str(pubCount) + " WHERE staff_ID = " + str(masterCount) + ";", file=SQLFile)
        masterCount = masterCount + 1
        for i in range(randint(3, 7)):
            fields = StaffGen() + '\'Bar Manager\', ' + str(pubCount) + ');'
            print(fields, file=SQLFile)
            print(PermanentGen(masterCount, "Bar"), file = SQLFile)
            masterCount = masterCount + 1
        for i in range(randint(5, 12)):
            fields = StaffGen() + '\'Chef\', ' + str(pubCount) + ');'
            print(fields, file=SQLFile)
            print(PermanentGen(masterCount, "Chef"), file = SQLFile)
            masterCount = masterCount + 1
        for i in range(randint(9, 12)):
            fields = StaffGen() + '\'Waiter\', ' + str(pubCount) + ');'
            print(fields, file=SQLFile)
            print(casualGen(masterCount), file=SQLFile)
            masterCount = masterCount + 1
        for i in range(randint(4, 14)):
            fields = StaffGen() + '\'Kitchen Porter\', '  + str(pubCount) + ');'
            print(fields, file=SQLFile)
            print(casualGen(masterCount), file=SQLFile)
            masterCount = masterCount + 1
        for i in range(randint(4, 14)):
            fields = StaffGen() + '\'Cleaner\', ' + str(pubCount) + ');'
            print(fields, file=SQLFile)
            print(casualGen(masterCount), file=SQLFile)
            masterCount = masterCount + 1
        pubCount = pubCount + 1
        print("\n", file = SQLFile)
    print('SELECT "Pubs and Staff Import Complete" as "";', file = SQLFile)
    print('SELECT "Begin import of food and drink" as "";', file = SQLFile)
    count = 1
    nonAlchFile = open("nonalch.txt", "r")
    drinks = nonAlchFile.read().splitlines()
    nonAlchFile.close()
    for i in range(len(drinks)):
        drink = drinks[i]
        details = drink.split(", ")
        name = details[0]
        price = details[1]
        desc = details[2]
        manu = details[3]
        cost = details[4]
        print('INSERT INTO Coursework.Item VALUES (NULL, ' + name + ", " + price + ", " + desc + ", " + manu + ", " + cost + ");", file=SQLFile)
        print('INSERT INTO Coursework.Drink VALUES (' + str(count) + ', NULL, "Non-Alch", ' + str(randint(30, 190)) + ");", file=SQLFile)
        count = count + 1
    print("\n", file = SQLFile)
    alchFile = open("alch.txt", "r")
    alchDrinks = alchFile.read().splitlines()
    alchFile.close()
    for i in range(len(alchDrinks)):
        alchDrink = alchDrinks[i]
        details = alchDrink.split(", ")
        name = details[0]
        price = details[1]
        desc = details[2]
        manu = details[3]
        cost = details[4]
        alch = details[5]
        print('INSERT INTO Coursework.Item VALUES (NULL, ' + name + ", " + price + ", " + desc + ", " + manu + ", " + cost + ");", file=SQLFile)
        print('INSERT INTO Coursework.Drink VALUES (' + str(count) + ', "' + alch + '", "Alch", ' + str(randint(30, 190)) + ");", file=SQLFile)
        count = count + 1
    print("\n", file = SQLFile)

def permSalary(low, high):
    salary = randint(low, high)
    salary = salary / 1000
    salary = round(salary, 1)
    salary = int(salary * 1000)
    return salary

def casualGen(idCount):
    rate = randint(6000, 8000)
    rate = rate / 1000
    rate = round(rate, 2)
    holiday = randint(1000, 15000)
    holiday = holiday / 1000
    holiday = round(holiday, 2)
    dates = startDate()
    starte = "'" + str(dates[2]) + "-" + str(dates[1]) + "-" + str(dates[0])
    return ("INSERT INTO Coursework.Casual VALUES (" + str(idCount) + ", " + str(randint(10,26)) + ", " + str(rate) + ", " + str(holiday) + ", " + starte + "', " + endDate(dates[0], dates[1], dates[2]) + ");")

def PermanentGen(idCount, Employ):
    pension = ["'State Pension', ", "'Private Pension', ", "'Peoples Pension', ", "NULL, ",  "'Private Pension', "]
    if Employ == "Venue":
        sal = permSalary(30000, 45000)
    elif Employ == "Bar":
        sal = permSalary(22000, 30000)
    elif Employ == "Chef":
        sal = permSalary(14000, 21000)
    dates = startDate()
    starte = "'" + str(dates[2]) + "-" + str(dates[1]) + "-" + str(dates[0])
    return("INSERT INTO Coursework.Permanent VALUES (" + str(idCount) + ", " + str(sal) + ", " + str(randint(7, 26)) + ", " + pension[randint(0, 4)] + starte + "');")

def startDate():
    day = randint(1,28)
    month = randint(1, 12)
    year = randint(2000, 2018)
    return(day, month, year)
    # return("'" + str(year) + "-" + str(month) + "-" + str(day))

def endDate(day, month, year):
    day = randint(day,28)
    month = randint(month, 12)
    year = randint(year, 2021)
    if randint(1,10) > 8:
        return("'" + str(year) + "-" + str(month) + "-" + str(day) + "'")
    else:
        return("NULL")

def StaffGen():
    fname =  firstName()
    lname = lastName()
    address = '\'' + str(randint(1, 200)) + " " + addresses() + '\', '
    postcode = '\'' + postcodes() + str(randint(1, 20)) + " " + str(randint(0, 9)) + choice(string.ascii_uppercase)  + choice(string.ascii_uppercase) + '\', '
    emailA = '\'' + fname + "." + lname + str(randint(1,99)) + emailAddress() + '\', '
    number = '\'' + numberGet() + '\', '
    emeNumber = '\'' + numberGet() + '\', '
    return("INSERT INTO Coursework.Staff VALUES (NULL, " + '\'' + fname + '\', \'' + lname + '\', ' + address + postcode + emailA + number + emeNumber)

def pubGen(pubCount, managerID):
    pubName = pubNameGen()
    address = str(randint(1, 200)) + " " + addresses()
    postcode = postcodes() + str(randint(1, 20)) + " " + str(randint(0, 9)) + choice(string.ascii_uppercase)  + choice(string.ascii_uppercase)
    return("INSERT INTO Coursework.Pub VALUES (NULL, '" + pubName + "', '" + address + "', '" + postcode + "', '" + numberGet() + "', '" + pubEmailGen(pubName) + "', " + str(managerID) + ", " + str(capacity()) + ");")

def pubEmailGen(pubName):
    pubSplit = pubName.split(" ")
    length = len(pubSplit)
    final = ""
    for i in range(length - 1):
        final = final + pubSplit[i + 1]
    return final + "@crazycatpubs.co.uk"

def capacity():
    capacityU = randint(50,600)
    capacityR = capacityU / 10
    capacityR = round(capacityR, 0)
    capacityR = capacityR * 10
    return int(capacityR)

def pubNameGen():
    pubFile = open("pubnames.txt", "r")
    pubNames = pubFile.read().splitlines()
    pubName = pubNames[randint(0, len(pubNames) - 1)]
    pubFile.close()
    return pubName

def firstName():
    fNameFile = open("fnames.txt", "r")
    fnames = fNameFile.read().splitlines()
    fname = fnames[randint(0, len(fnames) - 1)]
    fNameFile.close()
    return fname

def lastName():
    lNameFile = open("lnames.txt", "r")
    lnames = lNameFile.read().splitlines()
    lname = lnames[randint(0, len(lnames) - 1)]
    lNameFile.close()
    return lname

def addresses():
    addressFile = open("road.txt", "r")
    roads = addressFile.read().splitlines()
    road = roads[randint(0, len(roads) - 1)]
    addressFile.close()
    return road

def postcodes():
    postcodeFile = open("postcode.txt", "r")
    post = postcodeFile.read().splitlines()
    postcode = post[randint(0, len(post) - 1)]
    postcodeFile.close()
    return postcode

def emailAddress():
    emailFile = open("email.txt", "r")
    emails = emailFile.read().splitlines()
    email = emails[randint(0, len(emails) - 1)]
    emailFile.close()
    return email

def numberGet():
    number = '0'
    for i in range(10):
        number = number + str(randint(1,9))
    return number