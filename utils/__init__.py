#!/usr/bin/env python

from utils.car import Car
from utils.weather import Weather
from utils.competition import Competition

cars = {
    Car('ferrary', 340, 0.324, 26),
    Car('bugatti', 407, 0.39, 32),
    Car('toyota', 180, 0.25, 40),
    Car('lada', 180, 0.32, 56),
    Car('sx4', 180, 0.33, 44)
}
weather = Weather(20)
Competition(cars, weather).start(distance=10000)
exit()
