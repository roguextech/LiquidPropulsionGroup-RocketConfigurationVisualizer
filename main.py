from src.chemistry import Chemistry
from src.chemistryCEA import ChemistryCEA
from src.rocket import Rocket
from src.ceaRocket import ceaRocket
from src.flight import Flight
import math

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

#stinger rocket sizing
title = 'Stinger Engine Sizing'
oxidizer = 'LOX'        # full propellant selection is availible at https://rocketcea.readthedocs.io/en/latest/propellants.html
fuel = 'RP1'
Pcham = 15.2      #in bar
propellant_ratio = 2.3
pAmbient = 1.01325
chems = Chemistry.parse_initVeriables('test_2-3of_15atm')
#set veriables
mdot = 1
l_star = 1.1
cham_d = 3.75 * 0.0254 #in meters
conv_angle = math.pi / 4 # rad, 45deg
div_angle = math.pi / 12  # rad, 15deg
wall_temp = 850 # K
r1 = 1
r2 = 1
r3 = 0.4
step = 5e-4
nozzle_type = 'conical'
stinger = Rocket(title, chems, mdot, l_star, cham_d, conv_angle, div_angle, wall_temp, nozzle_type, r1, r2, r3, step)
stinger.variablesDisplay()
stinger = ceaRocket(title, oxidizer, fuel, Pcham, pAmbient, propellant_ratio, mdot, l_star, cham_d, conv_angle, div_angle, wall_temp, nozzle_type, r1, r2, r3, step)
stinger.variablesDisplay()
#stinger.graphDisplay()

#test
title = 'Stinger Test Sizing'
oxidizer = 'LOX'
fuel = 'RP1'
#chems = Chemistry.parse_initVeriables('stinger_test_25bar')
mdot = 3
l_star = 1.1
cham_d = 5.5 * 0.0254 #in meters
conv_angle = math.pi / 4 # rad, 45deg
div_angle = math.pi / 12  # rad, 15deg
wall_temp = 1000 # K
r1 = 1.5
r2 = 1.5
r3 = .5
step = 5e-4
propellant_ratio = 2.3
nozzle_type = 'bell80'
#stinger = Rocket(title, chems, mdot, l_star, cham_d, conv_angle, div_angle, wall_temp, nozzle_type, r1, r2, r3, step)
#stinger.variablesDisplay()
#stinger.graphDisplay()

#methate engine test
title = 'Methane Engine Test'
oxidizer = 'LOX'
fuel = 'CH4'
chems = Chemistry.parse_initVeriables('methane_test_50bar')
mdot = 5
l_star = 1.1
cham_d = 5 * 0.0254 #in meters
conv_angle = math.pi / 4 # rad, 45deg
div_angle = math.pi / 8  # rad, 15deg
wall_temp = 1000 # K
r1 = 1
r2 = 1
r3 = 0.4
step = 5e-4
propellant_ratio = 2.7
nozzle_type = 'bell80'
#methane = Rocket(title, chems, mdot, l_star, cham_d, conv_angle, div_angle, wall_temp, nozzle_type, r1, r2, r3, step)
#methane.variablesDisplay()
#methane.graphDisplay()



#rocket trajectory test
title = "test rocket trajectory"
mRocket = 10
thrust = 9000
mDot = 2
htarget = 13716
dragCd = 0.5
vehicleArea = 1.0
hInit = 0.0
#my_flight = Flight(title, mRocket, thrust, mDot, htarget, dragCd, vehicleArea, hInit)
#my_flight.printInfo()
