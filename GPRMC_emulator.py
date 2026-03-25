#-------------------
#GPRMC Emulator
#26/01/2026
#-------------------
"""
Headings and range of values in nmea GPRMC
1   Time       00:00:00.000–23:59:59.999
2   Status     A or V
3   Latitude   00–89°, minutes 00.0000–59.9999
4   N/S        N or S
5   Longitude  000–179°, minutes 00.0000–59.9999
6   E/W        E or W
7   SOG        0.0–999.9 knots
8   COG        0.0–359.9°
9   Date       ddmmyy
10  Mag Var    0.0–180.0 + E/W
11  Mode       A/D/E/N
12  Checksum   00–FF hex
"""
import random
import time
import datetime


def random_gprmc_time():
    # Pick a random time of day
    random_seconds = random.randint(0, 24*3600 - 1)
    t = (datetime.datetime.min + datetime.timedelta(seconds=random_seconds)).time()

    # Format into GPRMC hhmmss.sss
    return t.strftime("%H%M%S") + ".000"

#Code does not output a perfect string (ie mode and status may conflict) but it does the job.
def GPRMC_emulator():
    talker_id = "$GPRMC"
    UTC_time = (random_gprmc_time())
    status = random.choice(["A","B"])
    deg = random.uniform(0, 90)
    minutes = random.uniform(0, 60)
    latitude = f"{int(deg):02d}{minutes:06.4f}"
    NS = random.choice(["N","S"])
    deg = random.uniform(0, 180)
    minutes = random.uniform(0, 60)
    longitude = f"{int(deg):03d}{minutes:06.4f}"
    EW = random.choice(["E","W"])
    SOG = f"{random.uniform(0, 999.9):05.1f}"
    COG = f"{random.uniform(0, 359.9):05.1f}"
    date = 123456
    magvar = f"{random.randint(1,90):03.1f}"
    magvardir = random.choice(["E","W"])
    mode = random.choice(["A","D","E","M","N"])

    pre_checksum = (f"{talker_id},{UTC_time},{status},{latitude},{NS},{longitude},{EW},{SOG},{COG},{date},{magvar},{magvardir},{mode}*")

    checksum_string = pre_checksum[1:pre_checksum.find("*")]

    check_sum = 0
    for char in checksum_string:
        check_sum ^= ord(char)
   
    time.sleep(1)
    return (f"{pre_checksum}{hex(check_sum)[2:]}")





