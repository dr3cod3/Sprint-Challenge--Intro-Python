# Write classes for the following class hierarchy:
class Vehicle:
    pass  # Vehicle is the base class


class FlightVehicle(Vehicle):
    pass  # Vehicle is the base class for FlightVehicle


class Starship(FlightVehicle):  # FlightVehicle is the Parent class for Starship
    pass


class GroundVehicle(Vehicle):  # Vehicle is the base class for GroundVehicle
    pass


class Car(GroundVehicle):  # GroundVehicle is the base class for Car
    pass


class Motorcycle(GroundVehicle):  # GroundVehicle is the base class fpr Motorcyle
    pass


class Airplane(FlightVehicle):  # FlightVehicle is the base class for Airplane
    pass

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
