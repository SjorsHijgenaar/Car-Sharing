from random import randint
from car_class import Car
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import cm

def main():
  sixt_bmw_i3 = Car('SIXT', 'BMW', 'i3', 15, 0.34, 200)
  sixt_bmw_i3.add_hourly_package(3, 39, 0.34, 80)
  sixt_bmw_i3.add_hourly_package(6, 55, 0.34, 120)
  sixt_bmw_i3.add_hourly_package(24, 85, 0.34, 200)
  sixt_bmw_i3.add_hourly_package(48, 169, 0.34, 300)
  sixt_bmw_i3.add_hourly_package(72, 235, 0.34, 400)
  sixt_bmw_i3.add_hourly_package(168, 379, 0.34, 600)
  sixt_bmw_i3.add_km_package(50, 14)
  sixt_bmw_i3.add_km_package(100, 27)
  sixt_bmw_i3.add_km_package(150, 39)
  sixt_bmw_i3.add_km_package(250, 63)
  sixt_bmw_i3.add_km_package(500, 125)  

if __name__ == "__main__":
    main()