from machine import UART
lat = ""
lon = ""
time = ""
satellites = ""
alt = ""
speed =""
date =""
lati = ""
longi = ""
uart = UART(1, baudrate=9600)
uart.init(9600, bits=8, parity=None, stop=1, timeout_chars=500)
uart0 = UART(0,baudrate=9600)
uart0.init(9600, bits=8, parity=None, stop=1)
def GLL(lines):
	global lat, lon, time, satellites, alt, speed, date
	# print("==========================GLL=======================")
	if lines[5]:time = lines[5][0:2]+":"+lines[5][2:4]+":"+lines[5][4:]+" UTC"
	if lines[1]:lat = lines[1][0:2]+"°"+lines[1][2:]+lines[2]
	if lines[3]:lon = str(int(lines[3][0:3]))+"°"+lines[3][3:]+lines[4]
def GGA(lines):
	global lat, lon, time, satellites, alt, speed, date
	# print("==========================GGA=======================")
	if lines[1]: time = lines[1][0:2]+":"+lines[1][2:4]+":"+lines[1][4:]+" UTC"
	if lines[2]: lat = lines[2][0:2]+"°"+lines[2][2:]+lines[3]
	if lines[4]: lon = str(int(lines[4][0:3]))+"°"+lines[4][3:]+lines[5]
	if lines[7]: satellites = lines[7]
	if lines[9]: alt = lines[9]+' '+lines[10]
def RMC(lines):
	global lat, lon, time, satellites, alt, speed, date
	# print("==========================RMC=======================")
	if lines[1]: time = lines[1][0:2]+":"+lines[1][2:4]+":"+lines[1][4:]+" UTC"
	if lines[3]: lat = lines[3][0:2]+"°"+lines[3][2:]+lines[4]
	if lines[5]: lon = str(int(lines[5][0:3]))+"°"+lines[5][3:]+lines[6]
	if lines[7]: speed = str('%.4f' %(float(lines[7])*1.852))+' kmph'
	if lines[9]: date = lines[9][0:2]+"-"+lines[9][2:4]+"-"+lines[9][4:6]
def lattilong(line,lone):
	global lati, longi
	# print (line,lone)
	lati1 = float(line[0:2])
	lati2 = float(line[3:11])
	lati2 = (lati2)/60
	lati = lati1+ lati2
	if line[-1]=="S":
		lati=(-1)*lati
print("my 98j7")
	longi1 = float(lone[0:2])
	longi2 = float(lone[3:11])
	longi2 = (longi2)/60
	longi = longi1+ longi2
	if lone[-1]=="W":
		longi=(-1)*longi

while 1:
	read = uart.readline()
	# print("!!!")
	if read:
		read = read.decode('utf-8')
		# print(read)
		lines = read.split(",")
		if lines[0][3:] == "GLL":
			GLL(lines)
		if lines[0][3:] == "GGA":
			GGA(lines)
		if lines[0][3:] == "RMC":
			RMC(lines)
		if (lat and lon):
			lattilong(lat,lon)
		uart0.write("Latitude:"+lat+"Longitude:"+lon+'\n')
		uart0.write("Latitude:"+str(lati)+"Longitude:"+str(longi)+'\n')
		uart0.write("Date:"+date+"Time:"+time+'\n')
		uart0.write("No.of satellites:"+satellites+'\n')
		uart0.write("Altitude:"+alt+'\n')
		uart0.write("Speed:"+speed+'\n')
		uart0.write("==================================================\n")
