import math


class NotEnoughFuelError(Exception):

    ''' Raised when not enough fuel exists for a vehicle to move.'''

    def __int__(self: 'NotEnoughFuelError'):
        Exception.__int__(self, "Not enoguh fuel to move.")


class Motorized():

    '''
    A class used to model a car.

    operations:
            - fill_up(): fill up the fuel tank
            - travel_to(new_pos): change the vehicles position to new_pos

    attributes:
            - num_wheels(int): number of wheels of this vehicle
            - current_pos(float, float): the current position of this vehicle
                on a 2D plane - new vehicles start with (0.0, 0.0) as position
            - fuel_capacity(float): the capacity of the fuel tank in litres
            - fuel_level(float): current fuel level in litres - new vehicles
                start with full tank
            -fuel_economy(float): the number of litres of fuel required
                for the vehicle to travel 100km

    '''

    def __init__(self: 'Motorized', num_wheels: int,
                 fuel_capacity: float, fuel_economy: float) -> None:
        ''' Create a new motized vehicle. '''

        self.num_wheels = num_wheels
        self.current_pos = (0.0, 0.0)
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity
        self.fuel_economy = fuel_economy

    def fill_up(self: 'Motorized'):
        ''' Fill up the vehicle's fuel to capacity. '''
        self.fuel_level = self.fuel_capacity

    def travel_to(self: 'Motorized', new_pos: (float, float)) -> None:
        ''' Change the vehicle's position to new_pos if there is enough fuel
        in the tank. If successful, the vehicle's position and fuel levels
        are adjusted accordingly. Otherwise, a NotEnoughFuelError is raised,
        and the vehicle's position and  fuel levels are left unchanged.
        '''
        x1, y1 = new_pos
        x0, y0 = self.current_pos
        distance = abs(x1 - x0) + abs(y1 - y0)

        fuel_required = self.fuel_economy * (distance / 100)

        if (self.fuel_level > fuel_required):
            self.current_pos = new_pos
            self.fuel_level -= fuel_required
        else:
            raise NotEnoughFuelError()


class Car(Motorized):

    '''A Motorized vehicle with 4 wheels, a 50 litre tank, and a fuel economy
    of 8 litres per 100km.
    '''

    def __init__(self: 'Car') -> None:
        ''' Creates a new Car '''
        Motorized.__init__(self, 4, 50, 8)

    def fill_up(self: 'Car') -> None:
        ''' Fill up the Car's fuel to capacity. '''
        return super(Car, self).fill_up()

    def travel_to(self: 'Car', new_pos: (float, float)) -> None:
        ''' Make the Car travel to a new position using fuel. '''
        super(Car, self).travel_to(new_pos)


class Motorcycle(Motorized):

    ''' A Motorized vehicle with 2 wheels, a 15 litre fuel tank, 
    and a fuel economy of 5 litres per 100 km. '''

    def __init__(self: 'Motorcycle') -> None:
        ''' Create a new Motorcycle. '''
        Motorized.__init__(self, 2, 15, 5)

    def fill_up(self: 'Motorcycle') -> None:
        ''' Fill up Motorcyle fuel. '''
        super(Motorcycle, self).fill_up()

    def travel_to(self: 'Motocycle', new_pos: (float, float)) -> None:
        ''' Make the Motorcycle travel to the new position. '''
        super(Motocycle, self).travel_to(new_pos)
