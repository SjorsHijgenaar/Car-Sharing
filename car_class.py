from typing import List

class Package:
  def set_name(self, name):
      if self.duration == 0:
        return f'{self.free_km} km'
      else:
        return f'{self.duration} hr'
        

  def __init__(self, duration, price, km_price, free_km, name):
    self.duration = duration
    self.price = price
    self.km_price = km_price
    self.free_km = free_km
    self.name = name if name != '' else self.set_name(name)


class Car:
  def __init__(self, platform:str, model:str, make:str, hourly_rate:int, km_price:float, free_km:int):
    self.platform = platform
    self.model = model
    self.make = make
    self.hourly_rate = hourly_rate
    self.km_price = km_price
    self.free_km = free_km
    self.packages: List[Package] = []

  def add_package(self, duration, price, km_price, free_km, name = ''):
    self.packages.append(Package(duration, price, km_price, free_km, name))