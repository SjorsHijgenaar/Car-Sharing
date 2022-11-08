from car_class import Car
import heapq

def main():
  sixt_bmw_i3 = Car('SIXT', 'BMW', 'i3', 15, 0.34, 200)
  sixt_bmw_i3.add_package(3, 39, 0.34, 80)
  sixt_bmw_i3.add_package(6, 55, 0.34, 120)
  sixt_bmw_i3.add_package(24, 85, 0.34, 200)
  sixt_bmw_i3.add_package(48, 169, 0.34, 300)
  sixt_bmw_i3.add_package(72, 235, 0.34, 400)
  sixt_bmw_i3.add_package(168, 379, 0.34, 600)
  sixt_bmw_i3.add_package(0, 14, 0.34, 50)
  sixt_bmw_i3.add_package(0, 27, 0.34, 100)
  sixt_bmw_i3.add_package(0, 39, 0.34, 150)
  sixt_bmw_i3.add_package(0, 63, 0.34, 250)
  sixt_bmw_i3.add_package(0, 125, 0.34, 500)

  def find_best_package_combination(car: Car, distance, duraction, price):
    heap = [(0, (0, 0), tuple(package, 0) for package in car.packages)]

if __name__ == "__main__":
    main()