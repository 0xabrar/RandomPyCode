#Measurement Project
#Abrar Hussain

'''
- 1 barleycorn equivalent to 117.647 meters
- 1 furlong is 220 yards
- 1 fortnight is 2 weeks
- Mach 1 = speed of sound in air= 1130 feet/second (approx.)
- PSL speed of light in a vacuum = 299,792,458 metres/second
- 1 meter is 1.09361 yards
- 1 meter is 3.28084 feet
'''

miles_per_hour = float(raw_input("Miles per hour speed:"))

kilometers_per_hour = miles_per_hour * 1.60934
barleycorn_per_day = kilometers_per_hour * 1000 * 24 * 117.647

furlongs_per_hour = kilometers_per_hour * 1000 * 1.09361 / 220
furlongs_per_fortnight =  furlongs_per_hour * 24 * 14

feet_per_hour = kilometers_per_hour * 1000 * 3.28084
mach_number = feet_per_hour / (1130 * 3600)

meters_per_second = kilometers_per_hour / 3600 * 1000
PSL = meters_per_second / 299792458 

print "Barleycorns/day:", barleycorn_per_day 
print "Furlongs/fortnight:", furlongs_per_fortnight
print "Mach number:", mach_number 
print "PSL:", PSL





