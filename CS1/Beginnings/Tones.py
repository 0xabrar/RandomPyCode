# Tones Project
# Abrar Hussain

from math import pow
from winsound import Beep


def play_frequency() -> None:
    ''' Asks users for an octave and a pitch class and then converts
    it to the according frequency. The frequency is displayed.
    The frequency will then be played.

    >>> play_frequency(4, 9)
    '4 . 9 equals 440.0 Hertz.

    '''
    octave = int(input("Give me an octave: "))
    pitch_class = int(input("Give me a pitch class: "))

    octave_difference = octave - 4
    pitch_difference = pitch_class - 9
    C_nought = int(440 * pow(2, (octave_difference +
                        (pitch_difference / 12))))

    print (str(octave) + " . " + str(pitch_class) + " equals "
           + str(C_nought) + " Hertz.")
    # note is played for 2 seconds
    Beep(C_nought, 2000)


if __name__ == '__main__':

    print("This program can convert octave/pitchclass pairs" +
          " into their appropriate Hertz values. It uses the" +
          " tempered scale conversions. The frequencies will also be played.")

    # 3 frequenies played
    play_frequency()
    play_frequency()
    play_frequency()

    print("Well that's it for my program. Arigatou gozaimasu!")
