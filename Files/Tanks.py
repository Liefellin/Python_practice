import time


class Vehichle:

    def turn(self,left, ttype):
        ttype("left", True)
        time.sleep(0.25)
        ttype("left", False)


class TrackedVehicle(Vehichle):
    def control_track(self, left, stop):
        print("T")


class WheeledVehicle(Vehichle):
    def turn_front_wheels(self, left, on):
        return "W"


tank = TrackedVehicle()
tank.turn("left", tank.control_track)