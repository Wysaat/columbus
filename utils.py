import time

def isleapyear(year):
    if year % 400 == 0: return 1
    elif year % 100 == 0: return 0
    elif year % 4 == 0: return 1
    return 0

# get ctime() of the time tlength years from now    
def gettime(tlength):
    year = int(time.ctime().split()[-1])
    dyear = year + tlength
    days = 365 * tlength
    for y in range(year, int(dyear)):
        if isleapyear(y): days += 1
    seconds = days * 24 * 60 * 60
    return time.ctime(time.time() + seconds)
