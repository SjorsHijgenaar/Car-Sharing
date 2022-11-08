import enum
from platform import platform
from typing import List

class Package:
  def __init__(self, duration, price, km_price, free_km):
    self.duration = duration
    self.price = price
    self.km_price = km_price
    self.free_km = free_km

class Car:
  def __init__(self, platform:str, model:str, make:str, hourly_rate:int, km_price:float, free_km:int):
    self.platform = platform
    self.model = model
    self.make = make
    self.hourly_rate = hourly_rate
    self.km_price = km_price
    self.free_km = free_km
    self.packages: List[Package] = []

  def add_package(self, duration, price, km_price, free_km):
    self.packages.append(Package(duration, price, km_price, free_km))