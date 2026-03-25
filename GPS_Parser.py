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





