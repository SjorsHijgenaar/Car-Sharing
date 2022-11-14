from car_class import Package, Car
import heapq
import matplotlib.pyplot as plt

def main():
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

  x = []
  y = []

  def find_best_package_combination(car: Car, distance, duration):
    car.add_package(duration, duration * car.hourly_rate + max(0, distance - car.free_km) * car.km_price, car.km_price, car.free_km)
    # node is defined by a tuple of (cost, (distance, duration) and counts)
    # where counts is a breakdown of the number per package
    heap = [(0, (0, 0), tuple((id(package), package, 0) for package in car.packages))]
    visited = set()
    
    itr = 0
    while heap:
      x.append(itr)
      y.append(len(heap))
      itr += 1

      cost, dis_dur, counts = heapq.heappop(heap)
      if (cost, dis_dur, counts) in visited:
        continue
      visited.add((cost, dis_dur, counts))

      if dis_dur[0] >= distance and dis_dur[1] >= duration:
        yield (cost, dis_dur, counts)
        continue        

      remaining_km = max(0, distance - dis_dur[0])
      remaining_hrs = max(0, duration - dis_dur[1])

      for _id, package, count in counts:
        # heuristic for finding and adding package
        if 0 < package.duration < remaining_hrs or package.duration > remaining_hrs and package.free_km >= remaining_km or remaining_hrs == 0 and package.free_km >= remaining_km:        
            new_cost = cost + package.price
            new_counts = tuple((id(p), p, c + 1 if p == package else c) for i, p, c in counts)
            heapq.heappush(heap, (new_cost, (dis_dur[0] + package.free_km, dis_dur[1] + package.duration), new_counts))
          
  # distance = input("Type desired distance in kilometers: ")
  distance = 800
  # duration = input("Type desired duration in hours: ")
  duration = 168
  result = []
  for yields in find_best_package_combination(sixt_bmw_i3, distance, duration):
    result.append(yields)

  best = heapq.heappop(result)
  print(best)
  plt.plot(x, y)
  plt.show()


if __name__ == "__main__":
    main()