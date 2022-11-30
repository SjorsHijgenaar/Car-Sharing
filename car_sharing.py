from car_class import Car
import heapq

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

  mywheels_peugeot_208 = Car('MyWheels', 'Peugeot', 'E-308', 3.75, 0.33, 0)
  mywheels_peugeot_208.add_package(24, 37.50, 0.33, 0)

  cars = [sixt_bmw_i3, mywheels_peugeot_208]

  x = []
  y = []

  def find_best_package_combination(car: Car, distance, duration):
    # package for buying the total dis dur hourly
    car.add_package(duration, duration * car.hourly_rate + max(0, distance - car.free_km) * car.km_price, car.km_price, car.free_km, 'hourly')
    # package for buying remaining dis dur hourly AKA package 'free'
    car.add_package(0, 0, car.km_price, car.free_km, 'free')
    # node is defined by a tuple of (cost, (distance, duration) and counts)
    # where counts is a breakdown of the number per package
    heap = [(0, (0, 0), tuple((package.name, package, (0, 0) if package.name == 'free' else 0) for package in car.packages))]
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

      for _name, package, count in counts:
        # heuristic for finding and adding package
        if package.name == 'free':
          package.price = remaining_km * car.km_price + remaining_hrs * car.hourly_rate
        if remaining_hrs > 0: 
          # don't buy km packages
          if package.duration == 0:
            continue
          elif package.price < car.hourly_rate * remaining_hrs:
            # it's cheaper to buy package than driving hourly
            new_cost = cost + package.price
            # TODO: i = n, replace
            new_counts = tuple((n, p, c + 1 if p == package else c) for n, p, c in counts)
            heapq.heappush(heap, (new_cost, (dis_dur[0] + package.free_km, dis_dur[1] + package.duration), new_counts))
          else:
            # the package is more expensive than driving hourly
            new_cost = cost + car.km_price * remaining_km
            # the 'free' package will only be added once to fill up remaining hrs
            # all the free kms are then used
            new_counts = tuple((n, p, (car.free_km, remaining_hrs) if n == 'free' else c) for n, p, c in counts)
            heapq.heappush(heap, (new_cost, (dis_dur[0] + car.free_km, dis_dur[1] + remaining_hrs), new_counts))
        elif remaining_km > 0:
          # it's always more expensive to buy remaining km with hour packages
          if package.duration > 0 or package.free_km == 0 and package.name != 'free':
            continue
          elif package.price < car.km_price * remaining_km:
            new_cost = cost + package.price
            new_counts = tuple((n, p, c + 1 if p == package else c) for n, p, c in counts)
            heapq.heappush(heap, (new_cost, (dis_dur[0] + package.free_km, dis_dur[1] + package.duration), new_counts))
          else:
            new_cost = cost + car.km_price * remaining_km
            new_counts = tuple((n, p, (remaining_km, c[1]) if n == 'free' else c) for n, p, c in counts)
            heapq.heappush(heap, (new_cost, (dis_dur[0] + remaining_km, dis_dur[1]), new_counts))
          
  # distance = input("Type desired distance in kilometers: ")
  distance = 800
  # duration = input("Type desired duration in hours: ")
  duration = 168
  
  for car in cars:
    result = []
    for yields in find_best_package_combination(car, distance, duration):
      result.append(yields)
    best = heapq.heappop(result)
    print(''.join(map(str, best)).replace(", ('", "\n('"))


if __name__ == "__main__":
    main()