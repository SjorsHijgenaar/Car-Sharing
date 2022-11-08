import enum
from platform import platform
from typing import List

class Hourly_Package:
  def __init__(self, duration, price, km_price, free_km):
    self.duration = duration
    self.price = price
    self.km_price = km_price
    self.free_km = free_km

class Km_Package:
  def __init__(self, kms, price) -> None:
    self.kms = kms
    self.price = price

class Car:

  def __init__(self, platform:str, model:str, make:str, hourly_rate:int, km_price:float, free_km:int):
    self.platform = platform
    self.model = model
    self.make = make
    self.hourly_rate = hourly_rate
    self.km_price = km_price
    self.free_km = free_km
    self.hourly_packages: List[Hourly_Package] = []
    self.cheapest_hourly_package_index: int = None
    self.km_packages: List[Km_Package] = []
    self.chosen_km_packages = {
      "no_package": 0
    }

  def add_hourly_package(self, duration, price, km_price, free_km):
    self.hourly_packages.append(Hourly_Package(duration, price, km_price, free_km))

  def add_km_package(self, kms, price):
    self.km_packages.append(Km_Package(kms, price))
    self.chosen_km_packages[kms] = 0
  
  def get_cheapest_hourly_package(self, duration):
    if len(self.hourly_packages) == 0:
      # print(f'{self.platform} {self.model} {self.make} has no hourly packages. Renting by the hour is only option')
      return(self.hourly_rate * duration)

    if duration * self.hourly_rate <= self.hourly_packages[0].price:
      # print('Renting by the hour is cheapest based on duration')
      return(self.hourly_rate * duration)

    # combining packages is always more expensive than the next package
    # for now we assumed the duration is not longer than 7 days    
    for i, p in enumerate(self.hourly_packages):
      if p.duration >= duration:
        self.cheapest_hourly_package_index = i
        # print(f'Package for {p.duration} hours is cheapest based on duration')
        return(p.price)
      elif p.price + (duration - p.duration) * self.hourly_rate < self.hourly_packages[i+1].price:
        self.cheapest_hourly_package_index = i
        # print(f'Package for {p.duration} hours is cheapest based on duration')
        return(p.price + (duration - p.duration) * self.hourly_rate)        
  
  def get_cheapest_km_package(self, distance):
    if len(self.km_packages) == 0:
      # print(f'{self.platform} {self.model} {self.make} has no km packages. Renting by the hour is only option')
      return(self.km_price * distance)
    
    remaining_kms = distance
    km_cost = 0
    if self.cheapest_hourly_package_index == None:
      if distance < self.free_km:
        # print('Driving by the hour, no additional kms needed')
        self.chosen_km_packages["no_package"] += distance
        return(0)
      else:
        # print(f'Driving by the hour, but additional {distance - self.free_km} km needed')
        if self.km_price * (distance - self.free_km) < self.km_packages[0].price:
          # print('Buying additional km by the km is cheapest')
          self.chosen_km_packages["no_package"] += distance
          return(self.km_price * (distance - self.free_km))
        else:
          self.chosen_km_packages["no_package"] += self.free_km
          remaining_kms = remaining_kms - self.free_km
    elif distance <= self.hourly_packages[self.cheapest_hourly_package_index].free_km:
      # print(f'Enough km are included in the hourly package')      
      return(0)
    else:
      self.chosen_km_packages["no_package"] += self.hourly_packages[self.cheapest_hourly_package_index].free_km
      remaining_kms = remaining_kms - self.hourly_packages[self.cheapest_hourly_package_index].free_km
    
    while remaining_kms > 0:
      if remaining_kms * self.km_price < self.km_packages[0].price:
        # print(f'It is cheaper to buy {remaining_kms} individually')
        self.chosen_km_packages["no_package"] += remaining_kms
        remaining_kms = 0
        km_cost = km_cost + remaining_kms * self.km_price
      for i, p in enumerate(reversed(self.km_packages)):
        if p.kms <= remaining_kms or i == len(self.km_packages) - 1:
          # print(f'Km package of {p.kms} kms is required')
          self.chosen_km_packages[p.kms] += 1
          remaining_kms = remaining_kms - p.kms
          km_cost = km_cost + p.price
          break
    
    

    return(km_cost)
