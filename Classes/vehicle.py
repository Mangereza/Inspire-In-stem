#!/usr/bin/python

######################
#   Classes : Vehicle Class
#   Name    : Stephanie Mangereza
#   Date    : 03 /06 /2022
######################

class vehicle:
    def __init__(self, _max_speed, _mileage):
         self.speed= _max_speed
         self.mileage= _mileage

    def wee (self):
         print('Damn James your cars have  ' + self.mileage, 'MPG' ' its max speed is ' + self.speed, 'km/hr')
BMW=vehicle (str( 435 ), str(41 ))
BMW.wee()
Mercedes=vehicle (str( 329 ), str(52))
Mercedes.wee()

    






