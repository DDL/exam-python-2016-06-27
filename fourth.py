# Create a Rocket class
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9"
# 2nd parameter: the starting fuel level as a number
# 3rd parameter: number of launches as a number
#
# It should have 3 methods:
#
# launch()
# it should use 1 fuel if it's a falcon1 and 9 if it's a falcon9
# it should increment the launches by one
#
# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9
# it should return the used fuel
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2
#
# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11"

# Create a SpaceX class
# it should take 1 parameter in its constructor
# 1st parameter: the stored fuel
#
# it should have 4 methods:
#
# addRocket(rocket)
# it should add a new rocket to SpaceX that is given in its first parameter
#
# refill_all()
# it should refill all of its rockets with fuel and substract the needed fuel from the storage
#
# launch_all()
# it should launch all the rockets
#
# buy_fuel(amount)
# it should increase stored fuel by amount
#
# getStats()
# it should return its stats as a sting like: "rockets: 3, fuel: 100, launches: 1"


# The following code should work with the classes

class Rocket(object):
    def __init__(self, type_of_rocket= '', starting_fuel_level= 0, number_of_lunches = 0):
        self.type_of_rocket = type_of_rocket
        self.fuel_level = starting_fuel_level
        self.launch_num = number_of_lunches
        self.setRockets()

    def setRockets(self):
        if self.type_of_rocket == 'falcon1':
            self.fuel_use = 1
            self.fuel_limit = 5
        if self.type_of_rocket == 'falcon9':
            self.fuel_use = 9
            self.fuel_limit = 20

    def launch(self):
        self.fuel_level -= self.fuel_use
        self.launch_num += 1

    def refill(self):
        self.used_fuel = self.fuel_limit - self.fuel_level
        self.fuel_level = self.fuel_limit
        return self.used_fuel

    def getStats(self):
        return ('Name: %s , Fuel: %s' % (str(self.type_of_rocket), str(self.fuel_level)))


class SpaceX(object):
    def __init__(self, fuel_storage):
        self.fuel_storage = fuel_storage
        self.rockets = []

    def addRocket(self,rocket):
        self.rockets.append(rocket)
#
    def refill_all(self):
        for rocket in self.rockets:
            self.fuel_storage -= rocket.refill()
#
    def launch_all(self):
        for rocket in self.rockets:
            rocket.launch()
        self.launches += 1

    def buy_fuel(self, amount):
        self.fuel_storage += amount

    def getStats(self):
        self.launches = 0
        for rocket in self.rockets:
            self.launches += rocket.launch_num
        return ('Rockets: ' + str(len(self.rockets)) + ', Fuel: ' + str(self.fuel_storage) + ', Launches: ' + str(self.launches))

# The following code should work with the classes


space_x = SpaceX(100)
falcon1 = Rocket('falcon1', 0, 0)
falcon9 = Rocket('falcon9', 0, 0)
returned_falcon9 = Rocket('falcon9', 11, 1)

print(returned_falcon9.getStats()) # name: falcon9, fuel: 11
#
space_x.addRocket(falcon1)
space_x.addRocket(falcon9)
space_x.addRocket(returned_falcon9)

print(space_x.getStats()) # rockets: 3, fuel: 100, launches: 1
space_x.refill_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 1
space_x.launch_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 4
space_x.buy_fuel(50)
print(space_x.getStats()) # rockets: 3, fuel: 116, launches: 4
