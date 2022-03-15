import yaml
class Yaml_odczyt:
    @staticmethod
    def run(deserializeddata, filelocation):
        print("Odczyt_yaml")
        lst = []
        # TODO – do modyfikacji
        for dep in deserializeddata.data: lst.append({
            "Kod_TERYT": dep['Kod_TERYT'],
            "Województwo": dep["Województwo"],
            "Powiat": dep["Powiat"],
            "typ_JST": dep["typ_JST"],
            "nazwa_urzędu_JST": dep["nazwa_urzędu_JST"],
            "miejscowość": dep["miejscowość"],
            "telefon_z_numerem_kierunkowym": dep["telefon kierunkowy"]
        })
        jsontemp = {"departaments": lst}
        with open(filelocation, 'w', encoding='utf-8') as f: yaml.dump(jsontemp, f, ensure_ascii=False)