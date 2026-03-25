# GPS-NMEA-String-Parser
Short script that will parse NMEA strings such as GPRMC

NMEA sentences are long and hard to read this script will parse them for you.
Below is an example of an NMEA string.

&GPRMC,081236.00,A,3751.654,S,14507.328,E,012.3,045.6,150624,011.5,E,A,*2D

And here it is broken up

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

These are the Units,Min value,Max value that each piece of informatio has/uses.

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


