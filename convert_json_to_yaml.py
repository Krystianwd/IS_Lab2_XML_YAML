# -*- coding: utf-8 -*-
"""
json to yaml converter
"""
from deserialize_json import DeserializeJson
import yaml
from multipledispatch import dispatch
class ConvertJsonToYaml:
 @staticmethod
 @dispatch(str, str)
 def run(JsonLocation, destinationfilelocaiton):
    newDeserializator = DeserializeJson(JsonLocation)
    #newDeserializator.somestats()
    print("Zamiana na yaml przez plik")
    with open(destinationfilelocaiton, 'w', encoding='utf8') as f:
        yaml.dump(newDeserializator, f, allow_unicode=True)

 @staticmethod
 @dispatch(DeserializeJson, str)
 def run(deserializeddata, destinationfilelocaiton):
    print("Zamiana na yaml przez obiekt")
    with open(destinationfilelocaiton, 'w', encoding='utf8') as f:yaml.dump(deserializeddata, f, allow_unicode=True)
    print("it is done")
