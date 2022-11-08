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