#-----------------------
#GPS Parser
#23/01/2026
#-----------------------

#Function that gets the checksum value manually by XOR-ing all asciis values of string from (not including)$ to *
def validate(input_string):
    check_string = input_string[1:input_string.find("*")]
    check_sum = 0
    #print(check_string)
    for char in check_string:
        check_sum ^= ord(char)
    
    return check_sum


class Parse_GPRMC:

    def __init__(self,gps_input):
        #compares hex value at end of string to hex value from validate function if they are eqaul the GPRMC string is not corrupt
        if validate(gps_input) == int(f"0x{gps_input[gps_input.find('*')+1:]}",16):
            self.valid = True
            
            comma_position = []
            #gets index position of all commas in the string as that is how data is seprated
            for i,char in enumerate(gps_input):
                if char == ",":
                    comma_position.append(i)
            
            #Parses data from the string using comma_position
            self.TalkerID = gps_input[0:comma_position[0]]
            self.Timestamp = gps_input[comma_position[0]+1:comma_position[1]]
            self.Status = gps_input[comma_position[1]+1:comma_position[2]]
            self.Lat = float(gps_input[comma_position[2]+1:comma_position[3]])
            self.NS = gps_input[comma_position[3]+1:comma_position[4]]
            self.Long = float(gps_input[comma_position[4]+1:comma_position[5]])
            self.EW = gps_input[comma_position[5]+1:comma_position[6]]
            self.SOG = float(gps_input[comma_position[6]+1:comma_position[7]])
            self.COG = float(gps_input[comma_position[7]+1:comma_position[8]])
            self.Date = gps_input[comma_position[8]+1:comma_position[9]]
            self.MagVar = gps_input[comma_position[9]+1:comma_position[10]]
            self.MagVarDir = gps_input[comma_position[10]+1:comma_position[11]]
            self.Mode = gps_input[comma_position[11]+1:gps_input.find("*")]
            self.CheckSum = gps_input[gps_input.find("*"):]
        else:
            self.valid = False
            return valid
        

    #speed over ground is in knots this function converts speed unit depending on arg
    def speed(self,unit):
        if unit == "kmh":
            return self.SOG * 1.852
        elif unit ==  "knots":
            return self.SOG
        elif unit ==  "ms":
            return self.SOG * 0.514444
        else:
            sys.exit(f"Invalid argument {unit}")
    #returns cordinates  
    def location(self):
        latdegrees = str(self.Lat)[:2]
        latmin = str(self.Lat/60)[2:4]
        latsec = str(self.Lat/3600)[4:]
        lat_dd = latdegrees+latmin+latsec
        
        longdegrees = str(self.Long)[:2]
        longmin = str(self.Long/60)[2:4]
        longsec = str(self.Long/3600)[4:]
        long_dd = longdegrees+longmin+longsec
        
        return(lat_dd,long_dd)
    #returns degrees from true north(course over ground)
    def direction(self):
        return(self.COG)
    
    
    
class Parse_GPGGA:
    
    def __init__(self,gps_input):
        if validate(gps_input) == int(f"0x{gps_input[gps_input.find('*')+1:]}",16):
            print("Valid")
            
            comma_position = []
            #gets index position of all commas in the string as that is how data is seprated
            for i,char in enumerate(gps_input):
                if char == ",":
                    comma_position.append(i)
        
            self.TalkerID = gps_input[0:comma_position[0]]
            self.UTC = gps_input[comma_position[0]+1:comma_position[1]]
            self.Lat = float(gps_input[comma_position[1]+1:comma_position[2]])
            self.NS = gps_input[comma_position[2]+1:comma_position[3]]
            self.Long = float(gps_input[comma_position[3]+1:comma_position[4]])
            self.EW = gps_input[comma_position[4]+1:comma_position[5]]
            self.GPSQual = gps_input[comma_position[5]+1:comma_position[6]]
            self.Sats = int(gps_input[comma_position[6]+1:comma_position[7]])
            self.HDOP = gps_input[comma_position[7]+1:comma_position[8]]
            self.Altitude = gps_input[comma_position[8]+1:comma_position[9]]
            self.AltitudeVal = gps_input[comma_position[9]+1:comma_position[10]]
            self.GeoSep = gps_input[comma_position[10]+1:comma_position[11]]
            self.GeoVal = gps_input[comma_position[11]+1:comma_position[12]]
            self.DGPSRef = gps_input[comma_position[12]+1:gps_input.find("*")]
            self.Checksum = gps_input[gps_input.find("*"):]
            
            
    def location(self):
        latdegrees = str(self.Lat)[:2]
        latmin = str(self.Lat/60)[2:4]
        latsec = str(self.Lat/3600)[4:]
        lat_dd = latdegrees+latmin+latsec
        
        longdegrees = str(self.Long)[:2]
        longmin = str(self.Long/60)[2:4]
        longsec = str(self.Long/3600)[4:]
        long_dd = longdegrees+longmin+longsec
        
        return(lat_dd,long_dd)
    
class GPVTG:

    def __init__(self,gps_input):
        if validate(gps_input) == int(f"0x{gps_input[gps_input.find('*')+1:]}",16):
            print("Valid")
            
            comma_position = []
            #gets index position of all commas in the string as that is how data is seprated
            for i,char in enumerate(gps_input):
                if char == ",":
                    comma_position.append(i)
            
            self.TalkerID = gps_input[0:comma_position[0]]
            self.Course = gps_input[comma_position[0]+1:comma_position[1]]
            self.Refrence = gps_input[comma_position[1]+1:comma_position[2]]
            self.Degrees = gps_input[comma_position[2]+1:comma_position[3]]
            self.SOGkn = gps_input[comma_position[3]+1:comma_position[4]]
            self.kn = gps_input[comma_position[4]+1:comma_position[5]]
            self.SOGkmh = gps_input[comma_position[5]+1:comma_position[6]]
            self.kmh =gps_input[comma_position[6]+1:comma_position[7]]
            self.Mode = gps_input[comma_position[7]+1:gps_input.find("*")]
            self.Checksum = gps_input[gps_input.find("*"):]
            
            
    def speed(self,unit):
        if unit == "kmh":
            return self.SOGkmh
        elif unit == "knots":
            return self.SOGkn
        else:
            sys.exit(f"Invalid argument {unit}")






"""
order neo 6m outputs nmea sentences
GGA
GLL
GSA
GSV
RMC
VTG 

$GPRMC          - Sentence identifier
081236.00       - UTC time (08:12:36.00)
A               - Status (Active/Valid)
3751.654        - Latitude (37°51.654' = 37.86 degrees South)
S               - South
14507.328       - Longitude (145°07.328' = 145.12 degrees East)
E               - East
012.3           - Speed over ground (12.3 knots)
045.6           - Course over ground (45.6 degrees)
150624          - Date (15/06/2024)
011.5           - Magnetic variation (11.5 degrees)
E               - Magnetic direction East
A               - Mode (Autonomous)
*2D             - Checksum

#Field name Description Units Min value Max value
1   UTC Time    Time of fix (hhmmss.sss)  UTC	000000.000	235959.999
2   Latitude    Latitude    DDMM.MMMM    0000.0000	9000.0000
3   N/S	Latitude hemisphere	N / S	S	N
4   Longitude	Longitude	DDDMM.MMMM	00000.0000	18000.0000
5   E/W	Longitude hemisphere	E / W	W	E
6   Fix Quality	GPS fix type	code	0	8*
7   Number of Satellites	Satellites used	count	00	12†
8   HDOP	Horizontal dilution	unitless	0.0	~50.0
9   Altitude	Antenna altitude above MSL	meters	−10,000	+100,000
10  Altitude Units	Altitude unit	M	M	M
11  Geoid Separation	Height of geoid above WGS84	meters	−100	+100
12  Geoid Units	Geoid unit	M	M	M
13  Age of DGPS Data	Time since last DGPS update	seconds	0	999
14  DGPS Station ID	DGPS station identifier	ID	0000	1023


How to convert degrees,minutes,seconds to decimal degrees
One degree is equal to 60 minutes and equal to 3600 seconds:

1° = 60' = 3600"

One minute is equal to 1/60 degrees:

1' = (1/60)° = 0.01666667°

One second is equal to 1/3600 degrees:

1" = (1/3600)° = 2.77778e-4° = 0.000277778°

For angle with d integer degrees m minutes and s seconds:

d° m' s"

The decimal degrees dd is equal to:

dd = d + m/60 + s/3600
"""