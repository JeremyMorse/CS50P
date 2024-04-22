

def main():
    #Collect User Time
    userTime = input("What time is it? ").strip().casefold()
    #Call convert function
    systemTime = float(convert(userTime))
    #Display based on systemTime
    if 7.0 <= systemTime < 8.0:
        print("breakfast time")
    elif 12.0 <= systemTime < 13.0:
        print("lunch time")
    elif 18.0 <= systemTime < 19.0:
        print("dinner time")
    else:
        return None


def convert(time):
    #Convert 12-hour time
    if time.endswith(("p.m.", "pm", "p.m")):
        hh, mm = map(float, time.rstrip(" .pm").split(":"))
        hh += 12
    else:
        hh, mm = map(float, time.split(":"))
    #Convert minutes
    mm = mm / 60
    #Return
    return float(hh + mm)

#Version 1 of convert
"""
def convert(time):
    #Split time
    hh, mm = time.split(":")
    #Turn to floats
    hh = float(hh)
    mm = (float(mm) / 60)
    #Convert 12-hour time
    if time.endswith("p.m." or "pm" or "p.m") and hh < 12:
        hh = hh + 12
    ##print(hh + mm)
    return float(hh + mm)
    #Convert to float
    
"""


if __name__ == "__main__":
    main()

