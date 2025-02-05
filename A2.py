class Vehicle:
    def __init__(self, max_speed, milage):
        self.max_speed= max_speed
        self.milage= milage
modelX=Vehicle(240, 18)
print("modelX's max speed: ", modelX.max_speed)
print("ModelX's milage: ", modelX.milage)