#Gasoline Program (details on sheet)
#Abrar Hussain
'''
Constants:
- 1 gallon equivalent to 3.7854 litres
- 1 barrel of oil produces 19.5 gallons of gas 
- 1 gallon of gas produces approx. 20 pounds of C02
- 1 gallon of gas produces 115,000 BTU
- 1 gallon of ethanol produces 75,700 BTU
- price of oil is $4.00/gallon
'''

gallons_gasoline = float(raw_input("Gallons of gasoline:"))

num_litres = gallons_gasoline * 3.7854
num_barrels_req = gallons_gasoline / 19.5
C02_produced = gallons_gasoline * 20

energy_produced = gallons_gasoline * 115000
equiv_energy_ethanol = energy_produced / 75700
price = gallons_gasoline * 4

print
print "Number of litres:", num_litres
print "Number of barrels of oil required:", num_barrels_req
print "Number of pounds of CO2 produced:", C02_produced
print "Equivalent energy amount in ethanol gallons:", equiv_energy_ethanol
print "Price in US dollars:", price

print "\nThanks for playing."

