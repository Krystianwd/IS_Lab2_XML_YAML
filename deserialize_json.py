# -*- coding: utf-8 -*-
"""
deserialize json
"""
import json
class DeserializeJson:
 # konstruktor
 def __init__(self, filename):
  print("Tworzenie obiektu deserializacji")
  tempdata = open(filename, encoding="utf8")
  self.data = json.load(tempdata)
  # przykładowe statystyki
 def somestats(self):
  example_stat = 0
  slownik = {}
  for dep in self.data:
   if dep["Województwo"].strip()  in slownik:
    slownik[dep["Województwo"].strip()] = slownik[dep["Województwo"].strip()]+1
   if dep["Województwo"].strip()  not in slownik:
    slownik[dep["Województwo"].strip()] = 1
   if dep['typ_JST'] == 'GM' and dep['Województwo']== 'dolnośląskie':
    example_stat += 1
   #print('liczba urzędów miejskich w województwie dolnośląskim: ' + ' ' + str(example_stat))
  print(slownik)
