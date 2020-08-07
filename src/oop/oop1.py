# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# looks like vehicle is the base class for every other class
class Vehicle:
    def __init__(self):
        pass

# ground vehicle and flight vehicle are the next two categories

class GroundVehicle(Vehicle):
    def __init__(self):
        pass

class FlightVehicle(Vehicle):
    def __init__(self):
        pass

# next, the more specific classes: Car, Motorcycle, Starship, Airplane
class Car(GroundVehicle):
    def __init__(self):
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        pass

class Starship(FlightVehicle):
    def __init__(self):
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        pass
