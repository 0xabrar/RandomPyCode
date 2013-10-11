from motorized import Motorized
import unittest


class TestMotorized(unittest.TestCase):

    '''
    Used to unittest the Motorized class.
    '''

    def setUp(self):
        motorized = Motorized(4, 50, 10)

    def test_motorized_fill(self):
        motorized = Motorized(4, 50, 10)
        new_pos = (10.0, 10.0)
        motorized.travel_to(new_pos)
        motorized.fill_up()

        self.assertEqual(motorized.fuel_level, 50)

    def test_motorized_travel(self):
        motorized = Motorized(4, 50, 10)
        new_pos = (100.0, 0.0)
        motorized.travel_to(new_pos)

        self.assertEqual((100.0, 0.0), motorized.current_pos)

    def test_motorized_fuel_reduction(self):
        motorized = Motorized(4, 50, 10)
        new_pos = (100.0, 0.0)
        motorized.travel_to(new_pos)

        self.assertEqual(40, motorized.fuel_level)


if __name__ == '__main__':
    unittest.main()
