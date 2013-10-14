# Time Travel Project
# Abrar Hussain


import math

percentage_speed = float(
    input("Enter % of speed of light as floating point (ex. 0.5): ")) 
lorentz_factor = (1 / (math.sqrt(1 - (percentage_speed ** 2 / 1))))

ship_weight = str(lorentz_factor * 70000)
trip_alpha_centauri = str(4.3 / lorentz_factor)
trip_bernards_star = str(6.0 / lorentz_factor)
trip_betelgeuse = str(309 / lorentz_factor) 
trip_andromeda = str(2000000 / lorentz_factor)

print("The ship's weight is " + ship_weight + "kg.")
print("The astronaut's experience to Alpha Centauri is "
      + trip_alpha_centauri + " light years long.")
print("The astronaut's experience to Bernard's Star is "
      + trip_bernards_star + " light years long.")
print("The astronaut's experience to Betelgeuse is "
      + trip_betelgeuse + " light years long.")
print("The astronaut's experience to Andromeda is "
      + trip_andromeda + " light years long.")
