import datetime
import time as ta

def time_reformat(time):
    t = ta.strptime(time, "%H:%M")
    minutes = t.tm_hour * 60 + t.tm_min
    return minutes


def extract_time(time):
    """
    Extract hour and minutes from a datetime string
    Ex: "2022-04-16 06:37:30.472276" will return "6:37"
    """
    
    time = str(time)

    # if timezone is included in string, eliminate it
    if("+" in time):
        time = time.split("+")
        time = time[0]

    # eliminate date in string
    time = time.split(" ")
    time = time[1]
    time = time.split(":")
    time = time[0]+":"+time[1]
    time = time_reformat(time)

    return time



def session_expired(session_created):
    time = datetime.datetime.now()
    print(time)
    now=extract_time(time)
    session_time=extract_time(session_created)
    # if session time expire, return true
    if(now-session_time >=5):
        return True
    return False

django="2022-04-15 10:19:40.391464+00:00"




print(session_expired(django))

