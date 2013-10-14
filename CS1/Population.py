#Population Project
#Abrar Hussain

'''
- current population is 307,357,870 humans
- every 7 seconds, a birth
- every 13 seconds, a death
- every 35 seconds, a new immigrant
'''

start_population = 307357870
num_years = int(raw_input("Number of years into the future:"))
num_seconds = num_years * 365 * 24 * 60 * 60

births = num_seconds // 7
deaths = num_seconds // 13
immigrants = num_seconds // 35

future_population = int(start_population + births - deaths + immigrants)
print "The future population is:", future_population 


