from random import randrange, uniform
from car_class import Car
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import cm

def main():
  _ITERATIONS = 10000

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

  durations = np.empty(_ITERATIONS)
  distances = np.empty(_ITERATIONS)
  costs = np.empty([_ITERATIONS, 2])
  total_costs = np.empty(_ITERATIONS)

  for i in range (0, _ITERATIONS):
    # duration = 75
    duration = randrange(1, 168)
    distance = randrange(1, 1000)
    durations[i] = duration
    distances[i] = distance
    costs[i] = (sixt_bmw_i3.get_cheapest_hourly_package(duration), sixt_bmw_i3.get_cheapest_km_package(distance))
    total_costs[i] = sum(costs[i])

  # fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  # # Plot the surface.
  # surf = ax.plot_surface(duration, distance, total_costs, cmap=cm.coolwarm, linewidth=0, antialiased=False)
  # # Add a color bar which maps values to colors.
  # fig.colorbar(surf, shrink=0.5, aspect=5)

  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')
  ax.scatter(durations, distances, total_costs, picker=True)
  ax.set_xlabel('Duration [hr]')
  ax.set_ylabel('Distance [km]')
  ax.set_zlabel('Total cost [€]')

  def onpick(event):
    ind = event.ind
    print('Duration: ', durations[ind])
    print('Distance: ', distances[ind])
    print('Total cost: ', total_costs[ind])
    fig.canvas.draw_idle()

  fig.canvas.mpl_connect('pick_event', onpick)
  
  plt.show()
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_hourly_package(75):5.2f} for 1 hour')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_km_package(500):5.2f} for 201 km')

  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_km_package(210):5.2f} for 210 km')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_km_package(241):5.2f} for 241 km')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_km_package(242):5.2f} for 242 km')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_km_package(250):5.2f} for 250 km')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_km_package(300):5.2f} for 300 km')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_km_package(350):5.2f} for 350 km')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_km_package(400):5.2f} for 400 km')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_km_package(450):5.2f} for 450 km')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_km_package(500):5.2f} for 500 km')

  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_hourly_package(2):5.2f} for 2 hour')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_hourly_package(3):5.2f} for 3 hour')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_hourly_package(4):5.2f} for 4 hour')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_hourly_package(5):5.2f} for 5 hour')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_hourly_package(6):5.2f} for 6 hour')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_hourly_package(7):5.2f} for 7 hour')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_hourly_package(8):5.2f} for 8 hour')
  # print(f'This car would cost €{sixt_bmw_i3.get_cheapest_hourly_package(24):5.2f} for 24 hour')
  

if __name__ == "__main__":
    main()