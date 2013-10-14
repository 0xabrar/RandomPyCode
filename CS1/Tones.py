# Tones Project
# Abrar Hussain
''' This code redundancy could significantly be reduced with function
usage. But, alas, program speicifications. 
Future: One function with octave and pitch class as function parameters.
'''

from math import pow
import winsound

print("This program can convert octave/pitchclass pairs" +
      " into their appropriate Hertz values. It uses the" +
      " tempered scale conversions. The frequencies will also be played.")


# First note
octave_one = int(input("Give me an octave: "))
pitch_one = int(input("Give me a pitch class: "))

octave_differenc = octave_one - 4
pitch_difference = pitch_one - 9
C_nought = 440 * pow(2, (octave_differenc +
                    (pitch_difference / 12)))

print (str(octave_one) + " . " + str(pitch_one) + " equals "
       + str(C_nought))
winsound.Beep(int(C_nought), 2000)

# Second note
print("Let's do that again shall we.")
octave_two = int(input("Give me an octave: "))
pitch_two = int(input("Give me a pitch class: "))

octave_differenc = octave_two - 4
pitch_difference = pitch_two - 9
C_nought = 440 * pow(2, (octave_differenc +
                    (pitch_difference / 12)))

print (str(octave_two) + " . " + str(pitch_two) + " equals "
       + str(C_nought))
winsound.Beep(int(C_nought), 2000)

# Third note
print("One more time.")
octave_three = int(input("Give me an octave: "))
pitch_three = int(input("Give me a pitch class: "))

octave_differenc = octave_three - 4
pitch_difference = pitch_three - 9
C_nought = 440 * pow(2, (octave_differenc +
                    (pitch_difference / 12)))

print (str(octave_three) + " . " + str(pitch_three) + " equals "
       + str(C_nought))
winsound.Beep(int(C_nought), 2000)


print("Well that's it for my program. Arigatou gozaimasu!")
