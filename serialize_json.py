# -*- coding: utf-8 -*-
"""
serialize json
"""
from multipledispatch import dispatch
from deserialize_json import DeserializeJson
import json
class SerializeJson:
 #metoda statyczna
 @staticmethod
 def run(newDeserializator, filelocation):
  if(type(newDeserializator) is str):
   newDeserializator = DeserializeJson(newDeserializator)
   print("Serializacja przez plik")
  else:
   print("serializacja przez obiekt")
  lst = []
  #TODO – do modyfikacji
  for dep in newDeserializator.data:lst.append({
   "Kod_TERYT": dep['Kod_TERYT'],
   "Województwo": dep["Województwo"],
   "Powiat": dep["Powiat"],
   "typ_JST": dep["typ_JST"],
   "nazwa_urzędu_JST":dep["nazwa_urzędu_JST"],
   "miejscowość":dep["miejscowość"],
   "telefon_z_numerem_kierunkowym":dep["telefon kierunkowy"]
    })
  jsontemp = {"departaments":lst}
  with open(filelocation, 'w',encoding='utf-8') as f: json.dump(jsontemp, f, ensure_ascii=False)

