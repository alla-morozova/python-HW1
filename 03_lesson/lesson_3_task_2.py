from smartphone import Smartphone
catalog = [ Smartphone("Nokia", "AN", "+79777543464"),
            Smartphone("iPhone", "16", "+79777543451"),
            Smartphone("Samsung", "S", "+79747543453"),
            Smartphone("Honor", "H3", "+79447543414"),
            Smartphone("Tesno", "T", "+79237543454")]
for  smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} . {smartphone.number}")