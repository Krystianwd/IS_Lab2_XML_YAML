import yaml
from deserialize_json import DeserializeJson
from convert_json_to_yaml import ConvertJsonToYaml
from serialize_json import SerializeJson
tempconffile = open('Assets/basic_config.yaml',encoding="utf8")
confdata = yaml.load(tempconffile, Loader=yaml.FullLoader)
newDeserializator = None
Ile_operacji = int(input("Podaj ile chcesz wykonac operacji 1-3"))
Jakie_operacje = []
i = 0
while(Ile_operacji>i):
    Jakie_operacje.append(int(input("Podaj co chcesz zrobić: 0 - serializacja, 1 - deserializacja, 2 - konwersja do yaml ")))
    if(Jakie_operacje[i] == 0):
        Czy_serializacja = int(input("Podaj z skąd chcesz serializować: 0 - plik, 1 - obiekt"))
        if(Czy_serializacja == 0):
            SerializeJson.run(confdata['source_folder']+confdata['json_source_file'], confdata['source_folder']+confdata['json_destination_file'])
        if(Czy_serializacja == 1):
            if newDeserializator is None:
                print("brak obiektu deserializacji")
                break
            else:
                SerializeJson.run(newDeserializator, confdata['source_folder']+confdata['json_destination_file'])
    if(Jakie_operacje[i] == 1):
        newDeserializator = DeserializeJson(confdata['source_folder'] + confdata['json_source_file'])
    if(Jakie_operacje[i] == 2):
        Czy_serializacja = int(input("Podaj z skąd chcesz serializować: 0 - plik, 1 - obiekt"))
        if (Czy_serializacja == 0):
            ConvertJsonToYaml.run(confdata['source_folder'] + confdata['json_source_file'], confdata['source_folder'] + confdata['yaml_destination_file'])
        if (Czy_serializacja == 2):
            if newDeserializator is None:
                print("brak obiektu deserializacji")
                break
            else:
                ConvertJsonToYaml.run(newDeserializator, confdata['source_folder'] + confdata['yaml_destination_file'])
    i+=1

