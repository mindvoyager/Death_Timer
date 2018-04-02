#!/usr/bin/env python3
# this ^ makes sure that Python 3 and not 2 will be used.
'''
This program creates a "Death Countdown Meter" for how many hours remain
in your estimated expected lifespan.
'''
import time
from graphics import *
def inputLife():
    a = input("Enter your birthday in the format YYYY-MM-DD: ")
    x,y,z = a.split(sep='-')
    x,y,z = int(x),int(y),int(z)
    c = eval(input("Enter your expected lifespan in years (do some actuarial \
resarch): "))
    return x,y,z,c

# possibly for future implementation with leap years
#def isCommonYear(year):    # used modulo and evaluated if common year instead
#    if year % 4 != 0:      # of leap. Evaluating whether is leap year would
#        return True        # require evaluating cases from most special to
#    elif year % 100 != 0:  # least special (least efficient)
#        return False
#    elif year % 400 != 0:
#        return True
#    else:
#        return False


def secondsSinceEpoch(year,month,day):
    # super naive version
    monthsList = [31,28,31,30,31,30,31,31,30,31,30,31]
    sumDays = 0
    i = 0
    while i < month - 1:
        sumDays += monthsList[i]
        i += 1
    s = (year - 1970)*31556926 + sumDays*24*60*60 + day*24*60*60
    return s


def secondsConvert(years):
    return years * 31556926  # seconds/year
    # (((365 days * 24 hours/day) + 5 hours)*60 minutes/hour)
    # + 48 minutes)* 60 minutes/second + 46 seconds

def deathTime(year, month, day, lifespan):
    birth = secondsSinceEpoch(year,month,day)
    deathDay = birth + secondsConvert(lifespan)
    return float(deathDay)


def printTimer(deathDay):
    win = GraphWin('Lifespan Remaining Meter', width=800, height=200)
    centerpoint = Point(400, 100)
    while True:
        TimeLeftSeconds = deathDay - time.time()
        Years_s = TimeLeftSeconds
        Years = Years_s // 31556926
        Months_s = (Years_s % 31556926)           # seconds in average month,
        Months = Months_s // 2629746    # average month is 2629746 s
        Days_s = (Months_s % 2629746)  # days in seconds
        Days = Days_s // 86400  # divided by seconds in a day
        Hours_s = Days_s % 86400  # hours in seconds
        Hours = Hours_s // 3600  # divided by seconds in an hour
        Minutes_s = Hours_s % 3600  # minutes in seconds
        Minutes = Minutes_s // 60  # divided by seconds in a minute
        Seconds = (Minutes_s % 60) // 1
        textie = Text(centerpoint, 'Time Left: Years:{0:02.0f}  \
Months:{1:02.0f}  Days:{2:02.0f}  Hours:{3:02.0f}  Minutes:{4:02.0f}  \
Seconds:{5:02.0f}'.format(Years,Months,Days,Hours,Minutes,Seconds))
        textie.setSize(20)
        textie.setFace('helvetica')
        textie.setStyle('bold')
        textie.draw(win)
        time.sleep(1.0)
        textie.undraw()
#win.getMouse() # Pause to view result
#win.close()    # Close window when done

#entrie = Entry(Point(400,150), 10)
#entrie.draw(win)
#capture = entrie.getText()
#textie2 = Text(Point(400,50), capture)
#textie2.draw(win)

def main():
    Year,Month,Day,AgeAtDeath = inputLife()
    Death = deathTime(Year,Month,Day,AgeAtDeath)
    printTimer(Death)


if __name__ == '__main__':
    main()
