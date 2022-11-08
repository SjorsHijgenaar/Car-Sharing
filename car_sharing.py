from car_class import Car
import heapq

def main():
  distance = input("Type desired distance in kilometers: ")
  duration = input("Type desired duration in hours: ")

  sixt_bmw_i3 = Car('SIXT', 'BMW', 'i3', 0.27*60, 0.39, 200)
  sixt_bmw_i3.add_package(3, 39, 0.39, 80)
  sixt_bmw_i3.add_package(6, 55, 0.39, 120)
  sixt_bmw_i3.add_package(24, 85, 0.39, 200)
  sixt_bmw_i3.add_package(48, 169, 0.39, 300)
  sixt_bmw_i3.add_package(72, 235, 0.39, 400)
  sixt_bmw_i3.add_package(168, 379, 0.39, 600)
  sixt_bmw_i3.add_package(0, 14, 0.39, 50)
  sixt_bmw_i3.add_package(0, 27, 0.39, 100)
  sixt_bmw_i3.add_package(0, 39, 0.39, 150)
  sixt_bmw_i3.add_package(0, 63, 0.39, 250)
  sixt_bmw_i3.add_package(0, 125, 0.39, 500)

  def find_best_package_combination(car: Car, distance, duraction, price):
    # node is defined by a tuple of (cost, (distance, duration) and counts)
    # where counts is a breakdown of the number per package
    heap = [(0, (0, 0), tuple(package, 0)) for package in car.packages]

if __name__ == "__main__":
    main()